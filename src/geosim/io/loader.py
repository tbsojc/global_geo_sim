import csv
import json
from pathlib import Path

from src.geosim.core.country import Country
from src.geosim.core.province import Province
from src.geosim.core.world import World


DATA_PATH = Path("data")


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def parse_bool(value: str) -> bool:
    return value.strip().lower() in ["true", "1", "yes", "y"]


def parse_list(value: str, item_type=str) -> list:
    if not value:
        return []

    return [
        item_type(item.strip())
        for item in value.split("|")
        if item.strip()
    ]


def parse_modifiers(value: str) -> dict:
    if not value:
        return {}

    modifiers = {}

    for entry in value.split("|"):
        if not entry.strip():
            continue

        key, raw_value = entry.split(":")
        modifiers[key.strip()] = float(raw_value)

    return modifiers


def load_country(tag: str) -> Country:
    path = DATA_PATH / "countries" / f"{tag.lower()}.json"
    data = load_json(path)
    return Country.from_dict(data)


def load_provinces() -> dict[int, Province]:
    path = DATA_PATH / "provinces" / "provinces.csv"

    provinces = {}

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            province = Province(
                id=int(row["id"]),
                key=row["key"],
                name=row["name"],

                owner=row["owner"],
                controller=row["controller"],
                cores=parse_list(row["cores"]),

                region=row["region"],
                continent=row["continent"],

                population_m=float(row["population_m"]),
                gdp_b=float(row["gdp_b"]),
                urbanization=float(row["urbanization"]),

                culture=row["culture"],
                religion=row["religion"],
                ideology=row["ideology"],

                terrain=row["terrain"],
                climate=row["climate"],
                is_coastal=parse_bool(row["is_coastal"]),
                has_port=parse_bool(row["has_port"]),

                infrastructure=float(row["infrastructure"]),
                industry=float(row["industry"]),
                development=float(row["development"]),

                trade_node=row["trade_node"] or None,
                trade_power=float(row["trade_power"]),

                resource=row["resource"] or None,
                resource_output=float(row["resource_output"]),

                unrest=float(row["unrest"]),
                autonomy=float(row["autonomy"]),

                buildings=parse_list(row["buildings"]),
                modifiers=parse_modifiers(row["modifiers"]),
                neighbors=parse_list(row["neighbors"], int),
            )

            provinces[province.id] = province

    return provinces


def load_events():
    events = []
    events_path = DATA_PATH / "events"

    for file in events_path.glob("*.json"):
        data = load_json(file)
        events.extend(data)

    return events


def load_world(scenario_name: str) -> World:
    scenario_path = DATA_PATH / "scenarios" / f"{scenario_name}.json"
    scenario = load_json(scenario_path)

    countries = {}

    for tag in scenario["countries"]:
        country = load_country(tag)
        countries[country.tag] = country

    all_provinces = load_provinces()

    scenario_province_ids = scenario.get("provinces", [])

    if scenario_province_ids:
        provinces = {
            province_id: all_provinces[province_id]
            for province_id in scenario_province_ids
        }
    else:
        provinces = all_provinces

    return World(
        year=scenario["year"],
        month=scenario["month"],
        countries=countries,
        provinces=provinces,
        global_growth=scenario.get("global_growth", 1.8),
        global_tension=scenario.get("global_tension", 20.0),
    )
