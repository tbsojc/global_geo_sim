from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Country:
    tag: str
    name: str

    government: str

    base_stability: float
    inflation: float
    unemployment: float

    base_tech_level: float
    military_power: float

    province_ids: List[int] = field(default_factory=list)
    relations: Dict[str, float] = field(default_factory=dict)

    # Werden aus Provinzen berechnet
    population_m: float = 0.0
    gdp_b: float = 0.0
    infrastructure: float = 0.0
    industry: float = 0.0
    development: float = 0.0
    tech_level: float = 0.0
    stability: float = 0.0
    energy_dependence: float = 0.0

    def clamp(self) -> None:
        self.base_stability = max(0, min(100, self.base_stability))
        self.stability = max(0, min(100, self.stability))

        self.inflation = max(-5, min(50, self.inflation))
        self.unemployment = max(0, min(40, self.unemployment))

        self.base_tech_level = max(0, min(100, self.base_tech_level))
        self.tech_level = max(0, min(100, self.tech_level))

        self.infrastructure = max(0, min(100, self.infrastructure))
        self.industry = max(0, min(100, self.industry))
        self.development = max(0, min(100, self.development))

        self.military_power = max(0, self.military_power)
        self.energy_dependence = max(0, min(1, self.energy_dependence))

        self.gdp_b = max(0, self.gdp_b)
        self.population_m = max(0, self.population_m)

    def power_score(self) -> float:
        return (
            self.gdp_b * 0.4
            + self.population_m * 5
            + self.tech_level * 20
            + self.military_power * 25
            + self.stability * 8
        ) / 100
