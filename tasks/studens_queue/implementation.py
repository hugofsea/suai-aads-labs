import json

from typing import TextIO, Any

from datastructures import Queue
from models import Student


class StudentsQueue(Queue[Student]):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return str(self._list).replace('DoubleLinkedList', 'StudentsQueue')

    def dump(self, file: TextIO) -> None:
        json.dump(
            [student.model_dump() for student in self._list],
            file,
            indent=4
        )

    @classmethod
    def load(cls, file: TextIO) -> 'StudentsQueue':
        queue = cls()
        data: list[dict[str, Any]] = json.load(file)

        for student in data:
            queue.add(Student(**student))

        return queue
