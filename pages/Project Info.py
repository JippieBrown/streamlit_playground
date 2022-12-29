import streamlit as st
import streamlit.components.v1 as components
# from app import dropdown_elements

# DB Management
import sqlite3 
def read_db(db, table, column):
	list = [k[(0)] for k in sqlite3.connect(db).cursor().execute('SELECT '+ column +' FROM '+ table +'')]
	return list


st.set_page_config(page_title="Project Info",
				   page_icon=":smile:",
				   layout="wide"
)

st.subheader("Project Info")

col1, col2, col3 = st.columns([1,2,1])

col1.markdown("Hello")

col1.markdown("PARTY ALARM!!!!!")

col1.markdown('''
- First item
- Second item
- Third item
    - Indented item
    - Indented item
- Fourth item
''')

col2.markdown("HelloHelloHelloHelloHelloHello")

col3.markdown("Hello")

cam = col2.camera_input("Take a photo")

xml_file = col2.file_uploader("Read XML")