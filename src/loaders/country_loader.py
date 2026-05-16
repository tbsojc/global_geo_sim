import json
from pathlib import Path

from src.models.country import Country


def load_country(path: str | Path) -> Country:
    path = Path(path)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return Country.from_dict(data)


def load_countries(folder: str | Path) -> dict[str, Country]:
    folder = Path(folder)
    countries = {}

    for file in folder.glob("*.json"):
        country = load_country(file)
        countries[country.tag] = country

    return countries
