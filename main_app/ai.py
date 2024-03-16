# Had to change to version 3.10 for line 2 to work
from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# q will be for question
def get_response(q):
    response=chat.send_message(q, stream=True)
    return response

# Initialize streamlit 
st.set_page_config(page_title='ZoomerBot')
st.header('ZoomerBot')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input('Input:', key='input')
submit = st.button('Submit')

if submit and input:
    response = get_response(input)
    st.session_state['chat_history'].append(('You', input))
    st.subheader('Response')
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('ZoomerBot', chunk.text))
