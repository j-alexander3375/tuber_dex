import streamlit as st
import pandas as pd
from hololive import holo

st.markdown("# Welcome to TuberDex!")
st.markdown("## As development continues I hope to add more Indie and other corporation related VTubers, though for now, we have all of HoloLive!")
st.markdown("## By the time this project comes to fruition, this can hopefully help you find your next oshi. :)")
st.write("")

# for key, item in holo.items():
#  for i in item:
#    st.write(f"Hololive {key}'s {i}")

st.table(holo)
