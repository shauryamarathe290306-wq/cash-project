import streamlit as st

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="CurrencyVerse",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:
    st.title("🌍 CurrencyVerse")
    st.markdown("---")

    st.subheader("🚀 Features")

    st.markdown("""
- 💱 Live Currency Converter
- 🌍 Country Explorer
- 🏳️ Country Flags
- 🌦️ Live Weather
- 🕒 Local Time
- 🍛 Traditional Food
- 🎉 Festivals
- 🏛️ Tourist Attractions
- 👑 Great Personalities
- 📈 Exchange Rate History
- ❤️ Favorites
""")

    st.markdown("---")
    st.success("Version 1.0")

# -------------------------------------------------
# Main Title
# -------------------------------------------------

st.title("🌍 CurrencyVerse")
st.subheader("Explore the World Through Currency & Culture")

st.markdown("---")

st.markdown("""
Welcome to **CurrencyVerse**!

CurrencyVerse is a modern currency conversion application that goes beyond simple exchange rates.

Along with live currency conversion, you'll be able to explore:

- 💱 Real-time Currency Conversion
- 🌍 Country Information
- 🏳️ National Flags
- 🌦️ Live Weather
- 🕒 Local Time
- 🍛 Traditional Food
- 🎉 Festivals
- 🏛️ Famous Tourist Attractions
- 👑 Great Personalities
- 📈 Exchange Rate History
- ❤️ Favorite Countries

This project is being developed step by step using **Python** and **Streamlit**.
""")

st.markdown("---")

# -------------------------------------------------
# Upcoming Features
# -------------------------------------------------

st.header("🚀 Upcoming Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("💱 Live Currency Converter")

with col2:
    st.info("🏳️ Country Flags")

with col3:
    st.info("🌍 Country Explorer")

col4, col5, col6 = st.columns(3)

with col4:
    st.info("🌦️ Live Weather")

with col5:
    st.info("🍛 Traditional Food")

with col6:
    st.info("🏛️ Tourist Attractions")

col7, col8, col9 = st.columns(3)

with col7:
    st.info("👑 Great Personalities")

with col8:
    st.info("📈 Exchange Rate History")

with col9:
    st.info("❤️ Favorites")

st.markdown("---")

st.success("✅ CurrencyVerse project setup completed successfully!")

st.caption("Built with ❤️ using Python & Streamlit")