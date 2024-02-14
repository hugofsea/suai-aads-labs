import random
from dataclasses import dataclass
from typing import Optional, NamedTuple, NewType

USD = NewType('USD', int)


class ShouldBeSortedError(Exception):
    ...


class Car(NamedTuple):
    model: str
    vin: str
    engine_volume: float
    price: USD
    average_speed: float


@dataclass
class Node:
    data: Car
    prev_ptr: 'Optional[Node]' = None
    next_ptr: 'Optional[Node]' = None


class DoubleLinkedList:
    def __init__(self, *args: Car):
        self.__head: Optional[Node] = None
        self.__tail: Optional[Node] = None
        self.__length: int = 0

        for data in args:
            self.push(data)

    def __getitem__(self, __index: int) -> Car:
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

        return node.data

    def __contains__(self, __data: Car) -> bool:
        node = self.__head

        while node is not None:
            if node.data == __data:
                return True

            node = node.next_ptr

        return False

    def __len__(self) -> int:
        return self.__length

    def __iter__(self) -> 'DoubleLinkedList':
        self.__iterator = self.__head
        return self

    def __next__(self) -> Car:
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
    def first(self) -> Optional[Car]:
        return self.__head.data if self.__head is not None else None

    @property
    def last(self) -> Optional[Car]:
        return self.__tail.data if self.__tail is not None else None

    def push(self, data: Car) -> None:
        new_node = Node(data=data, prev_ptr=self.__tail)

        if self.__length == 0:
            self.__head = self.__tail = new_node
            self.__length += 1
            return

        self.__tail.next_ptr = new_node
        self.__tail = new_node
        self.__length += 1

    def unshift(self, data: Car) -> None:
        new_node = Node(data=data, next_ptr=self.__head)

        if self.__length == 0:
            self.__head = self.__tail = new_node
            self.__length += 1
            return

        self.__head.prev_ptr = new_node
        self.__head = new_node
        self.__length += 1

    def pop(self) -> Car:
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

    def shift(self) -> Car:
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

    def has(self, __data: Car, right_search: bool = False):
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

    def merge_sort(self) -> None:
        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i].price <= right[j].price:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def _merge_sort(lst):
            if len(lst) <= 1:
                return lst

            mid = len(lst) // 2
            left = _merge_sort(lst[:mid])
            right = _merge_sort(lst[mid:])
            return merge(left, right)

        sorted_data = _merge_sort(list(self))
        self.__head = None
        self.__tail = None
        self.__length = 0

        for data in sorted_data:
            self.push(data)


def quick_select(linked_list: DoubleLinkedList, k: int) -> Car:
    if len(linked_list) == 1:
        return linked_list.first

    pivot = linked_list[random.randint(0, len(linked_list) - 1)]
    L = DoubleLinkedList()
    M = DoubleLinkedList()
    R = DoubleLinkedList()

    for car in linked_list:
        if pivot.price > car.price:
            L.push(car)

        if pivot.price == car.price:
            M.push(car)

        if pivot.price < car.price:
            R.push(car)

    if k <= len(L):
        return quick_select(L, k)
    elif k <= len(L) + len(M):
        return pivot
    else:
        return quick_select(R, k - (len(L) + len(M)))


def fibonacci_search(linked_list: DoubleLinkedList, price: USD) -> int:
    arr = []
    for car in linked_list:
        if arr and arr[-1].price > car.price:
            raise ShouldBeSortedError('Linked list must be sorted in ascending order')
        arr.append(car)

    if price < arr[0].price or price > arr[-1].price:
        raise ValueError('Not Found')

    fm2 = 0
    fm1 = 1
    fm = fm1 + fm2
    offset = -1

    while fm < len(arr):
        fm2 = fm1
        fm1 = fm
        fm = fm1 + fm2

    while fm > 1:
        i = min(offset + fm2, len(arr) - 1)
        if arr[i].price < price:
            fm = fm1
            fm1 = fm2
            fm2 = fm - fm1
            offset = i
        elif arr[i].price > price:
            fm = fm2
            fm1 = fm1 - fm2
            fm2 = fm - fm1
        else:
            return i

    if fm1 == 1:
        if arr[offset + 1].price == price:
            return offset + 1

    raise ValueError('Not Found')
