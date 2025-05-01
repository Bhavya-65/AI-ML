import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0 , 50 ,18)

options = ["Python", "Java", "C++", "Javascript"]
choice = st.selectbox("Choose your favorite language:", options)

data = {
    "Name": ["John", "Jane", "Jake", "jill"],
    "Age" : [18,19,20,21],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
if name:
    st.write(f"Hello, {name}")
st.write(f"Your age is {age}. ")
st.write(f"Your favorite language is {choice}.")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write
    
