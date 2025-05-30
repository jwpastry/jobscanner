import streamlit as st
st.title("Opportunities of LAE and STEM in the EU", )
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
st.markdown('<h3 class="fade-in">Requirements and Background</h1>', unsafe_allow_html=True)
st.markdown('<h4 class="fade-in">Liberal arts education in the European'
            ' Union focuses on developing broad knowledge and critical thinking'
            ' skills across subjects like literature, history, philosophy, languages, '
            'and the social sciences. It encourages creativity, communication,'
            ' and problem-solving—skills that are valuable in many career paths.'
            ' Jobs available in the liberal arts field across the EU include teaching'
            ' and research positions at universities and colleges, roles in cultural'
            ' institutions like museums and libraries, and opportunities in publishing,'
            ' media, public relations, international relations, and non-profit organizations.'
            ' Graduates with a liberal arts background often work as educators, '
            'writers, editors, policy analysts, or cultural project managers.'
            ' As the EU continues to support creativity, diversity, and education,'
            ' the demand for professionals with strong analytical and communication'
            ' skills remains steady across both public and private sectors.'
            ' (Chatgpt.com, 2025)</h1>', unsafe_allow_html=True)
st.link_button("Learn More about Degrees Here", "https://www.educations.com/bachelors-degree/liberal-arts/europe")