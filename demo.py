import streamlit as st
st.set_page_config(page_title='cats')
st.header("Types of cats")

col1,col2=st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.image("./cat1.jpeg")
  st.write("Persian Cats are cute")
with col2:
  st.subheader("Ragdoll Cat")
  st.image("./cat2.jpeg",width=500)
  st.write("Ragdoll Cats are proud")

