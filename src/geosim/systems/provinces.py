def update_provinces(world) -> None:
    for province in world.provinces.values():
        owner = world.countries.get(province.owner)

        if owner is None:
            continue

        growth = world.global_growth

        growth += (province.infrastructure - 50) / 180
        growth += (province.industry - 50) / 160
        growth += (province.development - 50) / 200

        growth -= province.unrest / 100
        growth -= province.autonomy / 300

        if province.is_coastal:
            growth += 0.05

        if province.has_port:
            growth += 0.08

        if "financial_center" in province.buildings:
            growth += 0.12

        if "manufacturing_cluster" in province.buildings:
            growth += 0.10

        if "tech_hub" in province.buildings:
            growth += 0.10

        monthly_growth = growth / 12 / 100

        province.gdp_b *= 1 + monthly_growth
        province.resource_output *= 1 + monthly_growth

        if owner.stability < 50:
            province.unrest += 0.05

        if owner.stability > 70:
            province.unrest -= 0.03

        if province.owner not in province.cores:
            province.unrest += 0.08

        if province.unrest > 40:
            owner.stability -= 0.05

        province.clamp()
        owner.clamp()
