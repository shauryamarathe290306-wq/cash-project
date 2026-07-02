"""
CurrencyVerse - API Module

This module handles all communication with the ExchangeRate API.
"""

import requests

# Free ExchangeRate API
BASE_URL = "https://open.er-api.com/v6/latest"


def get_exchange_rates(base_currency: str):
    """
    Fetch live exchange rates for the selected base currency.

    Parameters:
        base_currency (str): Currency code (e.g., USD, INR)

    Returns:
        dict: Dictionary of exchange rates
        None: If API request fails
    """

    try:
        response = requests.get(
            f"{BASE_URL}/{base_currency}",
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if data.get("result") == "success":
            return data["rates"]

        return None

    except requests.exceptions.RequestException:
        return None