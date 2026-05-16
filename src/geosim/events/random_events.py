import random


def random_event_chance(chance_percent: float) -> bool:
    return random.random() < (chance_percent / 100)


def trigger_random_events(world) -> None:

    for country in world.countries.values():

        # =====================================================
        # Wirtschaftsboom
        # =====================================================

        if random_event_chance(2):

            growth = random.uniform(0.5, 2.0)

            country.gdp_b *= (1 + growth / 100)

            world.log_event(
                f"Economic boom in {country.name} "
                f"(+{growth:.2f}% GDP)"
            )

        # =====================================================
        # Energiekrise
        # =====================================================

        if random_event_chance(1.5):

            inflation = random.uniform(0.5, 2.5)

            country.inflation += inflation
            country.stability -= inflation * 0.4

            world.log_event(
                f"Energy crisis in {country.name} "
                f"(+{inflation:.2f} inflation)"
            )

        # =====================================================
        # Politische Reformen
        # =====================================================

        if random_event_chance(1):

            reform = random.uniform(0.5, 1.5)

            country.stability += reform
            country.tech_level += reform * 0.3

            world.log_event(
                f"Political reforms in {country.name}"
            )

        # =====================================================
        # Proteste
        # =====================================================

        if (
            country.inflation > 8
            and country.stability < 50
            and random_event_chance(5)
        ):

            damage = random.uniform(1.0, 4.0)

            country.stability -= damage

            world.log_event(
                f"Mass protests in {country.name} "
                f"(-{damage:.1f} stability)"
            )

        country.clamp()
