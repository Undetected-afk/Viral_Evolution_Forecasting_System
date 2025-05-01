
import streamlit as st
import plotly.express as px
import pandas as pd

def show_global_map():
    st.info("🌍 Simulated Global Variant Spread")

    data = pd.DataFrame({
        "lat": [40.7128, 34.0522, -1.2921, 51.5074, 28.6139],
        "lon": [-74.0060, -118.2437, 36.8219, -0.1278, 77.2090],
        "variant": ["Alpha", "Delta", "Omicron", "Lambda", "Kappa"],
        "cases": [8200, 5700, 4300, 1900, 1600]
    })

    fig = px.scatter_geo(
        data,
        lat="lat",
        lon="lon",
        color="variant",
        size="cases",
        hover_name="variant",
        size_max=30,
        projection="natural earth",
        title="Global Variant Spread Simulation"
    )

    fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)
