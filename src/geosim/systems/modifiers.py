from src.geosim.core.country import CountryModifiers
from src.geosim.systems.sliders import apply_slider_modifiers


COUNTRY_MODIFIER_DEFINITIONS = {
    "global_reserve_currency": CountryModifiers(
        trade_efficiency=1.10,
        diplomacy_efficiency=1.05,
        inflation_modifier=-0.01,
    ),

    "advanced_research_sector": CountryModifiers(
        research_efficiency=1.15,
        production_efficiency=1.03,
    ),

    "polarized_society": CountryModifiers(
        stability_modifier=-0.03,
        unrest_modifier=0.05,
    ),

    "export_powerhouse": CountryModifiers(
        trade_efficiency=1.12,
        production_efficiency=1.05,
    ),

    "state_directed_industry": CountryModifiers(
        production_efficiency=1.08,
        administration_efficiency=1.05,
        research_efficiency=0.97,
    ),
}


def reset_country_modifiers(country) -> None:
    country.final_modifiers = CountryModifiers()
    country.final_modifiers.add(country.base_modifiers)


def apply_active_modifiers(country) -> None:
    for modifier_name in country.active_modifiers:
        modifier = COUNTRY_MODIFIER_DEFINITIONS.get(modifier_name)

        if modifier is None:
            continue

        country.final_modifiers.add(modifier)

def update_country_modifiers(world) -> None:
    for country in world.countries.values():
        reset_country_modifiers(country)
        apply_active_modifiers(country)

        slider_modifiers = apply_slider_modifiers(country)
        country.final_modifiers.add(slider_modifiers)
