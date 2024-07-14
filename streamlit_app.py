import streamlit as st
import streamlit.components.v1 as components


# @st.experimental_dialog("Contact Me")
# def show_contact_form():
#     contact_form()

def mailto_link(email, subject='', body=''):
    return f"mailto:{email}?subject={subject}&body={body}"

email = "parkerbrydon@gmail.com"
subject = "Hello 👋"
body = "I wanted to reach out regarding..."
link = mailto_link(email, subject, body)

# --- SHARED ON ALL PAGES ---
st.logo("assets/TorCrime_logo.png")
st.set_page_config(
    page_title="Brydon Parker",
    page_icon="assets/TorCrime_logo.png",
)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.jpeg", width=230)

with col2:
    st.title("Brydon Parker", anchor=False)
    st.write(
        "Founding + Principal Data Scientist at [Stan](https://stan.store/brydon)",
    )
    if st.button("✉️ Contact Me"):
        components.html(
            f"""
            <script type="text/javascript">
                window.location.href = "{link}";
            </script>
            """,
            height=0,
            width=0
        )


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("⚔️ Experience", anchor=False)
st.write(
    """
- **Stan** (2022 - Present): Founding + Principal Data Scientist
    - The sole Data Scientist at Stan - owning all things data / AI / analytics / ML
    - Stan's ARR has grown from `$1M` -> `$30M` in the 2 years since I joined
    - "One of the best hires we've ever made" - [John Hu](https://www.linkedin.com/in/johnghu/) (CEO)
- **Shopify** (2021 - 2022): Senior Data Scientist
    - Full Stack Data Scientist - data modelling, experimentation, dashboarding, metrics, ML, ...
    - Owned data science for the Shopify Starter Plan + Drove multiple initiatives across Shopify's Growth Org
    - "One of the best Data Scientists I've ever worked with" - [Alex Hui](https://www.linkedin.com/in/alexghui/) (Senior Product Lead)
- **Deloitte** (2017 - 2021): Senior Data Scientist
    - Lead Data Scientist on 100k+ SKU Retail Forecasting Project with `$1B`+ in annual revenue
    - Lead Data Scientist on NLP Risk Detection Project for major client leveraging Deep Learning 
    - "One of the top Data Scientists on the Team" - [Omar Khalil](https://www.linkedin.com/in/omar-khalil-84169631/) (Senior ML Lead)
\n[LinkedIn](https://www.linkedin.com/in/brydon-parker/)
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("🦾 Skills", anchor=False)
st.write(
    """
    - **Communication** 🗣️: Data Storytelling + Stakeholder Management + Influencing Company Wide Business Decisions
    - **Data Analysis** 🤿: Deriving meaningful insights from data to impact business decisions
    - **Dashboards** 📊: Building Status + Self Serve dashboards to monitor important metrics and enable quick deep dives into data 
    - **Experimentation** 🧪: A/B Testing, Hypothesis Testing, Metrics Design
    - **Data Engineering** 🛠️: Data Modelling, ETL, Feature Engineering, Metrics
    - **AI** 🤖: Deep Learning, AI Assistants, NLP
    - **Machine Learning** 🦾: Forecasting, Classification, Clustering
    - **Coding** 🐍: Python, SQL, streamlit
    - **Opportunity Sizing** 💰: Estimating the ROI of different initiatives based on the data
    """
)

# --- Projects ---
st.write("\n")
st.subheader("💻 Projects", anchor=False)
st.write(
    """
    - [Collection of Projects](https://stan.store/brydon)
    - [GitHub](https://github.com/parker84)
    """
)

# --- EDUCATION ---
st.write("\n")
st.subheader("🎓 Education", anchor=False)
st.write(
    """
    - **University of Toronto** (2014 - 2019): Honours Bachelor of Science in Mathematics and Statistics
    """
)
