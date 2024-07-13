

import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/business_name_generator.py",
    title="Business Name Generator",
    icon=":material/emoji_objects:",
)
project_2_page = st.Page(
    "views/date_differ.py",
    title="Date Differ",
    icon=":material/date_range:",
)
all_projects_page = st.Page(
    "views/all_projects.py",
    title="All Projects",
    icon=":material/developer_board:",
)

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, all_projects_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/TorCrime_logo.png")
st.sidebar.markdown("Made with ❤️ by [Brydon](https://stan.store/brydon)")


# --- RUN NAVIGATION ---
pg.run()