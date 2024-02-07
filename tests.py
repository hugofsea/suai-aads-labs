import unittest

from main import DoubleLinkedList, USD, Car


class TestDoubleLinkedList(unittest.TestCase):
    def setUp(self):
        self.car_list = DoubleLinkedList([Car('Model1', 'VIN1', 2.0, USD(15000), 120.0),
                                          Car('Model2', 'VIN2', 1.8, USD(12000), 110.0),
                                          Car('Model3', 'VIN3', 2.5, USD(20000), 130.0)])

    def test_push(self):
        self.car_list.push(Car('Model4', 'VIN4', 2.2, USD(18000), 125.0))
        self.assertEqual(len(self.car_list), 4)

    def test_unshift(self):
        self.car_list.unshift(Car('Model0', 'VIN0', 2.4, USD(16000), 115.0))
        self.assertEqual(len(self.car_list), 4)

    def test_pop(self):
        popped_car = self.car_list.pop()
        self.assertEqual(len(self.car_list), 2)
        self.assertEqual(popped_car, Car('Model3', 'VIN3', 2.5, USD(20000), 130.0))

    def test_shift(self):
        shifted_car = self.car_list.shift()
        self.assertEqual(len(self.car_list), 2)
        self.assertEqual(shifted_car, Car('Model1', 'VIN1', 2.0, USD(15000), 120.0))

    def test_has(self):
        self.assertTrue(self.car_list.has(Car('Model2', 'VIN2', 1.8, USD(12000), 110.0)))
        self.assertFalse(self.car_list.has(Car('Model4', 'VIN4', 2.2, USD(18000), 125.0)))

    def test_reverse(self):
        self.car_list.reverse()
        reversed_data = list(self.car_list)
        self.assertEqual(reversed_data, [Car('Model3', 'VIN3', 2.5, USD(20000), 130.0),
                                         Car('Model2', 'VIN2', 1.8, USD(12000), 110.0),
                                         Car('Model1', 'VIN1', 2.0, USD(15000), 120.0)])

    def test_merge_sort(self):
        self.car_list.merge_sort()
        sorted_data = list(self.car_list)
        self.assertEqual(sorted_data, [Car('Model2', 'VIN2', 1.8, USD(12000), 110.0),
                                       Car('Model1', 'VIN1', 2.0, USD(15000), 120.0),
                                       Car('Model3', 'VIN3', 2.5, USD(20000), 130.0)])

    def test_heap_sort(self):
        self.car_list.heap_sort()
        sorted_data = list(self.car_list)
        self.assertEqual(sorted_data, [
            Car('Model3', 'VIN3', 2.5, USD(20000), 130.0),
            Car('Model1', 'VIN1', 2.0, USD(15000), 120.0),
            Car('Model2', 'VIN2', 1.8, USD(12000), 110.0),
        ])

    def test_selection_sort(self):
        self.car_list.selection_sort()
        sorted_data = list(self.car_list)
        self.assertEqual(sorted_data, [
            Car('Model2', 'VIN2', 1.8, USD(12000), 110.0),
            Car('Model1', 'VIN1', 2.0, USD(15000), 120.0),
            Car('Model3', 'VIN3', 2.5, USD(20000), 130.0),
        ])

    def test_comb_sort(self):
        self.car_list.comb_sort()
        sorted_data = list(self.car_list)
        self.assertEqual(sorted_data, [
            Car('Model3', 'VIN3', 2.5, USD(20000), 130.0),
            Car('Model1', 'VIN1', 2.0, USD(15000), 120.0),
            Car('Model2', 'VIN2', 1.8, USD(12000), 110.0)
        ])


if __name__ == '__main__':
    unittest.main()
