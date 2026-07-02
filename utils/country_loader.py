import json
from pathlib import Path


def load_countries():
    """
    Load all country data from countries.json.
    """

    data_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "countries.json"
    )

    try:
        with open(data_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        return {}