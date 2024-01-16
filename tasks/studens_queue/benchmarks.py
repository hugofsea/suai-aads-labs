from timeit import timeit
from implementation import Queue
from models import Student


ITERATIONS = 2000
ITEMS = 1000


def add():
    queue = Queue()
    students = [Student(full_name="Student " + str(i), group=str(i), course=1, age=20, average_rating=4.0) for i in range(ITEMS)]
    return lambda: [queue.add(student) for student in students]


def remove():
    queue = Queue()
    students = [Student(full_name="Student " + str(i), group=str(i), course=1, age=20, average_rating=4.0) for i in range(ITEMS * ITERATIONS)]
    for student in students:
        queue.add(student)
    return lambda: [queue.get() for _ in range(ITEMS)]


if __name__ == '__main__':
    add_time = timeit(add(), number=ITERATIONS)
    remove_time = timeit(remove(), number=ITERATIONS)

    print(f"Add time: {add_time:.6f} seconds for {ITERATIONS} iterations and {ITEMS} items")
    print(f"Remove time: {remove_time:.6f} seconds for {ITERATIONS} iterations and {ITEMS} items")
