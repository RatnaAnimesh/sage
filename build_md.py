import sys
import re

files = [
    "paper/00_abstract.md",
    "paper/01_introduction.md",
    "paper/02_ontology_and_memory.md",
    "paper/03_inference_and_causality.md",
    "paper/04_computational_optimizations.md",
    "paper/05_experiments_and_conclusion.md",
    "paper/06_discussion_and_rebuttals.md",
    "paper/07_conclusion_and_future_work.md",
    "paper/08_appendix.md",
    "paper/09_glossary.md",
    "paper/10_comparative_taxonomy.md"
]

header = """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>

<div align="center">
  <h1>SAGE: Symbolic Active Generative Engine</h1>
  <h2>A Deterministic, Topological Architecture for Autonomous General Intelligence</h2>
  <br>
  <b>Animesh Ratna</b><br>
  Birla Institute of Technology and Science, Pilani<br>
  <i>f20240665@pilani.bits-pilani.ac.in</i>
  <br><br>
</div>

"""

with open("sage_manuscript.md", "w") as f_out:
    f_out.write(header)
    for file in files:
        with open(file, "r") as f_in:
            content = f_in.read()
            # Remove the original title header from abstract
            if file == "paper/00_abstract.md":
                content = re.sub(r"^# Grounding.*", "", content)
            f_out.write(content + "\n\n")

print("Created sage_manuscript.md")
