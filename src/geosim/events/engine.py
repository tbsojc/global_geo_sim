def check_trigger(country, trigger: dict) -> bool:
    field = trigger["field"]
    value = getattr(country, field)

    if "greater_than" in trigger:
        return value > trigger["greater_than"]

    if "less_than" in trigger:
        return value < trigger["less_than"]

    return False


def apply_effect(country, effect: dict) -> None:
    field = effect["field"]
    change = effect["change"]

    current = getattr(country, field)
    setattr(country, field, current + change)

    country.clamp()


def process_events(world, events) -> None:
    for event in events:
        for country in world.countries.values():
            if check_trigger(country, event["trigger"]):
                apply_effect(country, event["effect"])
                world.log_event(
                    f"{event['name']} in {country.name}: "
                    f"{event['effect']['field']} {event['effect']['change']:+}"
                )
