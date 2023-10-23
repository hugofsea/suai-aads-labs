from typing import NewType
from pydantic import BaseModel

USD = NewType('USD', int)


class Car(BaseModel):
    model: str
    vin: str
    engine_volume: float
    price: USD
    average_speed: float
