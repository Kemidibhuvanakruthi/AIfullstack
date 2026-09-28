import ollama
import streamlit as st
st.title(":green[**CHATBOT**]🤖 \:tulip:")
if "messages" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question=st.chat_input("you:")

        

if question:
    with st.chat_message("user"):
        st.write("user:",question)


    st.session_state.messages.append({"role":"user",
                 "content":question})
    with st.spinner("Thinking..."):
        response=ollama.chat(
            model="llama3.2:3b",
            messages=[{"role":"system","content":"Give answer in 2 lines only"}]+st.session_state.messages
        )
    with st.chat_message("assistant"):

        st.write("AI:",response["message"]["content"])
    st.session_state.messages.append({"role":"assistant",
                 "content":response["message"]["content"]})


with st.sidebar:
    st.title("CHAT SETTINGS")
    personalities={"kid":"give the answers like you are expalining to  5 year old kid.Give the answer in 2 lines",
                   "professor":"you are an 'IIT professor'. Explain the topics using correct terminology.Give in 2 lines"}
    personality=st.selectbox("select a personality",personalities.keys())
    
    if st.button("clear cache"):
        st.session_state.messages=[]
        st.success("succesfully cleared the chat🤝")
    uploaded_file=st.file_uploader("upload a file")
    if uploaded_file is not None:
        st.success("file uploaded successfully😏..")
        
        with st.expander("preview⏮️⏮️"):
            context=uploaded_file.read().decode("utf-8")
            st.text(context)
st.balloons()
st.snow()