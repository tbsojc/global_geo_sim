from src.geosim.events.engine import process_events
from src.geosim.events.random_events import trigger_random_events
from src.geosim.systems.aggregation import aggregate_all_countries
from src.geosim.systems.diplomacy import update_diplomacy
from src.geosim.systems.economy import update_economy
from src.geosim.systems.politics import update_politics
from src.geosim.systems.provinces import update_provinces


def run_tick(world, events) -> None:
    update_provinces(world)

    aggregate_all_countries(world)

    update_economy(world)
    update_politics(world)
    update_diplomacy(world)

    process_events(world, events)
    trigger_random_events(world)

    aggregate_all_countries(world)

    world.advance_month()


def run_ticks(world, events, months: int) -> None:
    for _ in range(months):
        run_tick(world, events)
