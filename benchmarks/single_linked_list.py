import time
from typing import Callable, Literal, Any

from datastructures import SingleLinkedList

ITERATIONS = 20_000


class SignleLinkedListBenchmark:
    @staticmethod
    def run():
        tests_args = (
            ('push', lambda index: [index]),
            ('unshift', lambda index: [index]),
            ('shift', lambda index: []),
            ('pop', lambda index: []),
            ('index', lambda index: [index]),
            ('insert', lambda index: [index, index]),
            ('remove', lambda index: [index])
        )

        for test_args in tests_args:
            SignleLinkedListBenchmark.test(*test_args)

    @staticmethod
    def test(
            method_name: Literal['push', 'unshift', 'shift', 'pop', 'index', 'insert', 'remove'],
            get_arguments: Callable[[int], dict[str, Any]]
    ):
        linked_list = SingleLinkedList[int]()

        # filling
        for index in range(ITERATIONS - 1, -1, -1):
            linked_list.push(index)

        start = time.time()

        for index in range(ITERATIONS):
            SingleLinkedList.__dict__[method_name](linked_list, *get_arguments(index))

        end = time.time()

        print(f'Elapsed time for {method_name} method and {ITERATIONS} iterations is {end - start} seconds')


if __name__ == '__main__':
    SignleLinkedListBenchmark.run()
