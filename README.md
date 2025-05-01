# Viral Evolution & Mutation Forecasting System (VEMFS)

This project is a dynamic programming-based bioinformatics application designed to:
- Trace mutation paths of viral genome sequences
- Forecast next likely mutations
- Visualize global variant spread
- Simulate viral transmission and mutation emergence (SIR model)
- Compare wild-type and mutant 3D protein structures using PDB
- Display an evolutionary mutation tree

## 🚀 Features
- Streamlit interactive dashboard
- 3D visualizations (Py3Dmol, Plotly)
- Real viral genome input (FASTA)
- Advanced DP-based bioinformatics modeling

## 💻 How to Run (Locally)
1. Install requirements:
    ```
    pip install -r requirements.txt
    ```
2. Launch Streamlit:
    ```
    streamlit run app.py
    ```

## 🌐 Deploying to Streamlit Cloud
1. Upload this folder to a public GitHub repo
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New App", select this repo, set `app.py` as entry point

## 📂 Project Structure
- `app.py` – Main Streamlit interface
- `mutation_dp.py` – Sequence alignment logic (DP)
- `prediction.py` – Mutation forecast engine
- `sir_model.py` – Infection + mutation simulation
- `visualizer.py` – World map of variant spread
- `mutation_tree.py` – Evolutionary graph viewer
- `protein_viewer.py` & `alphafold_viewer.py` – 3D visualization

---

Built with ❤️ for real-world bioinformatics.