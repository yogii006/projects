import streamlit as st
st.header("Projects by Yogesh Yadav on Machine learning")
col1, col2, col3= st.columns(3)
image_width = 200  # Set the width you want
with col1:
    st.image("ipl.webp", use_column_width=False, width=image_width)
    st.markdown("### [IPL win prediction](https://yogii006ipl.streamlit.app/)")
with col2:
    st.image("heart.png", use_column_width=False, width=image_width)
    st.markdown("### [Heart disease prediction](https://yogii006heart-disease.streamlit.app/)")
with col3:
   st.image("bank.jpeg", use_column_width=False, width=image_width)
   st.markdown("### [Loan approval prediction](https://yogii006loan.streamlit.app/)")
