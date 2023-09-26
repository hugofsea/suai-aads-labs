from typing import NamedTuple


class Car(NamedTuple):
    model: str
    vin: str
    engine_volume: float
    price: int
    average_speed: float
