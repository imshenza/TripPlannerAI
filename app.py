import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI()
initial_message=[{"role":"system","content":"You are a dubai trip planner. You help user to pan their trip to Dubai. Your respose should not exceed 100 words. You are an expert in Dubai tourism,food cuulture. You can customize itinerary according to user needs. Ask questuions to user to customize according to what they need, after letting them explain what they need"},
                 {"role":"assistant",
                  "content":"I am an AI assistant that can help you plan your trip to Dubai. What would you like to know?"}]


if "messages" not in st.session_state:
    st.session_state.messages=initial_message
st.title("Dubai Trip Planner")
for message in st.session_state.messages:
    if message["role"]!="system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
user_message=st.chat_input("Enter your message")
if user_message:
    new_message={"role":"user","content":user_message}
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
        st.markdown(new_message["content"])
def get_respose_from_llm(messages):
    completion=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return completion.choices[0].message.content

response = get_respose_from_llm(st.session_state.messages)
if response:
    response_message={"role":"assistant","content":response}
    st.session_state.messages.append(response_message)
    with st.chat_message(response_message["role"]):
        st.markdown(response_message["content"])