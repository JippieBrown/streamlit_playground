import streamlit as st
import streamlit.components.v1 as components

gantt_css = open('html/gantt_css.html', 'r', encoding='utf-8')
gantt_html = open('html/gantt.html', 'r', encoding='utf-8')

components.html(
str(
    gantt_css.read()
) + 

str(
    gantt_html.read()
)
,
height=600,
width=600
)
