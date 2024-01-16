from timeit import timeit
from implementation import CarWithKey, CarAVLTree
from models import USD

ITERATIONS = 2000
ITEMS = 500


def insert():
    tree = CarAVLTree()
    cars = [
        CarWithKey(model=f"Car_{i}", vin="VIN1", engine_volume=2.0, price=USD(2000 * i), average_speed=100)
        for i in range(1, ITEMS + 1)
    ]
    return lambda: [tree.insert(car) for car in cars]


def find():
    tree = CarAVLTree()
    cars = [
        CarWithKey(model=f"Car_{i}", vin="VIN1", engine_volume=2.0, price=USD(2000 * i), average_speed=100)
        for i in range(1, ITEMS + 1)
    ]

    for car in cars:
        tree.insert(car)

    return lambda: [tree.find(car.key) for car in cars]


if __name__ == '__main__':
    insertion_time = timeit(insert(), number=ITERATIONS)
    search_time = timeit(find(), number=ITERATIONS)

    print(f"Insertion time: {insertion_time:.6f} seconds for {ITERATIONS} iterations and {ITEMS} items")
    print(f"Search time: {search_time:.6f} seconds for {ITERATIONS} iterations and {ITEMS} items")
