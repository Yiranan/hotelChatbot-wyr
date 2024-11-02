
"""
This script is a simple web demo based on Streamlit, showcasing the use of the ChatGLM3-6B model. For a more comprehensive web demo,
it is recommended to use 'composite_demo'.

Usage:
- Run the script using Streamlit: `streamlit run web_demo_streamlit.py`
- Adjust the model parameters from the sidebar.
- Enter questions in the chat input box and interact with the ChatGLM3-6B model.

Note: Ensure 'streamlit' and 'transformers' libraries are installed and the required model checkpoints are available.
"""

import streamlit as st

from GLM4API import LLMAPI

import online_main

from getVector import PARSE
import time


st.set_page_config(
    page_title="hotel chatbot",
    page_icon=":robot:",
    layout="wide"
)

@st.cache_resource
def get_model():
    parse_vector=PARSE()
    return parse_vector



parse_vector = get_model()

max_length = st.sidebar.slider("max_length", 0, 32768, 8192, step=1)

temperature = st.sidebar.slider("temperature", 0.0, 1.0, 0.6, step=0.01)

buttonLLM = st.sidebar.button("USE LLM", key="YES")
LLM_flag=0
if buttonLLM:
    api=LLMAPI()
    LLM_flag=1



with st.chat_message(name="user", avatar="user"):
    input_placeholder = st.empty()
with st.chat_message(name="assistant", avatar="assistant"):
    message_placeholder = st.empty()
markdown_container = st.empty()
prompt_text = st.chat_input("please input your question")


if prompt_text:
    # markdown_container.empty()
    
    try:
        input_placeholder.markdown(prompt_text)
        # prompt_text='Can I reserve multiple venues for one event at Warwick Conferences?'
        query_vector=parse_vector.parse(prompt_text)
        print(prompt_text)
        response = online_main.RAG(query_vector,top_n=1)# from RAG get answer
        if LLM_flag==1:
            # api=LLMAPI()
            print("api loaded")
            answer=api.QA('question:'+prompt_text+'prompt:'+response)
            # answer = response.split("Answer:")[1]
        else:
            # response = online_main.RAG(query_vector,top_n=1)# from RAG get answer
            # print(response)
            # message_placeholder.markdown(response)
            # response="Yes, multiple venues can be reserved for larger events."
            # match = re.search(r'Answer:(.*)', response)
            answer = response.split("Answer:")[1]

        temp=""
        for i in answer:
            time.sleep(0.05)
            temp=temp+i
            print(temp)
            message_placeholder.markdown(temp)



        # message_placeholder.markdown(answer_part)
 


    except:
        message_placeholder.markdown("program error, please contact engineer")
