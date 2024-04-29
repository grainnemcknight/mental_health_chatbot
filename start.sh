#!/bin/bash

# Start Uvicorn with FastAPI app
echo "Starting FastAPI app..."
uvicorn app:app --host 0.0.0.0 --port 8000 &

# Start Rasa server
echo "Starting Rasa server..."
rasa run --enable-api -m rasa_chatbot/models/nlu-20240429-204439-slim-nugget.tar.gz &

# Start Streamlit app
echo "Starting Streamlit app..."
streamlit run streamlit_app.py &

# Keep script running
wait
