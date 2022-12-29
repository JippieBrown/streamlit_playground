import streamlit as st
import pybase64

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = pybase64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="900" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)