from dataclasses import dataclass
from typing import Optional, Iterable, NamedTuple, NewType

USD = NewType('USD', int)


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
    def __init__(self, __iterable: Optional[Iterable[Car]] = None):
        self.__head: Optional[Node] = None
        self.__tail: Optional[Node] = None
        self.__length: int = 0

        if __iterable is not None:
            for data in __iterable:
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

    def heap_sort(self) -> None:
        def heapify(lst, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and lst[left].engine_volume < lst[largest].engine_volume:
                largest = left

            if right < n and lst[right].engine_volume < lst[largest].engine_volume:
                largest = right

            if largest != i:
                lst[i], lst[largest] = lst[largest], lst[i]
                heapify(lst, n, largest)

        length = len(self)
        arr: list[Car] = list(self)

        for i in range(length // 2 - 1, -1, -1):
            heapify(arr, length, i)

        for i in range(length - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

        self.__head = None
        self.__tail = None
        self.__length = 0

        for data in arr:
            self.push(data)

    def selection_sort(self) -> None:
        current = self.__head

        while current:
            min_node = current
            next_node = current.next_ptr

            while next_node:
                if min_node.data.engine_volume > next_node.data.engine_volume:
                    min_node = next_node
                next_node = next_node.next_ptr

            if current != min_node:
                current.data, min_node.data = min_node.data, current.data

            current = current.next_ptr

    def comb_sort(self):
        def get_next_gap(current_gap):
            next_gap = int(current_gap / 1.3)
            return max(next_gap, 1)

        arr: list[Car] = list(self)
        n = len(arr)
        gap = n
        swapped = True

        while gap != 1 or swapped:
            gap = get_next_gap(gap)
            swapped = False

            for i in range(0, n - gap):
                j = i + gap
                if arr[i].average_speed < arr[j].average_speed:
                    arr[i], arr[j] = arr[j], arr[i]
                    swapped = True

        self.__head = None
        self.__tail = None
        self.__length = 0

        for data in arr:
            self.push(data)

    def __check_index(self, __index: int):
        if not isinstance(__index, int):
            raise TypeError('list indices must be integers')

        if not (0 <= __index < self.__length or -self.__length <= -__index <= -1):
            raise IndexError('list index out of range')
