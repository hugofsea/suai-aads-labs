from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar("T")


@dataclass
class SingleNode(Generic[T]):
    data: T
    next_ptr: Optional['SingleNode[T]'] = None


class SingleLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.__length: int = 0
        self.__head: Optional[SingleNode[T]] = None
        self.__tail: Optional[SingleNode[T]] = None

    def __len__(self) -> int:
        return self.__length

    def __str__(self) -> str:
        string = '['
        node = self.__head

        while node is not None:
            string += str(node.data)

            if node.next_ptr is not None:
                string += ', '

            node = node.next_ptr

        return string + ']'

    def __getitem__(self, __key: int) -> T:
        if not isinstance(__key, int):
            raise TypeError("key must be an integer")

        node = self.__get_node(__key)

        return node.data

    def __setitem__(self, __key: int, __object: T) -> None:
        if not isinstance(__key, int):
            raise TypeError("key must be an integer")

        node = self.__get_node(__key)
        node.data = __object

    def __delitem__(self, __key: int) -> None:
        if not isinstance(__key, int):
            raise TypeError("key must be an integer")

        node = self.__get_node(__key - 1)

        delete_node = node.next_ptr
        node.next_ptr = delete_node.next_ptr

        del delete_node
        self.__length -= 1

    def __reversed__(self) -> 'SingleLinkedList[T]':
        def unshift(new_list: 'SingleLinkedList[T]', data: T) -> None:
            new_list.unshift(data)

        return self.__mutate_new(unshift)

    def __add__(self, __other: 'SingleLinkedList[T]') -> 'SingleLinkedList[T]':
        new_list = self.copy()

        for data in __other:
            new_list.push(data)

        return new_list

    def __contains__(self, __object: T) -> bool:
        for data in self:
            if data == __object:
                return True

        return False

    def __eq__(self, __other: 'SingleLinkedList[T]') -> bool:
        if not isinstance(__other, SingleLinkedList) or self.__length != len(__other):
            return False

        for index in range(self.__length):
            if self[index] != __other[index]:
                return False

        return True

    def push(self, __object: T) -> None:
        node = SingleNode[T](__object)

        if self.__length == 0:
            self.__head = node
            self.__tail = node
            self.__length += 1
            return

        self.__tail.next_ptr = node
        self.__tail = node
        self.__length += 1

    def unshift(self, __object: T) -> None:
        node = SingleNode[T](__object)

        if self.__length == 0:
            self.__head = node
            self.__tail = node
            self.__length += 1
            return

        node.next_ptr = self.__head
        self.__head = node
        self.__length += 1

    def shift(self) -> T:
        if self.__length == 0:
            raise IndexError('shift from empty list')

        first_node = self.__head
        first_node_value = first_node.data
        second_node = first_node.next_ptr

        self.__head = second_node
        self.__length -= 1

        del first_node

        return first_node_value

    def pop(self) -> T:
        if self.__length == 0:
            raise IndexError('pop from empty list')

        if self.__length == 1:
            node = self.__head
            node_value = node.data

            self.__head = self.__tail = None
            self.__length = 0
            del node
            return node_value

        penult_node = self.__get_node(self.__length - 2)

        last_node = self.__tail
        last_node_value = last_node.data

        penult_node.next_ptr = None
        self.__tail = penult_node
        self.__length -= 1

        del last_node

        return last_node_value

    def insert(self, __index: int, __object: T) -> None:
        if not isinstance(__index, int):
            raise TypeError("index must be an integer")

        if __index < 0:
            raise IndexError('index should be greater than 0')

        if __index == 0:
            return self.unshift(__object)

        if __index >= self.__length:
            return self.push(__object)

        node = self.__get_node(__index - 1)

        insert_node = SingleNode[T](__object)
        insert_node.next_ptr = node.next_ptr
        node.next_ptr = insert_node
        self.__length += 1

    def remove(self, __object: T) -> None:
        node = self.__head

        if node.data == __object:
            return self.shift()

        while node.next_ptr is not None and node.next_ptr.data != __object:
            node = node.next_ptr

        if node.next_ptr is None:
            raise ValueError('value not in list')

        if node.next_ptr == self.__tail:
            self.__tail = node

        remove_node = node.next_ptr
        node.next_ptr = remove_node.next_ptr

        del remove_node
        self.__length -= 1

    def reverse(self) -> None:
        prev_node = None
        current_node = self.__head

        while current_node is not None:
            next_node = current_node.next_ptr
            current_node.next_ptr = prev_node
            prev_node = current_node
            current_node = next_node

        self.__tail, self.__head = self.__head, self.__tail

    def copy(self) -> 'SingleLinkedList[T]':
        def push(new_list: 'SingleLinkedList[T]', data: T) -> None:
            new_list.push(data)

        return self.__mutate_new(push)

    def index(self, __object: T) -> int:
        for idx, data in enumerate(self):
            if data == __object:
                return idx

        raise ValueError(f'{__object} is not in list')

    def __check_range(self, __index: int) -> bool:
        return 0 <= __index < self.__length

    def __get_node(self, __index: int) -> SingleNode:
        if not self.__check_range(__index):
            raise IndexError('list index out of range')

        node = self.__head

        for _ in range(0, __index):
            node = node.next_ptr

        return node

    def __mutate_new(self, callback: Callable[['SingleLinkedList[T]', T], None]) -> 'SingleLinkedList[T]':
        new_list = SingleLinkedList[T]()

        for data in self:
            callback(new_list, data)

        return new_list
