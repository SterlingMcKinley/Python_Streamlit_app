from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_engineer.json"


# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Function to apply snowfall effect
def run_laptop_animation():
    rain(emoji="💻", font_size=20, falling_speed=5, animation_length="infinite")

# Page configuration
st.set_page_config(page_title="SITE RELIABILITY ENGINEER", page_icon="🐧💻")

# Run laptop animation
run_laptop_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display header with personalized name
st.markdown("<h1 style='text-align: center; color: White;'>Sterling M.</h1>", unsafe_allow_html=True)
st.header('Platform Engineer / Site Reliability Engineer', anchor=False)

# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="Programmer orange", height=300)

# Personalized message
st.markdown(
"""
Technologies & Methodologies that I will focus on this year :
- Python
- AWS Solutions Architect Associcate
- Certified Kubernetes Administrator
- SRE fundamentals
- Artificial Intelligence
"""
)

# Personalized message
st.markdown(
    f"Wishing you a SUCCESSFUL 2024!"
)

