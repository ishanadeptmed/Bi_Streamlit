import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Minimum Daily Census",
    layout="wide"
)

st.title("Minimum Daily Census")

powerbi_url = (
    "https://app.fabric.microsoft.com/reportEmbed?reportId=acc5494b-81e4-4de4-b3a2-314bce556ea1&autoAuth=true&ctid=1d7fd1ec-e7be-4f61-939a-8731f58950e5"
)

components.html(
    f"""
    <iframe
        width="100%"
        height="800"
        src="{powerbi_url}"
        frameborder="0"
        allowFullScreen="true">
    </iframe>
    """,
    height=820,
    scrolling=False
)