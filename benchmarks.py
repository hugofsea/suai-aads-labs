from main import Car, USD, DoubleLinkedList
import timeit
import random

random_cars = [
    Car(
        f'Model{i}',
        f'VIN{i}',
        random.uniform(1.0, 3.0),
        USD(random.randint(10000, 30000)),
        random.uniform(100.0, 150.0)
    )
    for i in range(1000)
]


def benchmark_merge_sort():
    def stmt():
        car_list = DoubleLinkedList(random_cars.copy())
        car_list.merge_sort()

    duration = timeit.timeit(stmt, number=100)
    print(f'Merge Sort: {duration:.6f} seconds')


def benchmark_heap_sort():
    def stmt():
        car_list = DoubleLinkedList(random_cars.copy())
        car_list.heap_sort()

    duration = timeit.timeit(stmt, number=100)
    print(f'Heap Sort: {duration:.6f} seconds')


def benchmark_selection_sort():
    def stmt():
        car_list = DoubleLinkedList(random_cars.copy())
        car_list.selection_sort()

    duration = timeit.timeit(stmt, number=100)
    print(f'Selection Sort: {duration:.6f} seconds')


def benchmark_comb_sort():
    def stmt():
        car_list = DoubleLinkedList(random_cars.copy())
        car_list.comb_sort()

    duration = timeit.timeit(stmt, number=100)
    print(f'Comb Sort: {duration:.6f} seconds')


if __name__ == '__main__':
    benchmark_merge_sort()
    benchmark_heap_sort()
    benchmark_selection_sort()
    benchmark_comb_sort()
