import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ASLLC Dashboards",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# POWER BI REPORT URLS
# =========================================================

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


# =========================================================
# SESSION STATE
# =========================================================

if "selected_report" not in st.session_state:
    st.session_state.selected_report = None


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Remove extra page spacing */
    .block-container {
        padding-top: 0.4rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    /* Home button */
    div.stButton > button {
        min-height: 38px;
        padding: 0.2rem 0.55rem;
        font-size: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.selected_report is None:

    # Main heading
    st.markdown(
        """
        <div style="
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            margin-top: 5px;
            margin-bottom: 30px;
        ">
            ASLLC Dashboards
        </div>
        """,
        unsafe_allow_html=True
    )

    # Two dashboard options
    col1, col2 = st.columns(2)

    # -----------------------------------------------------
    # OPTION 1
    # -----------------------------------------------------

    with col1:

        st.markdown(
            """
            <div style="
                text-align: center;
                font-size: 20px;
                font-weight: 600;
                margin-bottom: 10px;
            ">
                Daily Census Report
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "📊 Open Daily Census Report",
            use_container_width=True
        ):
            st.session_state.selected_report = 1
            st.rerun()

    # -----------------------------------------------------
    # OPTION 2
    # -----------------------------------------------------

    with col2:

        st.markdown(
            """
            <div style="
                text-align: center;
                font-size: 20px;
                font-weight: 600;
                margin-bottom: 10px;
            ">
                ASLLC Daily Census Reports for Governing Facilities
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "📈 Open Governing Facilities Report",
            use_container_width=True
        ):
            st.session_state.selected_report = 2
            st.rerun()


# =========================================================
# REPORT 1 - DAILY CENSUS
# =========================================================

elif st.session_state.selected_report == 1:

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    header_left, header_center, header_right = st.columns(
        [1, 8, 1],
        vertical_alignment="center"
    )

    # Home button
    with header_left:

        if st.button(
            "🏠",
            help="HomePage"
        ):
            st.session_state.selected_report = None
            st.rerun()

    # Centered title
    with header_center:

        st.markdown(
            """
            <div style="
                text-align: center;
                font-size: 25px;
                font-weight: 700;
                line-height: 38px;
                white-space: nowrap;
                margin: 0;
                padding: 0;
            ">
                ASLLC Daily Census Report
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # POWER BI REPORT
    # -----------------------------------------------------

    components.html(
        f"""
        <iframe
            src="{powerbi_url_1}"
            width="100%"
            height="900"
            frameborder="0"
            allowfullscreen="true"
            style="
                width: 100%;
                height: 900px;
                border: none;
                display: block;
            ">
        </iframe>
        """,
        height=905,
        scrolling=False
    )


# =========================================================
# REPORT 2 - GOVERNING FACILITIES
# =========================================================

elif st.session_state.selected_report == 2:

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    header_left, header_center, header_right = st.columns(
        [1, 8, 1],
        vertical_alignment="center"
    )

    # Home button
    with header_left:

        if st.button(
            "🏠",
            help="HomePage"
        ):
            st.session_state.selected_report = None
            st.rerun()

    # Centered title
    with header_center:

        st.markdown(
            """
            <div style="
                text-align: center;
                font-size: 25px;
                font-weight: 700;
                line-height: 38px;
                white-space: nowrap;
                margin: 0;
                padding: 0;
            ">
                ASLLC Daily Census Reports for Governing Facilities
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # POWER BI REPORT
    # -----------------------------------------------------

    components.html(
        f"""
        <iframe
            src="{powerbi_url_2}"
            width="100%"
            height="900"
            frameborder="0"
            allowfullscreen="true"
            style="
                width: 100%;
                height: 900px;
                border: none;
                display: block;
            ">
        </iframe>
        """,
        height=905,
        scrolling=False
    )
