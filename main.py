from src.geosim.core.tick import run_tick
from src.geosim.io.loader import load_events, load_world
from src.geosim.ui.console import (
    print_province_summary,
    print_recent_events,
    print_world_summary,
)


def run_simulation(
    scenario_name: str = "2026_world",
    months: int = 24,
    print_every: int = 1,
    show_provinces: bool = True,
) -> None:

    # Welt + Daten laden
    world = load_world(scenario_name)
    events = load_events()

    # Startausgabe
    print("\n=== Simulation gestartet ===")
    print(f"Scenario: {scenario_name}")

    print_world_summary(world)

    if show_provinces:
        print_province_summary(world)

    # Hauptloop
    for step in range(1, months + 1):

        run_tick(world, events)

        # Ausgabeintervall
        if step % print_every == 0 or step == months:

            print_world_summary(world)

            if show_provinces:
                print_province_summary(world)

            print_recent_events(world)

    print("\n=== Simulation beendet ===")


def main() -> None:

    run_simulation(
        scenario_name="2026_world",
        months=24,
        print_every=1,
        show_provinces=True,
    )


if __name__ == "__main__":
    main()
