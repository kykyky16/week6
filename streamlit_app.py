import streamlit as st

main_page = st.Page("main.py", title="Main Page")
page_2 = st.Page("aboutus.py", title="About Us")
page_3 = st.Page("allcourses.py", title="All Courses")

pg = st.navigation([main_page,page_2,page_3])
pg.run()