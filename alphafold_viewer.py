
import streamlit as st
import py3Dmol

def render_mutant_structure(reference_pdb_id="6VXX", mutated_residues=[614, 501, 484]):
    st.subheader("🧬 Wild-Type vs Mutated Protein Structure (Simulated)")

    # Viewer for wild-type structure
    st.markdown("#### Wild-Type Structure")
    wt_viewer = py3Dmol.view(query=f"pdb:{reference_pdb_id}", width=600, height=400)
    wt_viewer.setStyle({'cartoon': {'color': 'spectrum'}})
    wt_viewer.zoomTo()
    st.components.v1.html(wt_viewer._make_html(), height=400, width=600)

    # Viewer for mutant structure
    st.markdown("#### Simulated Mutant Structure (highlighted in red)")
    mut_viewer = py3Dmol.view(query=f"pdb:{reference_pdb_id}", width=600, height=400)
    mut_viewer.setStyle({'cartoon': {'color': 'lightgrey'}})
    for res in mutated_residues:
        mut_viewer.addStyle({'resi': str(res)}, {'stick': {'color': 'red'}, 'cartoon': {'color': 'red'}})
    mut_viewer.zoomTo()
    mut_viewer.spin(True)
    st.components.v1.html(mut_viewer._make_html(), height=400, width=600)
