from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Node(Generic[T]):
    data: T
    prev_ptr: 'Optional[Node[T]]' = None
    next_ptr: 'Optional[Node[T]]' = None


class DoubleLinkedList(Generic[T]):
    def __init__(self):
        self.__head: Optional[Node[T]] = None
        self.__tail: Optional[Node[T]] = None
        self.__length: int = 0

    def __len__(self) -> int:
        return self.__length

    @property
    def first(self) -> Optional[T]:
        return self.__head.data if self.__head is not None else None

    @property
    def last(self) -> Optional[T]:
        return self.__tail.data if self.__tail is not None else None

    def push(self, data: T) -> None:
        new_node = Node(data=data, prev_ptr=self.__tail)

        if self.__length == 0:
            self.__head = self.__tail = new_node
            self.__length += 1
            return

        self.__tail.prev_ptr = new_node
        self.__tail = new_node
        self.__length += 1

    def unshift(self, data: T) -> None:
        new_node = Node(data=data, next_ptr=self.__head)

        if self.__length == 0:
            self.__head = self.__tail = new_node
            self.__length += 1
            return

        self.__head.next_ptr = new_node
        self.__head = new_node
        self.__length += 1

    def pop(self) -> T:
        if self.__length == 0:
            raise IndexError('pop from empty list')

        remove_node = self.__tail
        data = remove_node.data

        self.__tail = remove_node.prev_ptr
        self.__tail.next_ptr = None

        if self.__length == 1:
            self.__head = None

        del remove_node
        self.__length -= 1

        return data

    def shift(self) -> T:
        if self.__length == 0:
            raise IndexError('pop from empty list')

        remove_node = self.__head
        data = remove_node.data

        self.__head = remove_node.next_ptr
        self.__head.prev_ptr = None

        if self.__length == 1:
            self.__tail = None

        del remove_node
        self.__length -= 1

        return data

    def reverse(self):
        current_node = self.__head

        while current_node is not None:
            next_node = current_node.next_ptr
            current_node.next_ptr, current_node.prev_ptr = current_node.prev_ptr, current_node.next_ptr
            current_node = next_node

        self.__head, self.__tail = self.__tail, self.__head
