import streamlit as st
st.title("Opportunities of Liberal Arts/STEM in the US")
st.markdown(''':blue-background[There are existing sources that offer better expertise and research, so I will directly link you there.]''')
st.write("This sector is mainly divided into two regions of the US, which these websites have covered:")
hover_box = """
<style>
.hover-box {
    position: relative;
    display: inline-block;
    width: 800px;
    height: 100px;
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

.link-button {
    display: inline-block;
    padding: 6px 12px;
    background-color: #ffffff;
    color: white;
    text-decoration: none;
    border-radius: 4px;
}

.link-button:hover {
    background-color: #007BA7;
}
</style>

<div class="hover-box">
    <p>The Western US</p>
    <div class="hover-content">
        <a href="https://www.indeed.com/q-western-states-jobs.html?vjk=4f7c25e8711e913c" class="link-button" target="_blank">Go to Link</a>
    </div>
</div>

.

<div class="hover-box">
    <p>The Eastern US</p>
    <div class="hover-content">
        <a href="https://www.indeed.com/q-eastern-region-usa-jobs.html" class="link-button" target="_blank">Go to Link</a>
    </div>
</div>
"""

st.markdown(hover_box, unsafe_allow_html=True)
