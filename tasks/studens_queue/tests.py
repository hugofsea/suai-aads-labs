import unittest
from implementation import StudentsQueue
from instances import Student


class TestStudentsQueue(unittest.TestCase):

    def setUp(self):
        # Создаем пустую очередь для каждого теста
        self.queue = StudentsQueue()

    def test_add_student(self):
        student1 = Student(full_name="Alice", group="A101", course=1, age=20, average_rating=4.5)
        student2 = Student(full_name="Bob", group="B202", course=2, age=21, average_rating=3.8)

        self.queue.add(student1)
        self.queue.add(student2)

        self.assertEqual(len(self.queue), 2)

    def test_get_student(self):
        student1 = Student(full_name="Alice", group="A101", course=1, age=20, average_rating=4.5)
        student2 = Student(full_name="Bob", group="B202", course=2, age=21, average_rating=3.8)

        self.queue.add(student1)
        self.queue.add(student2)

        retrieved_student = self.queue.get()
        self.assertEqual(retrieved_student, student1)
        self.assertEqual(len(self.queue), 1)

    def test_reverse_queue(self):
        student1 = Student(full_name="Alice", group="A101", course=1, age=20, average_rating=4.5)
        student2 = Student(full_name="Bob", group="B202", course=2, age=21, average_rating=3.8)

        self.queue.add(student1)
        self.queue.add(student2)

        self.queue.reverse()

        self.assertEqual(self.queue.get(), student2)
        self.assertEqual(self.queue.get(), student1)

    def test_dump_and_load(self):
        student1 = Student(full_name="Alice", group="A101", course=1, age=20, average_rating=4.5)
        student2 = Student(full_name="Bob", group="B202", course=2, age=21, average_rating=3.8)

        self.queue.add(student1)
        self.queue.add(student2)

        with open('backups/test.json', 'w') as file:
            self.queue.dump(file)

        with open('backups/test.json', 'r') as file:
            loaded_queue = StudentsQueue.load(file)

        self.assertEqual(len(loaded_queue), len(self.queue))
        self.assertEqual(loaded_queue.get(), self.queue.get())
        self.assertEqual(loaded_queue.get(), self.queue.get())


if __name__ == '__main__':
    unittest.main()
