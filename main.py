import streamlit as st
st.header("Projects by Yogesh Yadav on Machine learning")
col1, col2,col5 = st.columns(3)
image_width = 250  # Set the width you want
with col1:
    st.image("bank.jpeg", use_column_width=False, width=image_width)
    st.markdown("### [IPL win prediction](https://yogii006ipl.streamlit.app/)")
    st.markdown("### [Github code](https://github.com/yogii006/ipl)")
with col2:
    st.image("bank.jpeg", use_column_width=False, width=image_width)
    st.markdown("### [Heart disease prediction](https://yogii006heart-disease.streamlit.app/)")
    st.markdown("### [Github code](https://github.com/yogii006/heart-disease)")
with col5:
    st.image("ipl.jpg", use_column_width=False, width=image_width)
    st.markdown("### [IPL win prediction](https://yogii006ipl.streamlit.app/)")
    st.markdown("### [Github code](https://github.com/yogii006/ipl)")

col3, col4,col6 = st.columns(3)
with col3:
   st.image("bank.jpeg", use_column_width=False, width=image_width)
   st.markdown("### [Loan approval prediction](https://yogii006loan.streamlit.app/)")
   st.markdown("### [Github code](https://github.com/yogii006/loan)")
with col4:
   st.image("project.jpeg", use_column_width=False, width=image_width)
   st.markdown("### [Github code For this project](https://github.com/yogii006/projects)")
with col6:
    st.image("heart.png", use_column_width=False, width=image_width)
    st.markdown("### [Heart disease prediction](https://yogii006heart-disease.streamlit.app/)")
    st.markdown("### [Github code](https://github.com/yogii006/heart-disease)")
