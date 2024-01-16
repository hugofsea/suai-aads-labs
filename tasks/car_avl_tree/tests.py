import unittest
from datastructures.avl_tree import EmptyTreeError
from models import Car, USD
from implementation import CarAVLTree, CarWithKey


class TestCarAVLTree(unittest.TestCase):
    def setUp(self):
        # Создаем пустое AVL-дерево для каждого теста
        self.tree = CarAVLTree()

    def test_insert_and_find(self):
        car1 = Car(model="Car1", vin="VIN1", engine_volume=2.0, price=USD(20000), average_speed=100)
        car2 = Car(model="Car2", vin="VIN2", engine_volume=2.5, price=USD(25000), average_speed=120)

        self.tree.insert(CarWithKey(**car1.model_dump()))
        self.tree.insert(CarWithKey(**car2.model_dump()))

        found_car1, found1 = self.tree.find(car1.price)
        found_car2, found2 = self.tree.find(car2.price)

        self.assertTrue(found1)
        self.assertTrue(found2)
        self.assertEqual(found_car1.model, car1.model)
        self.assertEqual(found_car2.model, car2.model)

    def test_remove(self):
        car1 = Car(model="Car1", vin="VIN1", engine_volume=2.0, price=USD(20000), average_speed=100)
        car2 = Car(model="Car2", vin="VIN2", engine_volume=2.5, price=USD(25000), average_speed=120)

        self.tree.insert(CarWithKey(**car1.model_dump()))
        self.tree.insert(CarWithKey(**car2.model_dump()))

        self.tree.remove(car1.price)

        _, found1 = self.tree.find(car1.price)
        _, found2 = self.tree.find(car2.price)

        self.assertFalse(found1)
        self.assertTrue(found2)

    def test_min_max(self):
        car1 = Car(model="Car1", vin="VIN1", engine_volume=2.0, price=USD(20000), average_speed=100)
        car2 = Car(model="Car2", vin="VIN2", engine_volume=2.5, price=USD(25000), average_speed=120)
        car3 = Car(model="Car3", vin="VIN3", engine_volume=3.0, price=USD(30000), average_speed=150)

        self.tree.insert(CarWithKey(**car1.model_dump()))
        self.tree.insert(CarWithKey(**car2.model_dump()))
        self.tree.insert(CarWithKey(**car3.model_dump()))

        min_car = self.tree.get_min()
        max_car = self.tree.get_max()

        self.assertEqual(min_car.model, "Car1")
        self.assertEqual(max_car.model, "Car3")

    def test_empty_tree(self):
        with self.assertRaises(EmptyTreeError):
            self.tree.get_min()

        with self.assertRaises(EmptyTreeError):
            self.tree.get_max()

        with self.assertRaises(EmptyTreeError):
            self.tree.remove(USD(20000))

    def test_dump_and_load(self):
        car1 = Car(model="Car1", vin="VIN1", engine_volume=2.0, price=USD(20000), average_speed=100)
        car2 = Car(model="Car2", vin="VIN2", engine_volume=2.5, price=USD(25000), average_speed=120)

        self.tree.insert(CarWithKey(**car1.model_dump()))
        self.tree.insert(CarWithKey(**car2.model_dump()))

        with open('backups/test.json', 'w') as file:
            self.tree.dump(file)

        with open('backups/test.json', 'r') as file:
            loaded_tree = CarAVLTree.load(file)

        found_car1, found1 = loaded_tree.find(car1.price)
        found_car2, found2 = loaded_tree.find(car2.price)

        self.assertTrue(found1)
        self.assertTrue(found2)
        self.assertEqual(found_car1.model, car1.model)
        self.assertEqual(found_car2.model, car2.model)


if __name__ == '__main__':
    unittest.main()
