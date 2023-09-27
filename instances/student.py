from pydantic import BaseModel


class Student(BaseModel):
    full_name: str
    group: str
    course: int
    age: int
    average_rating: float
