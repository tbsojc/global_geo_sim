def update_politics(world) -> None:
    for country in world.countries.values():
        stability_change = 0.0

        stability_change -= max(0, country.inflation - 5) * 0.08
        stability_change -= max(0, country.unemployment - 7) * 0.06

        if country.government == "democracy":
            stability_change += 0.03
            stability_change -= max(0, country.inflation - 10) * 0.04

        elif country.government == "authoritarian":
            stability_change += 0.01
            stability_change -= max(0, country.unemployment - 12) * 0.04

        elif country.government == "hybrid":
            stability_change -= 0.01

        country.stability += stability_change
        country.clamp()
