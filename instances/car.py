from pydantic import BaseModel


class Car(BaseModel):
    model: str
    vin: str
    engine_volume: float
    price: int
    average_speed: float
