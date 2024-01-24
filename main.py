import streamlit as st
st. set_page_config(layout="wide")
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

col4, col5,col6 = st.columns(3)
with col4:
   st.markdown("### [Loan approval prediction](https://yogii006loan.streamlit.app/)")
   st.image("bank.jpeg", use_column_width=False, width=image_width)
   st.markdown("### [Github code](https://github.com/yogii006/loan)")
with col5:
   st.markdown("### [Link For this project](https://github.com/yogii006/projects)")
   st.image("project.jpeg", use_column_width=False, width=image_width)
   st.markdown("### [Github code For this project](https://github.com/yogii006/projects)")
with col6:
    st.markdown("### [Heart disease prediction](https://yogii006heart-disease.streamlit.app/)")
    st.image("heart.png", use_column_width=False, width=image_width)
    st.markdown("### [Github code](https://github.com/yogii006/heart-disease)")
