from dataclasses import dataclass, field

@dataclass
class CountryModifiers:
    tax_efficiency: float = 1.0
    production_efficiency: float = 1.0
    trade_efficiency: float = 1.0
    research_efficiency: float = 1.0
    administration_efficiency: float = 1.0
    diplomacy_efficiency: float = 1.0
    military_industry_efficiency: float = 1.0
    mobilization_speed: float = 1.0

    stability_modifier: float = 0.0
    unrest_modifier: float = 0.0
    inflation_modifier: float = 0.0
    unemployment_modifier: float = 0.0

    def add(self, other: "CountryModifiers") -> None:
        self.tax_efficiency += other.tax_efficiency - 1.0
        self.production_efficiency += other.production_efficiency - 1.0
        self.trade_efficiency += other.trade_efficiency - 1.0
        self.research_efficiency += other.research_efficiency - 1.0
        self.administration_efficiency += other.administration_efficiency - 1.0
        self.diplomacy_efficiency += other.diplomacy_efficiency - 1.0
        self.military_industry_efficiency += other.military_industry_efficiency - 1.0
        self.mobilization_speed += other.mobilization_speed - 1.0

        self.stability_modifier += other.stability_modifier
        self.unrest_modifier += other.unrest_modifier
        self.inflation_modifier += other.inflation_modifier
        self.unemployment_modifier += other.unemployment_modifier

@dataclass
class CountrySliders:
    democracy_authoritarian: int = 0
    liberty_control: int = 0
    globalism_nationalism: int = 0
    traditional_progressive: int = 0
    centralization_decentralization: int = 0
    production_trade: int = 0
    free_market_planned: int = 0
    hawk_dove: int = 0
    interventionism_isolationism: int = 0

    def clamp(self) -> None:
        self.democracy_authoritarian = max(-5, min(5, self.democracy_authoritarian))
        self.liberty_control = max(-5, min(5, self.liberty_control))
        self.globalism_nationalism = max(-5, min(5, self.globalism_nationalism))
        self.traditional_progressive = max(-5, min(5, self.traditional_progressive))
        self.centralization_decentralization = max(-5, min(5, self.centralization_decentralization))
        self.production_trade = max(-5, min(5, self.production_trade))
        self.free_market_planned = max(-5, min(5, self.free_market_planned))
        self.hawk_dove = max(-5, min(5, self.hawk_dove))
        self.interventionism_isolationism = max(-5, min(5, self.interventionism_isolationism))

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
class CountryEconomy:
    inflation: float
    unemployment: float


@dataclass
class CountryTechnology:
    tech_level: float


@dataclass
class CountryMilitary:
    military_power: float


@dataclass
class Country:
    tag: str
    name: str
    government: str

    state: CountryState
    economy: CountryEconomy
    technology: CountryTechnology
    military: CountryMilitary

    province_ids: list[int] = field(default_factory=list)
    relations: dict[str, float] = field(default_factory=dict)

    base_modifiers: CountryModifiers = field(default_factory=CountryModifiers)
    final_modifiers: CountryModifiers = field(default_factory=CountryModifiers)
    active_modifiers: list[str] = field(default_factory=list)
    sliders: CountrySliders = field(default_factory=CountrySliders)

    population_m: float = 0.0
    gdp_b: float = 0.0
    infrastructure: float = 0.0
    industry: float = 0.0
    development: float = 0.0
    energy_dependence: float = 0.0

    @classmethod
    def from_dict(cls, data: dict) -> "Country":
        return cls(
            tag=data["tag"],
            name=data["name"],
            government=data.get("government", "unknown"),
            state=CountryState(**data["state"]),
            economy=CountryEconomy(**data["economy"]),
            technology=CountryTechnology(**data["technology"]),
            military=CountryMilitary(**data["military"]),
            province_ids=data.get("province_ids", []),
            relations=data.get("relations", {}),
            base_modifiers=CountryModifiers(**data.get("base_modifiers", {})),
            final_modifiers=CountryModifiers(),
            active_modifiers=data.get("active_modifiers", []),
            sliders=CountrySliders(**data.get("sliders", {})),
        )

    def clamp(self) -> None:
        self.state.stability = max(0, min(100, self.state.stability))
        self.state.legitimacy = max(0, min(100, self.state.legitimacy))
        self.state.administrative_capacity = max(0, min(100, self.state.administrative_capacity))
        self.state.corruption = max(0, min(100, self.state.corruption))
        self.state.war_support = max(0, min(100, self.state.war_support))
        self.state.social_cohesion = max(0, min(100, self.state.social_cohesion))
        self.state.unrest = max(0, min(100, self.state.unrest))
        self.sliders.clamp()

        self.economy.inflation = max(-5, min(50, self.economy.inflation))
        self.economy.unemployment = max(0, min(40, self.economy.unemployment))

        self.technology.tech_level = max(0, min(100, self.technology.tech_level))
        self.military.military_power = max(0, self.military.military_power)

        self.infrastructure = max(0, min(100, self.infrastructure))
        self.industry = max(0, min(100, self.industry))
        self.development = max(0, min(100, self.development))
        self.energy_dependence = max(0, min(1, self.energy_dependence))
        self.gdp_b = max(0, self.gdp_b)
        self.population_m = max(0, self.population_m)

    def power_score(self) -> float:
        return (
            self.gdp_b * 0.4
            + self.population_m * 5
            + self.technology.tech_level * 20
            + self.military.military_power * 25
            + self.state.stability * 8
        ) / 100
