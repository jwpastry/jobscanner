import streamlit as st
st.title("Opportunities of Vocational Training in the EU")
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
st.markdown('<h4 class="fade-in">Vocational education and training (VET) in Europe offers individuals a practical pathway to gain skills and qualifications for specific trades or careers. While requirements can vary slightly between countries, there are some general conditions that apply across most European nations. Typically, individuals need to have completed lower secondary education (around age 15 or 16) to enter a vocational program. Some programs may also require basic language proficiency, especially for non-native speakers. Additionally, depending on the field, certain health checks or aptitude tests might be needed. Overall, vocational training in Europe is designed to be accessible, combining classroom learning with hands-on work experience to prepare students for the job market. (Chatgpt.com, 2025)</h1>', unsafe_allow_html=True)

st.link_button("See more here:", "https://education.ec.europa.eu/education-levels/vocational-education-and-training")