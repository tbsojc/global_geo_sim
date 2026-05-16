def change_relation(country, target_tag: str, amount: float) -> None:
    current = country.relations.get(target_tag, 0)
    country.relations[target_tag] = max(-100, min(100, current + amount))


def update_diplomacy(world) -> None:
    for country in world.countries.values():
        for target_tag, relation in country.relations.items():
            if relation < -50:
                world.global_tension += 0.02

            if relation > 50:
                world.global_tension -= 0.01

            if world.global_tension > 60 and relation < -40:
                change_relation(country, target_tag, -0.03)

    world.global_tension = max(0, min(100, world.global_tension))
