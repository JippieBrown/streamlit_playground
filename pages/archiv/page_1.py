import streamlit as st
import streamlit.components.v1 as components
from toolbox.db_tools import read_db
from st_aggrid import AgGrid



st.set_page_config(page_title="Test",
                   page_icon=":poop:",
                   layout="wide"
)

st.subheader("Home")

test = read_db('static_content.db','dropdown_elements','plant_type')
gis_type = st.selectbox("Menu",test)
if st.button('add'):
	st.write(gis_type)

from PIL import Image
image = Image.open('Siemens_Energy_logo.png')

st.image(image, caption='caption text', width=200)
# bootstrap 4 collapse example
components.html(
    '''
<div style="color:white;">
''' + str(test) +  '''
</div>
    ''',
    height=600,width=600
)
