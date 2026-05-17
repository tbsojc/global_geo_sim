def update_economy(world) -> None:
    for country in world.countries.values():
        mods = country.final_modifiers

        country.economy.inflation += (
            country.energy_dependence * 0.02
            + mods.inflation_modifier
        )

        if country.economy.inflation > 5:
            country.economy.unemployment += (
                0.01
                + mods.unemployment_modifier
            )

        if country.economy.inflation < 2:
            country.economy.unemployment -= (
                0.005
                * mods.production_efficiency
            )

        country.clamp()

def total_income(entity) -> float:
    return (
        getattr(entity, "tax_income", 0.0)
        + getattr(entity, "production_income", 0.0)
        + getattr(entity, "trade_income", 0.0)
    )


def income_per_capita(entity) -> float:
    population = getattr(entity, "population_m", 0.0)

    if population <= 0:
        return 0.0

    return total_income(entity) / population
