import google.generativeai as genai
import streamlit as st
import time

RESPONSE = """ """

def stream_data():
    for word in RESPONSE.split(" "):
        yield word + " "
        time.sleep(0.04)


genai.configure(api_key= "AIzaSyCtbkn_fspnC96QyY3b1fdOkqp4ZnKYWpI")

st.title("🍃 PrakritiAI", help="AI Based Prakriti q/a chatbot")
st.write("your personel health assistant is here ")
st.write("Ask me about ayurveda , yoga and Prakriti")
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", 
                            system_instruction="""Your name is 🍃 PrakritiAI, and
                                                You are ayurveda expert and yoga expert and a helpful and polite assistant,
                                                you will provide answer to the given question related to ayurveda and prakriti
                                                and resolve the user's queries be specific and brief, if the topic is not related to ayurveda health or prakriti
                                                then you can politely request the user to ask questions related to ayurveda health or prakriti, domain.
                                            """)
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

prompt = st.chat_input("Ask anything related to ayurveda...")

if prompt:
    st.chat_message("user").write(prompt)
    response = chat.send_message(prompt)
    RESPONSE = response.text
    st.chat_message("🍃").write(RESPONSE)
    st.session_state["chat_history"]=chat.history