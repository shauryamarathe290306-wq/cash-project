"""
CurrencyVerse - Currency Converter Module

This module performs currency conversion using live exchange rates.
"""


def convert_currency(amount: float, rates: dict, target_currency: str):
    """
    Convert the amount into the target currency.

    Parameters:
        amount (float): Amount entered by the user
        rates (dict): Exchange rates dictionary
        target_currency (str): Currency to convert into

    Returns:
        float | None
    """

    if rates is None:
        return None

    if target_currency not in rates:
        return None

    return amount * rates[target_currency]