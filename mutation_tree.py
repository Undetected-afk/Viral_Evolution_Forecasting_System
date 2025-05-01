
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np
from Bio import SeqIO

def score_mutation(seq1, seq2):
    # Simple scoring: +1 for match, -1 for mismatch
    score = 0
    for a, b in zip(seq1, seq2):
        if a == b:
            score += 1
        else:
            score -= 1
    return score

def build_mutation_tree(fasta_file):
    import io
    records = list(SeqIO.parse(io.StringIO(fasta_file.getvalue().decode("utf-8")), "fasta"))
    sequences = [str(rec.seq) for rec in records]
    names = [rec.id for rec in records]

    G = nx.DiGraph()
    for i, name in enumerate(names):
        G.add_node(name)

    mutation_scores = []

    for i in range(len(sequences)):
        for j in range(i+1, len(sequences)):
            score = score_mutation(sequences[i], sequences[j])
            mutation_scores.append((names[i], names[j], score))

    for a, b, score in mutation_scores:
        if score > 0:
            G.add_edge(a, b, weight=score)
        else:
            G.add_edge(b, a, weight=-score)

    return G

def draw_mutation_tree(G):
    st.subheader("🧬 Mutation Evolution Tree")
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    st.pyplot(plt)
