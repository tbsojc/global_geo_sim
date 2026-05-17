def get_country_value(country, field: str):
    field_map = {
        "stability": country.state.stability,
        "legitimacy": country.state.legitimacy,
        "administrative_capacity": country.state.administrative_capacity,
        "corruption": country.state.corruption,
        "war_support": country.state.war_support,
        "social_cohesion": country.state.social_cohesion,
        "unrest": country.state.unrest,

        "inflation": country.economy.inflation,
        "unemployment": country.economy.unemployment,

        "tech_level": country.technology.tech_level,
        "military_power": country.military.military_power,
    }

    if field in field_map:
        return field_map[field]

    return getattr(country, field)


def check_trigger(country, trigger: dict) -> bool:
    field = trigger.get("field")
    if field is None:
        return False

    value = get_country_value(country, field)

    if "operator" in trigger:
        operator = trigger["operator"]
        target = trigger["value"]

        if operator == ">":
            return value > target
        if operator == "<":
            return value < target
        if operator == ">=":
            return value >= target
        if operator == "<=":
            return value <= target
        if operator == "==":
            return value == target
        if operator == "!=":
            return value != target

    if "greater_than" in trigger:
        return value > trigger["greater_than"]

    if "less_than" in trigger:
        return value < trigger["less_than"]

    if "greater_or_equal" in trigger:
        return value >= trigger["greater_or_equal"]

    if "less_or_equal" in trigger:
        return value <= trigger["less_or_equal"]

    if "equals" in trigger:
        return value == trigger["equals"]

    return False


def apply_effect(country, effect: dict) -> None:
    field = effect["field"]
    amount = effect["amount"]

    if field == "stability":
        country.state.stability += amount
    elif field == "legitimacy":
        country.state.legitimacy += amount
    elif field == "administrative_capacity":
        country.state.administrative_capacity += amount
    elif field == "corruption":
        country.state.corruption += amount
    elif field == "war_support":
        country.state.war_support += amount
    elif field == "social_cohesion":
        country.state.social_cohesion += amount
    elif field == "unrest":
        country.state.unrest += amount

    elif field == "inflation":
        country.economy.inflation += amount
    elif field == "unemployment":
        country.economy.unemployment += amount

    elif field == "tech_level":
        country.technology.tech_level += amount
    elif field == "military_power":
        country.military.military_power += amount

    else:
        current = getattr(country, field)
        setattr(country, field, current + amount)


def process_events(world, events) -> None:
    for event in events:
        trigger = event.get("trigger")

        if not trigger:
            continue

        for country in world.countries.values():
            if check_trigger(country, trigger):
                for effect in event.get("effects", []):
                    apply_effect(country, effect)

                world.log_event(
                    f"{event['name']} in {country.name}"
                )

                country.clamp()
