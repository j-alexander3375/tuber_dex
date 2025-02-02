import streamlit as st
from hololive import holo

for key, item in holo:
  for i in item:
    st.write(f"Hololive {key}'s {i}")
