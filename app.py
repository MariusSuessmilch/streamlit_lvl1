import streamlit as st
from gpt_helper import chat_gpt

st.title("Hi")
import streamlit as st
from gpt_helper import chat_gpt

st.title("Hi")

# Probiere folgende Funktionen aus: st.Button, st.text_input, st.write
# Hier findest du sie beschrieben: https://docs.streamlit.io/develop/api-reference
st.write(chat_gpt("Hello", "You are a helpful assistant."))

if st.button("Click me"):
    st.write("Hello")
    