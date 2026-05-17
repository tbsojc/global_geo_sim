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
