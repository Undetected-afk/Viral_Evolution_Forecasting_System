#!/bin/bash
echo "Activating virtual environment (if any)..."
source venv/bin/activate 2>/dev/null || echo "No venv found, continuing without activation..."
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Launching Streamlit app in debug mode..."
streamlit run app.py --logger.level=debug