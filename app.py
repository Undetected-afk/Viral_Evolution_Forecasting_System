
import streamlit as st
from mutation_dp import trace_mutation_path
from prediction import forecast_mutations
from visualizer import show_global_map
from protein_viewer import show_protein_structure
from mutation_tree import build_mutation_tree, draw_mutation_tree
from sir_model import show_sir_simulation
from alphafold_viewer import render_mutant_structure

st.set_page_config(page_title="Viral Evolution Forecasting System", layout="wide")
st.title("🧬 Viral Evolution & Mutation Forecasting System")

st.markdown("Track, analyze, and forecast viral mutations globally using dynamic programming.")

uploaded_file = st.file_uploader("📄 Upload a FASTA file with viral genome sequences", type=["fasta"])
if uploaded_file:
    st.success("FASTA file uploaded successfully.")
    with st.spinner("🔍 Analyzing mutations..."):
        mutation_path_log = trace_mutation_path(uploaded_file)
    st.subheader("🔬 Mutation Trace (DP-Based)")
    st.code(mutation_path_log)

    st.subheader("📈 Predicted Next Mutations (DP Forecasting)")
    predictions = forecast_mutations(mutation_path_log)
    st.json(predictions)

    st.subheader("🌍 Global Variant Spread Visualization")
    show_global_map()

    if st.checkbox("🧬 Show 3D Spike Protein Structure with Mutation Sites"):
        show_protein_structure(pdb_id="6VXX", mutation_sites=[614, 501, 484])

    if st.checkbox("🧠 Visualize Mutation Evolution Tree"):
        G = build_mutation_tree(uploaded_file)
        draw_mutation_tree(G)

    if st.checkbox("📊 Simulate Infection Spread and Mutation Emergence (SIR+M)"):
        show_sir_simulation()

    if st.checkbox("🧬 Visualize Mutant vs Wild-Type Protein (AlphaFold View)"):
        render_mutant_structure()
else:
    st.warning("Please upload a FASTA file to start the analysis.")
