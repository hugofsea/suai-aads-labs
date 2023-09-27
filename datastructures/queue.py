from typing import TypeVar, Generic, Optional, Iterable

from datastructures import DoubleLinkedList

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self, iterable: Optional[Iterable[T]] = None):
        self._list = DoubleLinkedList[T](iterable)
        self._size = 0

    def __str__(self) -> str:
        return str(self._list).replace('DoubleLinkedList', 'Queue')

    @property
    def last(self) -> T:
        return self._list.last

    @property
    def first(self) -> T:
        return self._list.first

    def add(self, data: T) -> None:
        self._list.push(data)

    def get(self) -> T:
        return self._list.shift()

    def reverse(self) -> None:
        self._list.reverse()

    def clear(self) -> None:
        del self._list

        self._list = DoubleLinkedList[T]()
        self._size = 0
