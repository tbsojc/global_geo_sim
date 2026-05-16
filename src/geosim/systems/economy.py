def update_economy(world) -> None:
    for country in world.countries.values():
        country.inflation += country.energy_dependence * 0.02
        country.inflation += max(0, world.global_tension - 40) / 250

        country.clamp()
