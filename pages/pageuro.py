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

_EU_INTRO = """
There’s an old saying that goes, “Americans live to work, Europeans work to live.” While this is an exaggeration, the difference in mentality surrounding work is stark. There is a general strong focus in the U.S. on productivity and hustle culture.

Yet, despite the intensity of work in the U.S., Americans tend to be far friendlier in the workspace than their European counterparts—but not in the way you think. Americans frequently adopt a positive feedback mindset, opting for frequent praise. Europeans are less likely to give out praise. As the European Business Review puts it, “This doesn’t mean that Europe is hostile. Rather, they are simply less prone to excessive geniality.”

European mentality and self-image are also less focused on what someone does. While in conversation in the U.S., what someone does is often used to define that person, while European countries tend to view someone’s job as simply that: a job. This mindset is an easy way to grasp the European relationship to work. While Americans heavily identify themselves with their career and productivity, Europeans simply don’t.

American companies are frequently adjusting to better match our European counterparts, and there is hope that the country’s relationship to work will eventually be settled. Gen Z and Millennials have a very different view than their parents when it comes to work, and this is largely due to the awareness of European working culture.

European work culture is often viewed as a utopia to burnt-out American workers, and can be an excellent place to intern in order to travel and gain experience simultaneously. (https://absoluteinternship.com/blog/working-culture-usa-vs-europe/)
"""
def stream_data():
    for word in _EU_INTRO.split(" "):
        yield word + " "
        time.sleep(0.02)
if st.button("What does working in Europe look like?"):
    st.write_stream(stream_data)

st.image("Screen Shot 2025-05-22 at 10.09.46 AM.png")
