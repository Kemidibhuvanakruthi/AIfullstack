import streamlit as st
st.title("welcome to my first app")
name=st.text_input("enter your name")
email=st.chat_input("enetr your email")
if st.button("submit"):
    st.write("Hello",name)
    

