from src.geosim.core.country import CountryModifiers


def modifier_from_slider(value: int, per_step: float) -> float:
    return value * per_step


def apply_slider_modifiers(country) -> CountryModifiers:
    sliders = country.sliders

    mods = CountryModifiers()

    # -5 Demokratie / +5 Autoritarismus
    mods.diplomacy_efficiency += modifier_from_slider(
        -sliders.democracy_authoritarian,
        0.01,
    )

    mods.administration_efficiency += modifier_from_slider(
        sliders.democracy_authoritarian,
        0.01,
    )

    mods.stability_modifier += modifier_from_slider(
        -abs(sliders.democracy_authoritarian),
        0.002,
    )

    # -5 Freiheit / +5 Kontrolle
    mods.research_efficiency += modifier_from_slider(
        -sliders.liberty_control,
        0.01,
    )

    mods.unrest_modifier += modifier_from_slider(
        sliders.liberty_control,
        -0.005,
    )

    mods.stability_modifier += modifier_from_slider(
        sliders.liberty_control,
        0.002,
    )

    # -5 Globalismus / +5 Nationalismus
    mods.trade_efficiency += modifier_from_slider(
        -sliders.globalism_nationalism,
        0.015,
    )

    mods.stability_modifier += modifier_from_slider(
        sliders.globalism_nationalism,
        0.002,
    )

    # -5 Traditional / +5 Progressive
    mods.research_efficiency += modifier_from_slider(
        sliders.traditional_progressive,
        0.01,
    )

    mods.stability_modifier += modifier_from_slider(
        -abs(sliders.traditional_progressive),
        0.001,
    )

    # -5 Zentralisierung / +5 Dezentralisierung
    mods.administration_efficiency += modifier_from_slider(
        -sliders.centralization_decentralization,
        0.015,
    )

    mods.unrest_modifier += modifier_from_slider(
        -sliders.centralization_decentralization,
        -0.003,
    )

    # -5 Produktion / +5 Handel
    mods.production_efficiency += modifier_from_slider(
        -sliders.production_trade,
        0.015,
    )

    mods.trade_efficiency += modifier_from_slider(
        sliders.production_trade,
        0.015,
    )

    # -5 Freier Markt / +5 Planwirtschaft
    mods.trade_efficiency += modifier_from_slider(
        -sliders.free_market_planned,
        0.012,
    )

    mods.production_efficiency += modifier_from_slider(
        sliders.free_market_planned,
        0.01,
    )

    mods.research_efficiency += modifier_from_slider(
        -sliders.free_market_planned,
        0.008,
    )

    # -5 Hawk / +5 Dove
    mods.military_industry_efficiency += modifier_from_slider(
        -sliders.hawk_dove,
        0.02,
    )

    mods.stability_modifier += modifier_from_slider(
        sliders.hawk_dove,
        0.002,
    )

    # -5 Interventionismus / +5 Isolationismus
    mods.diplomacy_efficiency += modifier_from_slider(
        -abs(sliders.interventionism_isolationism),
        0.004,
    )

    mods.trade_efficiency += modifier_from_slider(
        sliders.interventionism_isolationism,
        -0.006,
    )

    return mods
