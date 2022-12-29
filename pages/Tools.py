import streamlit as st
from toolbox.db_tools import read_db, write_db
from PIL import Image

img_tool = Image.open('images/transparent/tool.png')

st.set_page_config(page_title="Tools",
                   page_icon=img_tool,
                   layout="wide"
)

st.header("Tools")

db_inst_tools = read_db('static_content.db','static_costs_installation_tools','tool')

st.image(img_tool, width=50)
tool = st.selectbox("Installation tools",db_inst_tools)
if st.button('add'):
	db_inst_tools = write_db('static_content.db','inst_tool',tool)
st.write(read_db('static_content.db','temp_tools','tool_item'))




