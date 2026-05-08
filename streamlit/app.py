import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("🛡️ AutoCyberSec News – Weekly Review")
st.caption("Utorok / Štvrtok • Vyber top články (max 8–10)")

# Načíta články s impact > 6 z posledných 7 dní
# Checkboxy + tlačidlo "Generovať LinkedIn posty a zaradiť do queue"
