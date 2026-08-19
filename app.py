import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ASLLC Dashboards",
    layout="wide"
)

# Report URLs
powerbi_url_1 = (
    "https://app.fabric.microsoft.com/reportEmbed?"
    "reportId=acc5494b-81e4-4de4-b3a2-314bce556ea1"
    "&autoAuth=true"
    "&ctid=1d7fd1ec-e7be-4f61-939a-8731f58950e5"
)

powerbi_url_2 = (
    "https://app.fabric.microsoft.com/reportEmbed?"
    "reportId=38adb732-64dd-4118-8b96-918d707e2861"
    "&autoAuth=true"
    "&ctid=1d7fd1ec-e7be-4f61-939a-8731f58950e5"
)

# Initialize selected report
if "selected_report" not in st.session_state:
    st.session_state.selected_report = None

# Home page
if st.session_state.selected_report is None:

    st.title("ASLLC Dashboards")
    st.write("Please select a dashboard:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "📊 Daily Census Report",
            use_container_width=True
        ):
            st.session_state.selected_report = 1
            st.rerun()

    with col2:
        if st.button(
            "📊 ASLLC Daily Census Reports for Governing Facilities",
            use_container_width=True
        ):
            st.session_state.selected_report = 2
            st.rerun()

# Report 1
elif st.session_state.selected_report == 1:

    if st.button("← Back to Dashboards"):
        st.session_state.selected_report = None
        st.rerun()

    st.title("Daily Census Report")

    components.html(
        f"""
        <iframe
            width="100%"
            height="800"
            src="{powerbi_url_1}"
            frameborder="0"
            allowfullscreen="true">
        </iframe>
        """,
        height=820,
        scrolling=False
    )

# Report 2
elif st.session_state.selected_report == 2:

    if st.button("← Back to Dashboards"):
        st.session_state.selected_report = None
        st.rerun()

    st.title("Additional Report")

    components.html(
        f"""
        <iframe
            width="100%"
            height="800"
            src="{powerbi_url_2}"
            frameborder="0"
            allowfullscreen="true">
        </iframe>
        """,
        height=820,
        scrolling=False
    )
