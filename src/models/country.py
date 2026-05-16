from dataclasses import dataclass
from typing import Dict, List


@dataclass
class CountryState:
    stability: float
    legitimacy: float
    administrative_capacity: float
    corruption: float
    war_support: float
    social_cohesion: float
    unrest: float


@dataclass
class Economy:
    inflation: float
    unemployment: float


@dataclass
class Technology:
    tech_level: float


@dataclass
class Military:
    military_power: float


@dataclass
class Country:
    tag: str
    name: str
    government: str
    state: CountryState
    economy: Economy
    technology: Technology
    military: Military
    province_ids: List[int]
    relations: Dict[str, int]

    @staticmethod
    def from_dict(data: dict) -> "Country":
        return Country(
            tag=data["tag"],
            name=data["name"],
            government=data["government"],
            state=CountryState(**data["state"]),
            economy=Economy(**data["economy"]),
            technology=Technology(**data["technology"]),
            military=Military(**data["military"]),
            province_ids=data["province_ids"],
            relations=data.get("relations", {}),
        )
