import streamlit as st

def load_css(css_path="assets/css/style.css"):
    """
    Load custom CSS into the Streamlit application.
    """
    try:
        with open(css_path, "r", encoding="utf-8") as css_file:
            st.markdown(
                f"<style>{css_file.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.error(f"CSS file not found: {css_path}")