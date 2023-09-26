from hashlib import md5
from typing import TypeVar, Generic, NamedTuple, Optional, Any, Callable

K = TypeVar("K", int, float, bool, str, tuple)
V = TypeVar("V")


class HashNode(NamedTuple, Generic[K, V]):
    key: K
    value: V


class HashTable(Generic[K, V]):
    T = TypeVar("T")

    def __init__(self):
        self.__size = 0
        self.__factor = 0.75
        self.__sizes = [
            5, 11, 23, 47, 97, 193, 389, 769, 1543, 3072, 3079, 12289,
            24593, 49157, 98317, 196613, 393241, 786433, 1572869, 3145739,
            6291469, 12582917, 25165843, 50331653, 100663319, 201326611,
            402653189, 805306457, 1610612736, 2147483629
        ]
        self.__sizes_index = 0
        self.__array: list[Optional[HashNode]] = [None] * self.__sizes[self.__sizes_index]

    def __getitem__(self, __key: K) -> V:
        if not isinstance(__key, (int, float, bool, str, tuple)):
            raise TypeError('hashmap key should be immutable')

        hash_index = self.__get_index(__key)

        if hash_index is None:
            raise KeyError(f'there is no item with key {__key}')

        return self.__array[hash_index].value

    def __setitem__(self, __key: K, __value: V) -> None:
        if not isinstance(__key, (int, float, bool, str, tuple)):
            raise TypeError('hashmap key should be immutable')

        if self.__sizes[self.__sizes_index] * self.__factor < self.__size:
            self.__increase_array_size()

        self.__insert(__key, __value)

    def __delitem__(self, __key: K) -> None:
        if not isinstance(__key, (int, float, bool, str, tuple)):
            raise TypeError('hashmap key should be immutable')

        hash_index = self.__get_index(__key)

        if hash_index is None:
            raise KeyError(f'there is no item with key {__key}')

        node = self.__array[hash_index]
        self.__array[hash_index] = None

        del node

    def __contains__(self, __key: K) -> bool:
        if not isinstance(__key, (int, float, bool, str, tuple)):
            raise TypeError('hashmap key should be immutable')

        return self.__array[self.__get_index(__key)] is not None

    def __str__(self) -> str:
        def add_to_parts(node: HashNode[K, V]) -> None:
            def get_string_format(data: Any) -> str:
                return f"'{data}'" if isinstance(data, str) else f'{data}'

            parts.append(
                f'{get_string_format(node.key)}: {get_string_format(node.value)}'
            )

        parts = []

        self.__map_nodes(add_to_parts)

        return '{' + ', '.join(parts) + '}'

    def __len__(self) -> int:
        return self.__size

    def get(self, __key: K, __default_value: Optional[Any] = None) -> V:
        if not isinstance(__key, (int, float, bool, str, tuple)):
            raise TypeError('hashmap key should be immutable')

        hash_index = self.__get_index(__key)

        return __default_value if self.__array[hash_index] is None else self.__array[hash_index].value

    def values(self) -> list[V]:
        def get_value(node: HashNode[K, V]) -> V:
            return node.value

        return self.__map_nodes(get_value)

    def items(self) -> list[tuple[K, V]]:
        def get_item(node: HashNode[K, V]) -> tuple[K, V]:
            return node.key, node.value

        return self.__map_nodes(get_item)

    def keys(self) -> list[K]:
        def get_key(node: HashNode[K, V]) -> K:
            return node.key

        return self.__map_nodes(get_key)

    def __map_nodes(self, __callback: Callable[[HashNode[K, V]], T]) -> list[T]:
        output = []

        for node in self.__array:
            if node is None:
                continue

            output.append(__callback(node))

        return output

    def __increase_array_size(self) -> None:
        self.__sizes_index += 1
        old_array = self.__array

        self.__size = 0
        self.__array = [None] * self.__sizes[self.__sizes_index]

        for item in old_array:
            if item is None:
                continue

            self.__insert(item.key, item.value)
            del item

        del old_array

    def __insert(self, __key: K, __value: V) -> None:
        if self.__size == len(self.__array):
            raise MemoryError('hash table is full')

        node = HashNode[K, V](__key, __value)
        hash_index = self.__get_index(__key)

        if self.__array[hash_index] is None:
            self.__size += 1

        self.__array[hash_index] = node

    @staticmethod
    def __get_hash(__key: K) -> int:
        result_hash = md5(str(__key).encode('utf-8')).hexdigest()

        return int(result_hash, 16)

    def __get_index(self, __key: K) -> int:
        hash_index = self.__get_hash(__key) % len(self.__array)

        while self.__array[hash_index] is not None and self.__array[hash_index].key != __key:
            hash_index = (hash_index + 1) % len(self.__array)

        return hash_index
