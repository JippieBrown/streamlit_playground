import streamlit as st


import requests
from bs4 import BeautifulSoup as bs

def search(query):
    # Suchanfrage an die Google-Suche senden
    url = "https://www.google.com/search?q=" + query
    response = requests.get(url)

    # HTML-Antwort parsen
    soup = bs(response.text, "html.parser")

    # Erstes Suchergebnis auswählen
    result = soup.find("div", {"class": "g"})

    # Titel und Link des Suchergebnisses ausgeben
    print(result.find("h3").text)
    print(result.find("a")["href"])

# Beispielaufruf
search("Python programming language")

st.write(search("Python programming language"))