from src.geosim.events.engine import process_events
from src.geosim.events.random_events import trigger_random_events
from src.geosim.systems.aggregation import aggregate_all_countries
from src.geosim.systems.diplomacy import update_diplomacy
from src.geosim.systems.economy import update_economy
from src.geosim.systems.politics import update_politics
from src.geosim.systems.provinces import update_provinces
from src.geosim.systems.modifiers import update_country_modifiers


def run_tick(world, events) -> None:
    world.advance_month()

    update_country_modifiers(world)

    update_provinces(world)
    aggregate_all_countries(world)
    update_economy(world)
    update_politics(world)
    update_diplomacy(world)
    process_events(world, events)
    trigger_random_events(world)


def run_ticks(world, events, months: int) -> None:
    for _ in range(months):
        run_tick(world, events)
