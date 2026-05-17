def weighted_average(items, value_fn, weight_fn) -> float:
    total_weight = sum(weight_fn(item) for item in items)

    if total_weight <= 0:
        return 0.0

    return sum(
        value_fn(item) * weight_fn(item)
        for item in items
    ) / total_weight


def aggregate_country_from_provinces(world, country) -> None:
    provinces = world.provinces_of(country.tag)

    if not provinces:
        return

    mods = country.final_modifiers

    population = sum(p.population_m for p in provinces)

    gdp = sum(
        getattr(p, "gdp_b", 0.0)
        for p in provinces
    )

    avg_infrastructure = weighted_average(
        provinces,
        lambda p: p.infrastructure,
        lambda p: max(p.population_m, 0.1),
    )

    avg_industry = weighted_average(
        provinces,
        lambda p: p.industry,
        lambda p: max(getattr(p, "gdp_b", 0.1), 0.1),
    )

    avg_development = weighted_average(
        provinces,
        lambda p: p.development,
        lambda p: max(p.population_m, 0.1),
    )

    avg_unrest = weighted_average(
        provinces,
        lambda p: p.unrest,
        lambda p: max(p.population_m, 0.1),
    )

    energy_output = sum(
        p.resource_output
        for p in provinces
        if p.resource == "energy"
    )

    economic_size = max(gdp / 1000, 1)

    country.population_m = population
    country.gdp_b = gdp

    country.infrastructure = avg_infrastructure
    country.industry = avg_industry
    country.development = avg_development

    country.technology.tech_level = (
        country.technology.tech_level * 0.85
        + avg_development * 0.15 * mods.research_efficiency
    )

    unrest_pressure = max(0, avg_unrest - 10)
    country.state.stability -= (
        unrest_pressure
        * 0.03
        / mods.administration_efficiency
    )

    country.energy_dependence = max(
        0,
        min(1, 1 - (energy_output / economic_size) / 100)
    )

    country.clamp()


def aggregate_all_countries(world) -> None:
    for country in world.countries.values():
        aggregate_country_from_provinces(world, country)
