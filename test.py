import streamlit as st
st.set_page_config(
    page_title="Art Faculty Data"
)
visualise = st.Page('studentSurvey.py', title='Pencapaian Akademik', icon=":material/school:")

home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, visualise]
        }
    )

pg.run()
