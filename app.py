import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CurrencyVerse",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load Custom CSS
# -----------------------------
def load_css():
    with open("assets/css/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -----------------------------
# Hero Section
# -----------------------------
st.markdown(
    """
    <h1 class="hero-title">🌍 CurrencyVerse</h1>
    <p class="hero-subtitle">
        Explore the world through currencies, culture and countries.
    </p>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Welcome Card
# -----------------------------
st.markdown(
    """
    <div class="glass-card">
        <h2>💱 Live Currency Converter</h2>
        <p>
            Welcome to <b>CurrencyVerse</b>.
            This application will help you convert currencies in real time while
            exploring countries, weather, food, famous personalities, tourist
            attractions and much more.
        </p>
        <p><b>🚀 Live converter coming in the next step.</b></p>
    </div>
    """,
    unsafe_allow_html=True
)