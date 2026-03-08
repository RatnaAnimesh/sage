"""
SAGE Academic Streamer: Massive-Scale Science and Math Ingestion

A dedicated streaming daemon that continuously pulls structured relationships
from academic Wikidata ontologies (Mathematics, Physics, Chemistry, Biology).
Demonstrates SAGE's continuous O(1) memory ingestion pipeline.
"""

import urllib.request
import urllib.parse
import json
import time
import gc
from sage.memory.atomspace import AtomSpace
from sage.causality.scm import SCM
from sage.learning.ingestion import KnowledgeIngestor

print("=== Booting SAGE Massive-Scale Science Streamer ===")

space = AtomSpace("Academic_Web", db_path="sage_science.db")
dag = SCM("Science_DAG")
ingestor = KnowledgeIngestor(atomspace=space, causal_model=dag)

# Target Domains: Mathematical concept, Physical quantity, Chemical element, Biological process
TARGET_WIKIDATA_CLASSES = [
    "wd:Q1936384", # mathematical concept
    "wd:Q230238",  # physical quantity
    "wd:Q11364",   # chemical element
    "wd:Q849463",  # biological process
    "wd:Q18844855" # physical particle
]

def fetch_science_chunk(offset: int) -> list:
    print(f"--> [Network] Querying Academic Wikidata Chunk (Offset {offset})...")
    
    # We cycle through different target classes based on the offset to get a broad mix
    target_class = TARGET_WIKIDATA_CLASSES[(offset // 50) % len(TARGET_WIKIDATA_CLASSES)]
    
    # A simple, direct query that never times out on Wikidata
    query = f"""
    SELECT ?subjectLabel ?propertyLabel ?objectLabel WHERE {{
      ?subject wdt:P31 {target_class} . 
      ?subject ?p ?object .
      ?property wikibase:directClaim ?p .
      FILTER(STRSTARTS(STR(?p), "http://www.wikidata.org/prop/direct/"))
      FILTER(isIRI(?object))
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
    }} LIMIT 25 OFFSET {offset}
    """
    
    url = "https://query.wikidata.org/sparql?query=" + urllib.parse.quote(query)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'SAGE_Science_Bot/1.0', 'Accept': 'application/json'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
        triplets = []
        for item in data['results']['bindings']:
            sub = item.get('subjectLabel', {}).get('value', 'Unknown').replace(" ", "_")
            pred = item.get('propertyLabel', {}).get('value', 'Unknown').replace(" ", "_")
            obj = item.get('objectLabel', {}).get('value', 'Unknown').replace(" ", "_")
            
            # Skip unresolved HTTP URLs
            if "http" not in sub and "http" not in pred and "http" not in obj:
                # Academic facts are highly reliable, seeding with high confidence (900/1000)
                triplets.append((sub, pred, obj, 900, 1000))
                
        return triplets
        
    except Exception as e:
        print(f"    [Network Error] API Timeout or Limit Reached: {e}")
        return []

try:
    loop_count = 0
    total_ingested = 0
    total_discovered = 0
    while True:
        loop_count += 1
        print(f"\n--- Ingestion Cycle {loop_count} ---")
        
        # 1. DOWNLOAD
        chunk = fetch_science_chunk(offset=loop_count * 50)
        
        if len(chunk) > 0:
            print(f"--> [Ingest] Found {len(chunk)} new academic relationships.")
            # 2. TRAIN
            ingestor.ingest_triplets(chunk)
            total_ingested += len(chunk)
            print(f"    [AtomSpace] RAM Active Memory: {len(space.objects)} Entities, {len(space.morphisms)} Connections.")
            print(f"    [AtomSpace] Lifetime Ingested: {total_ingested} Facts.")
        
        # 3. DESTROY (Clean RAM)
        chunk.clear() 
        del chunk
        gc.collect() 
        
        # 4. PRUNE (Optimization)
        deleted = space.prune_hypotheses(confidence_threshold=0.01)
        if deleted > 0:
            print(f"    [Optimizer] Pruned {deleted} weak hypothesis links.")
            
        # 5. OFFLOAD TO DISK (Ensure O(1) Memory during infinite streaming)
        offloaded = space.offload_to_disk(max_ram_entities=3000)
        if offloaded > 0:
            print(f"    [LTM] Pushed {offloaded} stable concepts to SQLite disk storage.")
            
        print("--> Awaiting next streaming chunk to respect API limits...\n")
        time.sleep(4.0)

except KeyboardInterrupt:
    print(f"\n[Shutdown] Science streaming paused. Total academic facts ingested: {total_ingested}.")
