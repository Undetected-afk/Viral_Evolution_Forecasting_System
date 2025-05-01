
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show_global_map():
    st.subheader("🌍 3D Global Variant Spread Map")

    data = pd.DataFrame({
        "lat": [40.7128, 34.0522, -1.2921, 51.5074, 28.6139],
        "lon": [-74.0060, -118.2437, 36.8219, -0.1278, 77.2090],
        "variant": ["Alpha", "Delta", "Omicron", "Lambda", "Kappa"],
        "cases": [8200, 5700, 4300, 1900, 1600]
    })

    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lon = data["lon"],
        lat = data["lat"],
        text = data["variant"],
        marker = dict(
            size = data["cases"] / 300,
            color = "red",
            opacity = 0.7,
            line=dict(width=1, color="white")
        ),
        mode = "markers",
    ))

    fig.update_geos(
        projection_type="orthographic",
        showland=True, landcolor="rgb(230, 230, 230)",
        showocean=True, oceancolor="LightBlue",
        showlakes=True, lakecolor="LightBlue",
        showrivers=True, rivercolor="Blue",
    )

    fig.update_layout(
        title="3D Earth View of Variant Spread",
        margin=dict(l=0, r=0, t=30, b=0),
        geo=dict(
            projection_rotation=dict(lon=0, lat=0, roll=0),
            showcountries=True,
        )
    )

    st.plotly_chart(fig, use_container_width=True)
