
import streamlit as st
import plotly.express as px
import pandas as pd

def show_global_map():
    st.subheader("🌍 3D Time-Lapse Globe of Variant Spread")

    # Simulated time-series mutation spread data
    data = pd.DataFrame({
        "lat": [40.7128, 34.0522, -1.2921, 51.5074, 28.6139, 19.4326, -33.8688],
        "lon": [-74.0060, -118.2437, 36.8219, -0.1278, 77.2090, -99.1332, 151.2093],
        "variant": ["Alpha", "Delta", "Omicron", "Lambda", "Kappa", "Pi", "Theta"],
        "cases": [8200, 5700, 4300, 1900, 1600, 800, 400],
        "date": ["2022-01", "2022-02", "2022-03", "2022-04", "2022-05", "2022-06", "2022-07"]
    })

    fig = px.scatter_geo(
        data,
        lat="lat",
        lon="lon",
        color="variant",
        size="cases",
        hover_name="variant",
        animation_frame="date",
        projection="orthographic",
        title="Variant Spread Over Time (Animated Globe)"
    )

    fig.update_traces(marker=dict(line=dict(width=1, color="white")))
    fig.update_geos(
        showland=True, landcolor="rgb(230, 230, 230)",
        showocean=True, oceancolor="LightBlue",
        showlakes=True, lakecolor="LightBlue"
    )
    fig.update_layout(margin=dict(r=0, t=30, l=0, b=0))
    st.plotly_chart(fig, use_container_width=True)
