import os
import re

# The order of the paper sections
FILES = [
    "paper/00_abstract.md",
    "paper/01_introduction.md",
    "paper/02_ontology_and_memory.md",
    "paper/03_inference_and_causality.md",
    "paper/04_computational_optimizations.md",
    "paper/05_experiments_and_conclusion.md"
]

OUTPUT_TEX = "arxiv_submission/sage_paper.tex"

LATEX_PREAMBLE = r"""\documentclass[10pt,twocolumn,letterpaper]{article}

\usepackage{cvpr}
\usepackage{times}
\usepackage{epsfig}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{booktabs}
\usepackage{hyperref}

% SAGE specific math commands
\newcommand{\R}{\mathbb{R}}
\newcommand{\F}{\mathcal{F}}
\newcommand{\C}{\mathcal{C}}

\cvprfinalcopy

\def\cvprPaperID{****} % *** Enter the CVPR Paper ID here
\def\httilde{\mbox{\tt\raisebox{-.5ex}{\symbol{126}}}}

\begin{document}

\title{SAGE: Symbolic Active Generative Engine \\
A Deterministic, Topological Architecture for Autonomous General Intelligence}

\author{Animesh Ratna\\
Birla Institute of Technology and Science, Pilani\\
{\tt\small f20240665@pilani.bits-pilani.ac.in}
}

\maketitle
"""

LATEX_FOOTER = r"""
\end{document}
"""

def markdown_to_latex(text: str) -> str:
    """Basic conversion from markdown syntax to latex syntax."""
    # Abstract
    text = text.replace("**Abstract**", r"\begin{abstract}")
    if r"\begin{abstract}" in text:
        # If there's an abstract, we need to end it before the introduction
        text = text.replace("# 1. Introduction", r"\end{abstract}" + "\n\n" + r"\section{Introduction}")
    
    # Headers
    text = re.sub(r'^# \d+\. (.*?)$', r'\\section{\1}', text, flags=re.MULTILINE)
    text = re.sub(r'^## \d+\.\d+ (.*?)$', r'\\subsection{\1}', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.*?)$', r'\\subsubsection{\1}', text, flags=re.MULTILINE)
    
    # Bold text
    text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
    
    # Italic text
    text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', text)
    
    # Math blocks (just converting standard $$ to equation environment)
    # We will keep inline math $x$ as is.
    
    # Tables (Very basic conversion for the Ablation table)
    # Note: A robust converter would use pandoc, but this handles the specific SAGE table
    if "| Architecture |" in text:
        table_latex = r"""
\begin{table*}[h]
\centering
\caption{Ablation Studies on Causal Discovery Benchmark}
\begin{tabular}{lccc}
\toprule
Architecture & Discovery Steps & Hallucination Rate & Peak Memory \\
\midrule
\textbf{SAGE (Full)} & \textbf{4} & \textbf{0.0\%} & $\mathbf{O(\chi^3)}$ \\
\textit{No Coarse-Graining (RG)} & $132 \gg 4$ & 0.0\% & $O(N!)$ \\
\textit{No MPS Tensor Contraction} & DNF (Loop Limit) & N/A & OOM \\
\textit{No Topos Subobject Classes} & 12 & 14.2\% $>$ 0\% & $O(N)$ \\
\textit{Baseline Autoregressive} & N/A (Failed) & $\sim$80-90\% & $O(N^2)$ \\
\bottomrule
\end{tabular}
\end{table*}
"""
        # Strip the markdown table lines
        lines = []
        in_table = False
        for line in text.split('\n'):
            if line.startswith('| Architecture |'):
                in_table = True
                lines.append(table_latex)
            elif in_table and not line.startswith('|'):
                in_table = False
                lines.append(line)
            elif not in_table:
                lines.append(line)
        text = '\n'.join(lines)
        
    # Code Blocks (Algorithm pseudocode)
    text = re.sub(r'```text(.*?)```', r'\\begin{verbatim}\1\\end{verbatim}', text, flags=re.DOTALL)
    
    return text

def compile_paper():
    """Reads all markdown sections and compiles them into a single LaTeX file."""
    print("Compiling SAGE paper to LaTeX...")
    
    full_text = LATEX_PREAMBLE
    
    for file_path in FILES:
        if not os.path.exists(file_path):
            print(f"Warning: Missing section {file_path}")
            continue
            
        with open(file_path, 'r') as f:
            content = f.read()
            
        latex_content = markdown_to_latex(content)
        full_text += latex_content + "\n\n"
        
    full_text += LATEX_FOOTER
    
    with open(OUTPUT_TEX, 'w') as f:
        f.write(full_text)
        
    print(f"Successfully generated {OUTPUT_TEX}!")

if __name__ == "__main__":
    compile_paper()
