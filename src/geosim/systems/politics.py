def update_politics(world) -> None:
    for country in world.countries.values():
        mods = country.final_modifiers

        stability_change = 0.0

        stability_change -= max(
            0,
            country.economy.inflation - 5
        ) * 0.08

        stability_change -= max(
            0,
            country.economy.unemployment - 7
        ) * 0.06

        if country.government == "democracy":
            stability_change += 0.03
            stability_change -= max(
                0,
                country.economy.inflation - 10
            ) * 0.04

        elif country.government == "authoritarian":
            stability_change += 0.01
            stability_change -= max(
                0,
                country.economy.unemployment - 12
            ) * 0.04

        elif country.government == "hybrid":
            stability_change -= 0.01

        stability_change += mods.stability_modifier

        country.state.stability += stability_change
        country.state.unrest += mods.unrest_modifier

        country.clamp()
