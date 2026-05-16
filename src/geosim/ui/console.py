def print_world_summary(world) -> None:
    print(f"\n===== {world.date_label()} =====")
    print(f"Global Tension: {world.global_tension:.2f}")
    print("-" * 82)

    print(
        f"{'State':<15} "
        f"{'GDP':>10} "
        f"{'Stab':>7} "
        f"{'Infl':>7} "
        f"{'Unemp':>7} "
        f"{'Mil':>7} "
        f"{'Power':>8} "
        f"{'Prov':>5}"
    )

    print("-" * 82)

    for country in sorted(
        world.countries.values(),
        key=lambda c: c.power_score(),
        reverse=True
    ):
        provinces = world.provinces_of(country.tag)

        print(
            f"{country.name:<15} "
            f"{country.gdp_b:>10.0f} "
            f"{country.stability:>7.1f} "
            f"{country.inflation:>7.1f} "
            f"{country.unemployment:>7.1f} "
            f"{country.military_power:>7.1f} "
            f"{country.power_score():>8.1f} "
            f"{len(provinces):>5}"
        )


def print_province_summary(world) -> None:
    print("\nProvinces:")
    print("-" * 100)

    print(
        f"{'Province':<18} "
        f"{'Owner':<6} "
        f"{'Pop':>7} "
        f"{'GDP':>8} "
        f"{'Infra':>7} "
        f"{'Ind':>7} "
        f"{'Dev':>7} "
        f"{'Unrest':>8} "
        f"{'Res':<15} "
        f"{'Out':>7}"
    )

    print("-" * 100)

    for province in sorted(
        world.provinces.values(),
        key=lambda p: (p.owner, p.name)
    ):
        print(
            f"{province.name:<18} "
            f"{province.owner:<6} "
            f"{province.population_m:>7.1f} "
            f"{province.gdp_b:>8.0f} "
            f"{province.infrastructure:>7.1f} "
            f"{province.industry:>7.1f} "
            f"{province.development:>7.1f} "
            f"{province.unrest:>8.1f} "
            f"{str(province.resource):<15} "
            f"{province.resource_output:>7.1f}"
        )


def print_country_provinces(world, country_tag: str) -> None:
    country = world.countries.get(country_tag)

    if country is None:
        print(f"\nUnknown country: {country_tag}")
        return

    provinces = world.provinces_of(country_tag)

    print(f"\nProvinces of {country.name}:")
    print("-" * 100)

    for province in sorted(provinces, key=lambda p: p.name):
        print(
            f"{province.name:<18} | "
            f"Pop: {province.population_m:>6.1f} | "
            f"Infra: {province.infrastructure:>5.1f} | "
            f"Industry: {province.industry:>5.1f} | "
            f"Dev: {province.development:>5.1f} | "
            f"Unrest: {province.unrest:>5.1f} | "
            f"Resource: {province.resource}"
        )


def print_recent_events(world, limit: int = 8) -> None:
    if not world.event_log:
        return

    print("\nEvents:")
    for entry in world.event_log[-limit:]:
        print(f" - {entry}")
