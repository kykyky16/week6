# pages/01_Full_JSON_Viewer.py
import json
from pathlib import Path
import streamlit as st
import pandas as pd

st.markdown("All Courses")
st.sidebar.markdown("All Courses")

st.title("Course Catalog")

st.set_page_config(page_title="Full JSON Viewer", layout="wide")
st.title("Full JSON File Viewer")

json_path = "/workspaces/week6/data/courses-full.json"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)


for course_name, details in data.items():
    with st.expander(course_name):
        st.table(pd.DataFrame(details.items(), columns=["Attribute", "Value"]))

st.subheader("Raw JSON")
st.json(data)

st.subheader("Pretty Printed")
st.code(json.dumps(data, indent=2, ensure_ascii=False), language="json")

