import streamlit as st
st. set_page_config(layout="wide")

# Inject custom CSS to adjust sidebar width
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            min-width: 250px;
            max-width: 250px;
        }
    </style>
""", unsafe_allow_html=True)

# Create navigation links
nav_links = {
    "Home/This Project 😘": "https://yogii006.streamlit.app/",
    "IPL win prediction 😅": "https://yogii006ipl.streamlit.app/",
    "LOAN approval prediction 🙄": "https://yogii006loan.streamlit.app/",
    "Heart disease prediction 😅": "https://yogii006heart-disease.streamlit.app/",
    "IPL win prediction 🖥️": "https://yogii006.streamlit.app/",
    "IPL win prediction 😘": "https://yogii006.streamlit.app/"
}

# Display navigation links in the sidebar
st.sidebar.title('Navigation')
for label, url in nav_links.items():
    st.sidebar.markdown(f'<a href="{url}" target="_self">{label}</a>', unsafe_allow_html=True)

st.header("Projects by Yogesh Yadav on Machine learning")
col1, col2,col3 = st.columns(3)
image_width = 350  # Set the width you want
with col1:
    st.markdown("### [IPL win prediction](https://yogii006ipl.streamlit.app/)")
    st.image("ipl.jpg", use_column_width=False, width=image_width)
    st.markdown("### [Github code](https://github.com/yogii006/ipl)")
with col2:
    st.markdown("### [Loan win prediction](https://yogii006loan.streamlit.app/)")
    st.image("bank.jpeg", use_column_width=False, width=image_width)
    st.markdown("### [Github code](https://github.com/yogii006/loan)")
with col3:
    st.markdown("### [Heart disease prediction](https://yogii006heart-disease.streamlit.app/)")
    st.image("heart.png", use_column_width=False, width=image_width)
    st.markdown("### [Github code](https://github.com/yogii006/heart-disease)")
# st.title("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
st.title("--------------------------------------------------------")
col4, col5,col6 = st.columns(3)
with col4:
   st.markdown("### [Loan approval prediction](https://yogii006loan.streamlit.app/)")
   st.image("bank.jpeg", use_column_width=False, width=image_width)
   st.markdown("### [Github code](https://github.com/yogii006/loan)")
with col5:
   st.markdown("### [Link For this project](https://github.com/yogii006/projects)")
   st.image("project.jpeg", use_column_width=False, width=image_width)
   st.markdown("### [Github code](https://github.com/yogii006/projects)")
with col6:
    st.markdown("### [Heart disease prediction](https://yogii006heart-disease.streamlit.app/)")
    st.image("heart.png", use_column_width=False, width=image_width)
    st.markdown("### [Github code](https://github.com/yogii006/heart-disease)")
