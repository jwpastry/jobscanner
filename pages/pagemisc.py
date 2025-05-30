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

_MS_INTRO = """
An example of working in an educational program would be the International Baccalaureate sector, which is a curriculum valid worldwide. 
The International Baccalaureate (IB) program is a globally recognized educational framework designed to challenge students to think critically, work collaboratively, and develop a deep understanding of both local and global issues. It offers a rigorous curriculum that emphasizes academic excellence, intercultural awareness, and personal growth. The IB program is structured to foster independent learning, intellectual curiosity, and a passion for lifelong learning.

Through its three core components—the Extended Essay, Theory of Knowledge (TOK), and Creativity, Activity, Service (CAS)—students are encouraged to engage in research, explore different perspectives, and participate in meaningful community activities. The IB program is known for its holistic approach, preparing students not only for higher education but also for a successful and well-rounded life.

Whether pursuing the IB Diploma in high school or the Middle Years Program (MYP), the IB curriculum allows students to study a broad range of subjects, including languages, sciences, mathematics, and the arts, fostering a balanced academic experience. By completing the IB program, students join a worldwide network of learners committed to making a positive impact on the world around them, which does require higher education to teach. (https://chatgpt.com/)
"""
def stream_data():
    for word in _MS_INTRO.split(" "):
        yield word + " "
        time.sleep(0.02)
if st.button("What does working elsewhere look like?"):
    st.write_stream(stream_data)

st.image("misc.png", "IB Programs and their Availability Globally")