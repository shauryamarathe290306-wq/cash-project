import streamlit as st

from utils.css_loader import load_css
from utils.api import get_exchange_rates
from utils.converter import convert_currency

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="CurrencyVerse",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Load CSS
# --------------------------------------------------

load_css()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🌍 CurrencyVerse")

st.sidebar.markdown("---")

st.sidebar.info(
    """
### 🚀 Features

✔ Live Currency Converter

✔ Professional UI

✔ Country Explorer *(Coming Soon)*

✔ Weather *(Coming Soon)*

✔ Food *(Coming Soon)*

✔ Tourist Places *(Coming Soon)*

✔ Personalities *(Coming Soon)*
"""
)

st.sidebar.markdown("---")

st.sidebar.success("Phase 1 Development")

# --------------------------------------------------
# Hero Section
# --------------------------------------------------

st.markdown(
    """
<h1 class="hero-title">🌍 CurrencyVerse</h1>

<p class="hero-subtitle">
Explore the World Through Currency
</p>
""",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# Currency List
# --------------------------------------------------

currencies = [
    "USD", "EUR", "GBP", "INR", "JPY",
    "AUD", "CAD", "CHF", "CNY", "SGD",
    "NZD", "AED", "SAR", "ZAR", "RUB"
]

# --------------------------------------------------
# Currency Converter Card
# --------------------------------------------------

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.subheader("💱 Live Currency Converter")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input(
        "Enter Amount",
        min_value=0.0,
        value=1.0,
        step=1.0
    )

    from_currency = st.selectbox(
        "From Currency",
        currencies,
        index=0
    )

with col2:
    to_currency = st.selectbox(
        "To Currency",
        currencies,
        index=3
    )

    swap = st.button("🔄 Swap")

# -----------------------------
# Swap Logic
# -----------------------------

if swap:
    from_currency, to_currency = to_currency, from_currency

# -----------------------------
# Convert Button
# -----------------------------

convert = st.button("🚀 Convert Currency")

st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# Live Currency Conversion
# --------------------------------------------------

if convert:

    if from_currency == to_currency:
        st.warning("⚠️ Please select two different currencies.")

    else:

        with st.spinner("Fetching live exchange rates..."):

            rates = get_exchange_rates(from_currency)

            if rates is None:
                st.error("❌ Unable to fetch exchange rates.")

            else:

                converted_amount = convert_currency(
                    amount,
                    rates,
                    to_currency
                )

                if converted_amount is None:
                    st.error("❌ Conversion failed.")

                else:

                    st.success("✅ Conversion Successful")

                    st.markdown("---")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            "Source Amount",
                            f"{amount:.2f} {from_currency}"
                        )

                    with col2:
                        st.metric(
                            "Converted Amount",
                            f"{converted_amount:.2f} {to_currency}"
                        )

                    st.markdown("---")

                    st.info(
                        f"💹 Live Exchange Rate\n\n"
                        f"1 {from_currency} = {rates[to_currency]:.4f} {to_currency}"
                    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.markdown(
    """
<div style="text-align:center; padding:20px;">

### 🌍 CurrencyVerse

Made with ❤️ using Streamlit

**Version 1.0 | Phase 1**

More exciting features are coming soon...

</div>
""",
    unsafe_allow_html=True
)