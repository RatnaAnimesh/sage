"""
SAGE Continuous Knowledge Streamer

This script demonstrates the "Download -> Train -> Destroy" paradigm.
Instead of loading a Gigabyte dataset into RAM, SAGE:
1. Opens a network stream to a Knowledge API (e.g. Wikidata SPARQL).
2. Downloads a tiny chunk of (Subject, Predicate, Object) triplets.
3. Ingests them into the AtomSpace (updating NALS logic and Engram tape).
4. Explicitly OVERWRITES and DELETES the downloaded raw data from RAM.
5. Runs the Garbage Collector to prune useless AtomSpace links.
6. Repeats recursively.
"""

import urllib.request
import urllib.parse
import json
import time
import sys
import gc
from sage.memory.atomspace import AtomSpace
from sage.causality.scm import SCM
from sage.learning.ingestion import KnowledgeIngestor

print("=== SAGE Live Streaming Ingestor Initiated ===")

space = AtomSpace("Live_Web")
dag = SCM("Real_World_DAG")
ingestor = KnowledgeIngestor(atomspace=space, causal_model=dag)

# A fast SPARQL query to get random facts about prominent entities (e.g. Cities, Planets, People)
# We shuffle the offset to pull new streaming data every loop
def fetch_wikidata_chunk(offset: int) -> list:
    print(f"--> [Network] Downloading raw Wikidata chunk (Offset {offset})...")
    
    query = f"""
    SELECT ?subjectLabel ?predicateLabel ?objectLabel WHERE {{
      {{
        SELECT ?subject ?predicate ?object WHERE {{
          ?subject wdt:P31 wd:Q515 . # Instances of Cities
          ?subject ?predicate ?object .
          FILTER(isIRI(?object))
        }} LIMIT 50 OFFSET {offset}
      }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
    }}
    """
    
    url = "https://query.wikidata.org/sparql?query=" + urllib.parse.quote(query)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'SAGE_Prototype_Bot/1.0', 'Accept': 'application/json'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
        triplets = []
        for item in data['results']['bindings']:
            sub = item.get('subjectLabel', {}).get('value', 'Unknown').replace(" ", "_")
            pred = item.get('predicateLabel', {}).get('value', 'Unknown').replace(" ", "_")
            obj = item.get('objectLabel', {}).get('value', 'Unknown').replace(" ", "_")
            
            # If the API didn't return an English label, it returns an HTTP URL. We skip those.
            if "http" not in sub and "http" not in pred and "http" not in obj:
                # We assume a base confidence of 500 positive hits for Wikidata facts
                triplets.append((sub, pred, obj, 500, 500))
                
        return triplets
        
    except Exception as e:
        print(f"    [Network Error] Could not reach Wikidata: {e}")
        # Fallback to simulate web stream if offline
        return [("Data_Stream", "Is", "Offline", 1, 1)]

# The Recursive Training Loop
try:
    loop_count = 0
    while True:
        loop_count += 1
        print(f"\n--- Ingestion Cycle {loop_count} ---")
        
        # 1. DOWNLOAD
        # We offset the query by 50 each time to simulate a continuous stream read
        raw_data_block = fetch_wikidata_chunk(offset=loop_count * 50)
        
        if len(raw_data_block) > 0:
            print(f"--> [Ingest] Teaching SAGE {len(raw_data_block)} new facts...")
            # 2. TRAIN
            ingestor.ingest_triplets(raw_data_block)
            
            print(f"    SAGE AtomSpace now contains {len(space.objects)} Entities and {len(space.morphisms)} Connections.")
        
        # 3. DESTROY
        print("--> [RAM Cleanup] Shredding raw JSON dataset from computer memory...")
        
        # Explicitly overwrite the list in memory to prevent data remanence, then delete
        raw_data_block.clear() 
        del raw_data_block
        
        # Force Python's C-backend garbage collector to physically free the RAM
        gc.collect() 
        
        # 4. PRUNE (Optimization)
        # SAGE forgets useless hypotheses to stay lightweight
        deleted = space.prune_hypotheses(confidence_threshold=0.01)
        if deleted > 0:
            print(f"    [Optimizer] Pruned {deleted} dead hypothesis links.")
            
        print("--> Holding for next streaming chunk...\n")
        time.sleep(3.0)

except KeyboardInterrupt:
    print("\n[Shutdown] Streaming connection closed safely.")
