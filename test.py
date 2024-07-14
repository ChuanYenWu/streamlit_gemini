from streamlit_mic_recorder import mic_recorder
import streamlit as st

def callback():
    if st.session_state.my_recorder_output:
        audio_bytes = st.session_state.my_recorder_output['bytes']
        st.audio(audio_bytes)


mic_recorder(key='my_recorder', callback=callback)