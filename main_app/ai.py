# Had to change to version 3.10 for line 2 to work
from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
from vertexai.preview.generative_models import GenerativeModel

GenerativeModel.configure(api_key=os.getenv('API_KEY'))

model = GenerativeModel('gemini-1.0-pro')