import requests
import streamlit as st

# Custom CSS to change icon colors
def load_css():
    css = """
    <style>
        /* Targeting the SVG icons in chat messages */
        .st-bm .st-ck svg {
            fill: #5373C4 !important; /* Change color here */
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


st.title("Clare")

load_css()


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Send the user input to FastAPI server
    response = requests.post("http://localhost:8000/parse/", json={"text": prompt})
    if response.status_code == 200:
        data = response.json()
        bot_message = f"Intent: {data['intent']}, Confidence: {data['confidence']:.2f}, Intent Number: {data['intent_number']}"
    else:
        bot_message = "Error processing request."

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(bot_message)
    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_message})

