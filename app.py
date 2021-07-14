import streamlit as st
import joblib
model = joblib.load('Sentiment_Analysis_major.ipynb')
st.title('Sentiment Analyser')
ip = st.text_input('Enter your message:')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])  
