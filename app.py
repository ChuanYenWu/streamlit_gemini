import time
from dotenv import load_dotenv
import streamlit as st

import numpy as np
import pandas as pd

import os
import google.generativeai as ggi

from streamlit_float import *

from voice import record_voice

# Float feature initialization
float_init()

# local with .env file
#load_dotenv(".env")
#fetcheed_api_key = os.getenv("API_KEY")
# for Streamlit Community Cloud
fetcheed_api_key = st.secrets['API_KEY']
ggi.configure(api_key = fetcheed_api_key)

#model = ggi.GenerativeModel("gemini-pro") 
#chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question,stream=True)
    return response

def input_selector():
    input_options = ["Key", "Voice"]
    with st.sidebar: 
        return st.selectbox("Input select", input_options)

st.title("Chat Application using Gemini Pro")

def main():
    st.session_state.gemini_history = []
    st.session_state.model = ggi.GenerativeModel('gemini-pro')
    st.session_state.chat = st.session_state.model.start_chat(
        history=st.session_state.gemini_history,
    )

    inputtype = input_selector()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    input_container = st.container()
    if inputtype == "Key":
        with input_container:
            prompt = st.chat_input('Your message here...')
    elif inputtype == "Voice":
        with input_container:
            prompt = record_voice()

        # React to user input
        #if prompt := st.chat_input('Your message here...'):
    if prompt:
    
        # Display user message in chat message container
        with st.chat_message('user'):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append(
            {
                "role":'user',
                "content":prompt,
            }
        )
        ## Send message to AI
        response = st.session_state.chat.send_message(
            prompt,
            stream=True,
        )
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ''
            assistant_response = response
            # Streams in a chunk at a time
            for chunk in response:
                # Simulate stream of chunk
                # TODO: Chunk missing `text` if API stops mid-stream ("safety"?)
                for ch in chunk.text.split(' '):
                    full_response += ch + ' '
                    time.sleep(0.05)
                    # Rewrites with a cursor at end
                    message_placeholder.write(full_response + '▌')
            # Write full message with placeholder
            message_placeholder.write(full_response)

        # Add assistant response to chat history
        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":st.session_state.chat.history[-1].parts[0].text,
            }
        )
        st.session_state.gemini_history = st.session_state.chat.history

    # floating_audio_bar()
    chat_input_css = float_css_helper(bottom="1rem", display="flex", justify_content="center", margin="0 auto", max_width="800px")
    # Float button container
    input_container.float(chat_input_css)



if __name__ == "__main__":
    main()