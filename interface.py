import streamlit as st
from run import Run

st.markdown("<h1 style='text-align: center; color: black;'>AUTOFRIGO</h1>",unsafe_allow_html=True)
for _ in range(2):
    st.title("")
if st.button('Download KPI'):
    Run().run_kpi()
    st.success('Done!')

sn = st.text_input('Serial number')
if len(sn) < 12:
    st.info("Serial number too short")
elif len(sn) > 12:
    st.info("Serial number too long")
else:
    if st.button("Download catalogue"):

            Run().run_frigoshop(sn)
            st.success('Done!')
            #st.error("Try again in few minutes")


