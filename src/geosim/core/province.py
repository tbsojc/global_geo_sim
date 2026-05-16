from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Province:
    id: int
    key: str
    name: str

    owner: str
    controller: str

    cores: List[str] = field(default_factory=list)

    region: str = "unknown"
    continent: str = "unknown"

    population_m: float = 0.0
    urbanization: float = 0.0
    gdp_b: float = 0.0

    culture: str = "unknown"
    religion: str = "secular"
    ideology: str = "neutral"

    terrain: str = "plains"
    climate: str = "temperate"

    is_coastal: bool = False
    has_port: bool = False

    infrastructure: float = 50.0
    industry: float = 0.0
    development: float = 0.0

    trade_node: Optional[str] = None
    trade_power: float = 0.0

    resource: Optional[str] = None
    resource_output: float = 0.0

    unrest: float = 0.0
    autonomy: float = 0.0

    buildings: List[str] = field(default_factory=list)
    modifiers: Dict[str, float] = field(default_factory=dict)

    neighbors: List[int] = field(default_factory=list)

    def clamp(self) -> None:
        self.population_m = max(0.0, self.population_m)

        self.urbanization = max(
            0,
            min(100, self.urbanization)
        )

        self.infrastructure = max(
            0,
            min(100, self.infrastructure)
        )

        self.industry = max(
            0,
            min(100, self.industry)
        )

        self.development = max(
            0,
            min(100, self.development)
        )

        self.unrest = max(
            0,
            min(100, self.unrest)
        )

        self.autonomy = max(
            0,
            min(100, self.autonomy)
        )
