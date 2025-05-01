
import streamlit as st
from fitness_scorer import score_mutation_path

def mutation_designer():
    st.subheader("🧬 Design a Custom Variant")

    reference_seq = st.text_input("Reference Sequence", "ATGCAGTCAGTCAGTCAGTC")
    custom_seq = st.text_input("Your Mutated Sequence", "")

    if custom_seq and len(custom_seq) == len(reference_seq):
        score, warnings = score_mutation_path(reference_seq, custom_seq)
        st.success(f"✅ Fitness Score: {score}")
        if warnings:
            st.warning("⚠️ Mutation Flags:")
            for w in warnings:
                st.markdown(f"- {w}")
    elif custom_seq:
        st.error("❌ Sequence must be the same length as reference.")
