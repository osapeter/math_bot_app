#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from math_bot import process_math_question

st.set_page_config(page_title="Kiddo Math Bot 🤖", page_icon="🧠")

st.title("Kiddo Math Chatbot 🤖🎓")
st.write("Ask me anything like 'What is 5 + 3?' or '7 x 2'!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

user_input = st.chat_input("What's your math question?")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    bot_response = process_math_question(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.chat_message("assistant").write(bot_response)

