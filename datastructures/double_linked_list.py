from dataclasses import dataclass
from typing import TypeVar, Optional, Iterable

T = TypeVar('T')


@dataclass
class Node[T]:
    data: T
    prev_ptr: 'Optional[Node[T]]' = None
    next_ptr: 'Optional[Node[T]]' = None


class DoubleLinkedList[T]:
    def __init__(self, __iterable: Optional[Iterable[T]] = None):
        self.__head: Optional[Node[T]] = None
        self.__tail: Optional[Node[T]] = None
        self.__length: int = 0

        if __iterable is not None:
            for data in __iterable:
                self.push(data)

    def __getitem__(self, __index: int) -> T:
        self.__check_index(__index)

        if __index >= 0:
            node = self.__head
            i = 0

            while i < __index:
                node = node.next_ptr
                i += 1
        else:
            node = self.__tail
            i = self.__length - 1

            while i > __index:
                node = node.prev_ptr
                i -= 1

    def __contains__(self, __data: T) -> bool:
        node = self.__head

        while node is not None:
            if node.data == __data:
                return True

            node = node.next_ptr

        return False

    def __len__(self) -> int:
        return self.__length

    def __iter__(self) -> 'DoubleLinkedList[T]':
        self.__iterator = self.__head
        return self

    def __next__(self) -> T:
        if self.__iterator is None:
            raise StopIteration

        result = self.__iterator.data
        self.__iterator = self.__iterator.next_ptr

        return result

    def __str__(self) -> str:
        string = 'DoubleLinkedList(['
        node = self.__head

        while node is not None:
            string += str(node.data)

            if node.next_ptr is not None:
                string += ', '

            node = node.next_ptr

        return string + '])'

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

        self.__tail.next_ptr = new_node
        self.__tail = new_node
        self.__length += 1

    def unshift(self, data: T) -> None:
        new_node = Node(data=data, next_ptr=self.__head)

        if self.__length == 0:
            self.__head = self.__tail = new_node
            self.__length += 1
            return

        self.__head.prev_ptr = new_node
        self.__head = new_node
        self.__length += 1

    def pop(self) -> T:
        if self.__length == 0:
            raise IndexError('pop from empty list')

        remove_node = self.__tail
        data = remove_node.data

        self.__tail = remove_node.prev_ptr

        if self.__length == 1:
            self.__head = None
        else:
            self.__tail.next_ptr = None

        del remove_node
        self.__length -= 1

        return data

    def shift(self) -> T:
        if self.__length == 0:
            raise IndexError('shift from empty list')

        remove_node = self.__head
        data = remove_node.data

        self.__head = remove_node.next_ptr

        if self.__length == 1:
            self.__tail = None
        else:
            self.__head.prev_ptr = None

        del remove_node
        self.__length -= 1

        return data

    def has(self, __data: T, right_search: bool = False):
        node = self.__head if not right_search else self.__tail

        while node is not None:
            if node.data == __data:
                return True

            node = node.next_ptr if not right_search else node.prev_ptr

        return False

    def reverse(self):
        current_node = self.__head

        while current_node is not None:
            next_node = current_node.next_ptr
            current_node.next_ptr, current_node.prev_ptr = current_node.prev_ptr, current_node.next_ptr
            current_node = next_node

        self.__head, self.__tail = self.__tail, self.__head

    def __check_index(self, __index: int):
        if not isinstance(__index, int):
            raise TypeError('list indices must be integers')

        if not (0 <= __index < self.__length or -self.__length <= -__index <= -1):
            raise IndexError('list index out of range')
