import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
# import leafmap.foliumap as leafmap
from streamlit_folium import st_folium
import folium

st.set_page_config(layout="wide")

start_coords = [52.44718037871482, 13.42348578273783]
m = folium.Map(location=start_coords, zoom_start=16)

folium.Marker(
    [52.44718037871482, 13.44348578273783],
    popup="Test",
    tooltip="auch test"
).add_to(m)

# render map
st_data = st_folium(m, width = "wide")



# df = pd.DataFrame(
#     np.array([[52.44718037871482, 13.42348578273783]]),
#     columns=['lat', 'lon'])


# st.map(df)


# HtmlFile = open("html/map.html", 'r', encoding='utf-8')
# source_code = HtmlFile.read() 
# # print(source_code)
# components.html(source_code,height=1200)


# from bokeh.models.widgets import Button
# from bokeh.models import CustomJS
# from streamlit_bokeh_events import streamlit_bokeh_events

# loc_button = Button(label="Get Location")
# loc_button.js_on_event("button_click", CustomJS(code="""
#     navigator.geolocation.getCurrentPosition(
#         (loc) => {
#             document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
#         }
#     )
#     """))
# result = streamlit_bokeh_events(
#     loc_button,
#     events="GET_LOCATION",
#     key="get_location",
#     refresh_on_update=False,
#     override_height=75,
#     debounce_time=0)