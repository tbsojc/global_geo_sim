def update_provinces(world) -> None:
    for province in world.provinces.values():
        owner = world.countries.get(province.owner)

        if owner is None:
            continue

        mods = owner.final_modifiers

        growth = world.global_growth

        growth += (province.infrastructure - 50) / 180
        growth += (province.industry - 50) / 160
        growth += (province.development - 50) / 200

        growth -= province.unrest / 100
        growth -= province.autonomy / 300

        if province.is_coastal:
            growth += 0.05 * mods.trade_efficiency

        if province.has_port:
            growth += 0.08 * mods.trade_efficiency

        if "financial_center" in province.buildings:
            growth += 0.12 * mods.trade_efficiency

        if "manufacturing_cluster" in province.buildings:
            growth += 0.10 * mods.production_efficiency

        if "tech_hub" in province.buildings:
            growth += 0.10 * mods.research_efficiency

        growth *= mods.production_efficiency

        monthly_growth = growth / 12 / 100

        factor = 1 + monthly_growth

        province.tax_income *= factor
        province.production_income *= factor
        province.trade_income *= factor
        province.resource_output *= 1 + monthly_growth

        if owner.state.stability < 50:
            province.unrest += 0.05

        if owner.state.stability > 70:
            province.unrest -= 0.03

        province.unrest += mods.unrest_modifier

        if province.owner not in province.cores:
            province.unrest += 0.08

        if province.unrest > 40:
            owner.state.stability -= 0.05

        province.clamp()
        owner.clamp()
