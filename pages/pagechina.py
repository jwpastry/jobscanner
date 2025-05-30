import streamlit as st
import time

st.subheader("Here are the details:",divider = True)

st.markdown("""
    <style>
    .fade-in {
        animation: fadeIn 2s ease-in-out forwards;
        opacity: 0;
    }

    @keyframes fadeIn {
        to {
            opacity: 1;
        }
    }
    </style>
""", unsafe_allow_html=True)
st.markdown('<h1 class="fade-in">Select an area:</h1>', unsafe_allow_html=True)

col1,col2 = st.columns(2)
with col1:
    st.link_button("Vocational Education", "http://localhost:8501/US_VOC")
with col2:
    st.link_button("LAE and STEM", "http://localhost:8501/US_LAE")

_CH_INTRO = """
In particular for China's educational sector for example, here is testimony for how working in that sector feels like from an official briefing: 
China’s education sector is expansive, driven by a large student population and a growing demand for diverse educational services. It is dynamic, witnessing ongoing innovation and adaptation to address evolving educational needs and preferences. China has made notable progress in delivering high-quality education, known for its rigorous standards and competitiveness.

However, with the implementation of policies like the double reduction policy (to reduce the pressures of homework and after-school tutoring), the Chinese education sector is going through a period of adaptation.
Despite challenges, the after-school tutoring market in China is projected to grow, driven by a focus on outcome-based education. (https://www.china-briefing.com/news/chinas-education-sector-latest-trends-and-policies/)
"""
def stream_data():
    for word in _CH_INTRO.split(" "):
        yield word + " "
        time.sleep(0.02)
if st.button("What does working in China look like?"):
    st.write_stream(stream_data)