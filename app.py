# ---------------------------------------------------------
# REPORT 1
# ---------------------------------------------------------
elif st.session_state.selected_report == 1:

    # Header row
    col_home, col_title, col_right = st.columns([1, 8, 1])

    with col_home:
        if st.button("🏠", help="HomePage"):
            st.session_state.selected_report = None
            st.rerun()

    with col_title:
        st.markdown(
            """
            <div style="
                text-align: center;
                font-size: 26px;
                font-weight: 700;
                line-height: 1.5;
                margin: 0;
                padding: 0;
            ">
                ASLLC Daily Census Report
            </div>
            """,
            unsafe_allow_html=True
        )

    # Power BI report
    components.html(
        f"""
        <iframe
            width="100%"
            height="900"
            src="{powerbi_url_1}"
            frameborder="0"
            allowfullscreen="true"
            style="border:none;">
        </iframe>
        """,
        height=905,
        scrolling=False
    )


# ---------------------------------------------------------
# REPORT 2
# ---------------------------------------------------------
elif st.session_state.selected_report == 2:

    # Header row
    col_home, col_title, col_right = st.columns([1, 8, 1])

    with col_home:
        if st.button("🏠", help="HomePage"):
            st.session_state.selected_report = None
            st.rerun()

    with col_title:
        st.markdown(
            """
            <div style="
                text-align: center;
                font-size: 26px;
                font-weight: 700;
                line-height: 1.5;
                margin: 0;
                padding: 0;
            ">
                ASLLC Daily Census Reports for Governing Facilities
            </div>
            """,
            unsafe_allow_html=True
        )

    # Power BI report
    components.html(
        f"""
        <iframe
            width="100%"
            height="900"
            src="{powerbi_url_2}"
            frameborder="0"
            allowfullscreen="true"
            style="border:none;">
        </iframe>
        """,
        height=905,
        scrolling=False
    )
