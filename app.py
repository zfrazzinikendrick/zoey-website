import streamlit as st
import numpy as np
import datetime


def home_page():
    st.title(":green[Zoey's Website]")

def resume_page():
    st.title("Resume Page")
    st.markdown("supporting text... bla bla bla...")

def project_page():
    st.title("Projects")
    st.markdown("placeholder text.... bla bla bla...")


#page = st.navigation(
#    {"Home": home_page,
#    "Resume": resume_page,
#    "Projects": project_page},
#    position="top",
#    expanded=True
#)
pages = [st.Page(home_page, title="Home"), 
     st.Page(resume_page, title="Resume"), 
     st.Page(project_page, title="Projects")
    ]
page = st.navigation(
    pages,
    position="top",
    expanded=True
)

page.run()