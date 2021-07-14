import streamlit as st
import joblib
st.title('Sentiment_Analyzer - Tweet_Reviews')
test_model = joblib.load('Sentiment_Analyser')
ip = st.text_input('Enter your message')
op = test_model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
if (op==0):
  st.title('POSITIVE')
else :
  st.title('NEGATIVE')
   
