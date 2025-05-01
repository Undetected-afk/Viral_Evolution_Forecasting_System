
from Bio import SeqIO
import numpy as np

def trace_mutation_path(fasta_file):
    # Read sequences
    import io
    sequences = list(SeqIO.parse(io.StringIO(fasta_file.getvalue().decode("utf-8")), "fasta"))

    
    if len(sequences) < 2:
        return "Need at least 2 sequences for mutation tracing."

    # Convert to strings
    seqs = [str(record.seq) for record in sequences]

    # Perform pairwise DP alignment (simplified global alignment)
    path_log = []
    for i in range(len(seqs) - 1):
        score, alignment = align_sequences(seqs[i], seqs[i+1])
        path_log.append(f"Alignment {i+1}: Score {score}\n{alignment[0]}\n{alignment[1]}\n")

    return "\n".join(path_log)

def align_sequences(seq1, seq2):
    match_score = 1
    mismatch_penalty = -1
    gap_penalty = -2

    m, n = len(seq1), len(seq2)
    dp = np.zeros((m+1, n+1))
    for i in range(m+1):
        dp[i][0] = i * gap_penalty
    for j in range(n+1):
        dp[0][j] = j * gap_penalty

    for i in range(1, m+1):
        for j in range(1, n+1):
            match = dp[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty)
            delete = dp[i-1][j] + gap_penalty
            insert = dp[i][j-1] + gap_penalty
            dp[i][j] = max(match, delete, insert)

    aligned1, aligned2 = "", ""
    i, j = m, n
    while i > 0 and j > 0:
        current = dp[i][j]
        if current == dp[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty):
            aligned1 = seq1[i-1] + aligned1
            aligned2 = seq2[j-1] + aligned2
            i -= 1
            j -= 1
        elif current == dp[i-1][j] + gap_penalty:
            aligned1 = seq1[i-1] + aligned1
            aligned2 = "-" + aligned2
            i -= 1
        else:
            aligned1 = "-" + aligned1
            aligned2 = seq2[j-1] + aligned2
            j -= 1

    while i > 0:
        aligned1 = seq1[i-1] + aligned1
        aligned2 = "-" + aligned2
        i -= 1
    while j > 0:
        aligned1 = "-" + aligned1
        aligned2 = seq2[j-1] + aligned2
        j -= 1

    return dp[m][n], (aligned1, aligned2)
