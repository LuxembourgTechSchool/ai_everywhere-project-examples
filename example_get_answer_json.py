import streamlit as st
from proxy import lts_proxy

prompt = st.chat_input("Write your prompt for chat completion")

if prompt:
    proxy = lts_proxy.Proxy()
    role = "You're an helpful assistant"
    prompt += ' Results MUST be in JSON format.'
    answer = proxy.get_chat(role, prompt, json_mode=True)
    st.write(answer)
    st.header('JSON')
    try:
        import json
        st.write(json.loads(answer))
    except:
        st.write('Failed to convert the answer to JSON')