def calculate_province_trade_income(province, base_prices: dict[str, float]) -> float:
    if not province.resource:
        return 0.0

    base_price = base_prices.get(province.resource, 0.0)

    return (
        base_price
        * (province.resource_output / 100)
        * (province.trade_power / 100)
    )


def update_trade_income(world, base_prices: dict[str, float]) -> None:
    for province in world.provinces.values():
        province.trade_income = calculate_province_trade_income(
            province,
            base_prices
        )
