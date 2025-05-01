
# Multi-objective mutation fitness scoring engine
from Bio.Seq import Seq

# Simplified BLOSUM-like matrix for scoring (custom)
AA_SCORE_MATRIX = {
    ('A', 'A'): 1, ('A', 'G'): 0, ('A', 'T'): -1, ('A', 'C'): -2,
    ('G', 'G'): 1, ('G', 'A'): 0, ('G', 'T'): -1, ('G', 'C'): -2,
    ('T', 'T'): 1, ('T', 'A'): -1, ('T', 'G'): -1, ('T', 'C'): -2,
    ('C', 'C'): 1, ('C', 'A'): -2, ('C', 'T'): -2, ('C', 'G'): -1,
}

# Known immune escape mutations (example positions)
IMMUNE_ESCAPE_SITES = {
    484: "E484K",
    417: "K417N",
    501: "N501Y"
}

def score_mutation_path(seq1: str, seq2: str):
    score = 0
    warnings = []

    for i in range(min(len(seq1), len(seq2))):
        a, b = seq1[i], seq2[i]
        if a == b:
            score += 1
        else:
            score += AA_SCORE_MATRIX.get((a, b), -3)

            # Check for immune escape
            if i in IMMUNE_ESCAPE_SITES:
                score += 5  # bonus if immune escape known
                warnings.append(f"⚠️ Immune escape mutation at position {i+1}: {IMMUNE_ESCAPE_SITES[i]}")

    return score, warnings
