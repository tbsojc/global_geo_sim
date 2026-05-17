from dataclasses import dataclass, field
from typing import Dict, List

from src.geosim.core.country import Country
from src.geosim.core.province import Province


@dataclass
class World:
    year: int
    month: int

    countries: Dict[str, Country]
    provinces: Dict[int, Province]
    trade_good_prices: dict[str, float] = field(default_factory=dict)

    global_growth: float = 1.8
    global_tension: float = 20.0

    event_log: List[str] = field(default_factory=list)

    def date_label(self) -> str:
        return f"{self.month:02d}/{self.year}"

    def advance_month(self) -> None:
        self.month += 1

        if self.month > 12:
            self.month = 1
            self.year += 1

    def log_event(self, text: str) -> None:
        self.event_log.append(
            f"[{self.date_label()}] {text}"
        )

    def provinces_of(self, country_tag: str):
        return [
            province
            for province in self.provinces.values()
            if province.owner == country_tag
        ]
