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

_US_INTRO = """
The work culture in the United States has a rich historical background that has shaped its unique characteristics. Influenced by various factors, the evolution of work culture in the US has been significant in shaping its current form.

During the early colonial era, the Protestant work ethic played a vital role in establishing the foundation of the American work culture. This ethic emphasized the values of hard work, self-reliance, and personal responsibility. The 19th century, on the other hand, brought industrialization and urbanization, which introduced new dynamics to the American workplace such as an emphasis on efficiency.

In the early 20th century, labor movements gained momentum, leading to the establishment of workers’ rights and labor laws. These developments aimed to ensure fair treatment and better working conditions for employees. As a result, work culture in the US began to recognize the importance of employee rights and the need for a conducive and equitable work environment.

Post-World War II, corporate culture and innovation took center stage in the American business landscape. Management practices focused on fostering innovation, collaboration, and employee engagement to drive business success. This era saw the rise of multinational corporations and the emphasis on teamwork, creativity, and adaptability in the workplace.

In recent decades, technological advancements and globalization have played a significant role in shaping the modern work culture in the US. The rapid development of technology and the interconnectedness of the global economy have introduced new ways of working, such as remote work and virtual collaboration. This has brought about changes in communication, flexibility, and work-life balance, influencing the work culture to adapt to these evolving trends.

Today, the work culture in the US reflects a blend of traditional values and modern practices. Individualism, self-motivation, and a results-oriented mindset are highly valued. Collaboration, diversity, and inclusion have also gained prominence, recognizing the importance of bringing diverse perspectives and experiences together for innovation and success. (https://nnroad.com/blog/work-culture-in-the-us/#:~:text=While%20there%20is%20a%20strong,compared%20to%20some%20other%20countries.)
"""
def stream_data():
    for word in _US_INTRO.split(" "):
        yield word + " "
        time.sleep(0.02)
if st.button("What does working in the US look like?"):
    st.write_stream(stream_data)

st.image("Screen Shot 2025-05-22 at 10.11.22 AM.png")
st.image("Screen Shot 2025-05-28 at 10.50.04 AM.png")