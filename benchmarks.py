from main import Car, USD, DoubleLinkedList, quick_select, fibonacci_search
import timeit
import random

random_cars = [
    Car(
        f'Model{i}',
        f'VIN{i}',
        random.uniform(1.0, 3.0),
        USD(10000 + i * 100),
        random.uniform(100.0, 150.0)
    )
    for i in range(1000)
]


def benchmark_quick_select():
    car_list = DoubleLinkedList(*random_cars)

    def stmt():
        quick_select(car_list, random.randint(1, 1000))

    duration = timeit.timeit(stmt, number=100)
    print(f'Quick select: {duration:.6f} seconds')


def benchmark_fib_search():
    car_list = DoubleLinkedList(*random_cars)

    def stmt():
        fibonacci_search(car_list, USD(10000 + 100 * random.randint(1, 1000)))

    duration = timeit.timeit(stmt, number=100)
    print(f'Fib search: {duration:.6f} seconds')


if __name__ == '__main__':
    benchmark_quick_select()
    benchmark_fib_search()
