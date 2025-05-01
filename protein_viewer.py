
import streamlit as st
import py3Dmol

def show_protein_structure(pdb_id="6VXX", mutation_sites=[]):
    st.subheader("🔬 3D Structure: SARS-CoV-2 Spike Protein")

    viewer = py3Dmol.view(query=f"pdb:{pdb_id}", width=700, height=500)
    viewer.setStyle({'cartoon': {'color': 'spectrum'}})

    # Highlight mutation sites
    for site in mutation_sites:
        viewer.addStyle({'resi': str(site)}, {'stick': {'color': 'red'}})

    viewer.zoomTo()
    viewer.spin(True)
    st.components.v1.html(viewer._make_html(), height=500, width=700)
