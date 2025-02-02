import streamlit as st
from hololive import holo

st.write("Welcome to TuberDex!\nAs development continues I hope to add more Indie and other corporation related VTubers, though for now, we have all of HoloLive!\nBy the time this project comes to fruition, this can hopefully help you find your next oshi. :)")

for key, item in holo.items():
  for i in item:
    st.write(f"Hololive {key}'s {i}")
