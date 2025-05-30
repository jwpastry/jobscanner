import streamlit as st
import time

import base64
from typing import Any

def get_base64_of_file(file_path: str) -> str:
    with open(file_path, "rb") as file:
        content: bytes = file.read()
        encoded: str = base64.b64encode(content).decode()
    return encoded

img_path = "background.png"
img_base64 = get_base64_of_file(img_path)
print(img_base64)
page_bg_img = f'''
    <style>
    body {{
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
''' % img_base64

print(page_bg_img)

st.markdown(page_bg_img, unsafe_allow_html=True)



st.title("Welcome to the atlas!")
with st.spinner("Initializing...", show_time=False):
    time.sleep(1.5)

st.image("Screen Shot 2025-04-10 at 10.20.52 AM.png")

col1,col2,col3,col4 = st.columns(4)
st.write("Click on a location button to show their job market sector!")

with col1:
    st.link_button("US", "http://localhost:8501/pageamerica")
    st.write("The US as an entirety of a job market is divided between private and public. The public sector has different application requirements and is state-centered compared to the private sector for the education sector.")

with col2:
    st.link_button("EU", "http://localhost:8501/pageuro")
    st.write("The EU has multiple countries with various industries that are very vibrant, and Europe is also known for a large amount of Vocational Education institutions compared to Liberal Arts.")

with col3:
    st.link_button("China", "http://localhost:8501/pagechina")
    st.write("Mainland China has a variety of curriculum types that share the majority of subjects. There are various international and state-run programs that have different requirements for job entry.")

with col4:
    st.link_button("SAR and Misc", "http://localhost:8501/pagemisc")
    st.write("Special autonomous regions and other areas around the world have varying educational systems, but one major area they share are IB schools and/or international education programs, which have requirements related to higher education.")

st.image("Screen Shot 2025-04-24 at 10.42.51 AM.png")

