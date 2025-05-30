import streamlit as st
st.title("Opportunities of Vocational Training in the US")

st.markdown(''':blue-background[There are existing sources that offer better expertise and research, so I will directly link you there.]''')
hover_box = """
<style>
.hover-box {
    position: relative;
    display: inline-block;
    width: 800px;
    height: 150px;
    background-color: #f0f0f0;
    border-radius: 8px;
    padding: 10px;
    text-align: center;
    transition: box-shadow 0.3s ease;
}

.hover-box:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.hover-content {
    display: none;
    position: absolute;
    bottom: 10px;
    left: 10px;
    right: 10px;
}

.hover-box:hover .hover-content {
    display: block;
}

}
</style>

<div class="hover-box">
    <p>The vocational training sector plays a critical role in equipping individuals
             with the practical skills and knowledge needed to succeed in specific trades 
             or occupations. Vocational training is an extra part to preparation for different jobs, 
             preparing learners to enter the workforce directly 
             with area specific training. This sector supports a large range of
             industries and is widely seen around the world.</p>
    <div class="hover-content">
    </div>
</div>
.
<div class="hover-box">
    <p>Vocational training can lead to careers in numerous fields,
              such as healthcare, construction, 
             automotive technology, information technology, hospitality, and 
             manufacturing. For example, individuals may pursue roles such as electricians, 
             plumbers, medical assistants, welders, chefs, or IT support technicians. 
             As industries evolve, vocational education
              continues to adapt, integrating new technologies and methodologies to 
             keep the workforce current and competitive. Working as a teacher in the US requires previous vocational training. (https://chatgpt.com/, 2025)</p>
    <div class="hover-content">
    </div>
</div>

"""

st.markdown(hover_box, unsafe_allow_html=True)

st.link_button("Learn more about it here:", "https://jobs.chronicle.com/jobs/vocational-and-technical-fields/united-states/")