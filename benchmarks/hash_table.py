import time
from typing import Callable, Literal, Any

from datastructures import HashTable

ITERATIONS = 200_000


class SignleLinkedListBenchmark:
    @staticmethod
    def run():
        tests_args = (
            ('__getitem__', lambda index: [f'key_{index}']),
            ('__setitem__', lambda index: [f'key_{index}', index]),
            ('__delitem__', lambda index: [f'key_{index}']),
            ('__contains__', lambda index: [f'key_{index}']),
            ('get', lambda index: [f'key_{index}']),
        )

        for test_args in tests_args:
            SignleLinkedListBenchmark.test(*test_args)

    @staticmethod
    def test(
            method_name: Literal[
                '__getitem__',
                '__setitem__',
                '__delitem__',
                '__contains__',
                'get',
            ],
            get_arguments: Callable[[int], dict[str, Any]]
    ):
        hash_table = HashTable[str, int]()

        # filling
        for index in range(ITERATIONS - 1, -1, -1):
            hash_table[f'key_{index}'] = index

        start = time.time()

        for index in range(ITERATIONS):
            HashTable.__dict__[method_name](hash_table, *get_arguments(index))

        end = time.time()

        print(f'Elapsed time for {method_name} method and {ITERATIONS} iterations is {end - start} seconds')


if __name__ == '__main__':
    SignleLinkedListBenchmark.run()
