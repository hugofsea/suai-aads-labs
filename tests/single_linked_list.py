import unittest

from datastructures import SingleLinkedList


class TestSingleLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList[int]()

    def test_push(self):
        self.linked_list.push(1)
        self.assertEqual(len(self.linked_list), 1)

        self.linked_list.push(2)
        self.assertEqual(len(self.linked_list), 2)

        self.assertEqual(self.linked_list[0], 1)
        self.assertEqual(self.linked_list[1], 2)

    def test_unshift(self):
        self.linked_list.unshift(1)
        self.assertEqual(len(self.linked_list), 1)

        self.linked_list.unshift(2)
        self.assertEqual(len(self.linked_list), 2)

        self.assertEqual(self.linked_list[0], 2)
        self.assertEqual(self.linked_list[1], 1)

    def test_shift(self):
        self.linked_list.push(1)
        self.linked_list.push(2)

        self.assertEqual(self.linked_list.shift(), 1)
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list[0], 2)

        self.assertEqual(self.linked_list.shift(), 2)
        self.assertEqual(len(self.linked_list), 0)

    def test_pop(self):
        self.linked_list.push(1)
        self.linked_list.push(2)

        self.assertEqual(self.linked_list.pop(), 2)
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list[0], 1)

        self.assertEqual(self.linked_list.pop(), 1)
        self.assertEqual(len(self.linked_list), 0)

    def test_insert(self):
        self.linked_list.push(1)
        self.linked_list.push(3)

        self.linked_list.insert(1, 2)
        self.assertEqual(len(self.linked_list), 3)
        self.assertEqual(self.linked_list[1], 2)

        self.linked_list.insert(0, 0)
        self.assertEqual(len(self.linked_list), 4)
        self.assertEqual(self.linked_list[0], 0)

        self.linked_list.insert(10, 4)
        self.assertEqual(len(self.linked_list), 5)
        self.assertEqual(self.linked_list[4], 4)

    def test_remove(self):
        self.linked_list.push(1)
        self.linked_list.push(2)
        self.linked_list.push(3)

        self.linked_list.remove(2)
        self.assertEqual(len(self.linked_list), 2)
        self.assertEqual(self.linked_list[0], 1)
        self.assertEqual(self.linked_list[1], 3)

        self.linked_list.remove(3)
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list[0], 1)

    def test_reverse(self):
        self.linked_list.push(1)
        self.linked_list.push(2)
        self.linked_list.push(3)

        self.linked_list.reverse()
        self.assertEqual(len(self.linked_list), 3)
        self.assertEqual(self.linked_list[0], 3)
        self.assertEqual(self.linked_list[1], 2)
        self.assertEqual(self.linked_list[2], 1)

    def test_copy(self):
        self.linked_list.push(1)
        self.linked_list.push(2)
        self.linked_list.push(3)

        copied_list = self.linked_list.copy()
        self.assertEqual(len(copied_list), 3)
        self.assertEqual(copied_list[0], 1)
        self.assertEqual(copied_list[1], 2)
        self.assertEqual(copied_list[2], 3)

    def test_index(self):
        self.linked_list.push(1)
        self.linked_list.push(2)
        self.linked_list.push(3)

        self.assertEqual(self.linked_list.index(2), 1)
        self.assertEqual(self.linked_list.index(1), 0)
        self.assertEqual(self.linked_list.index(3), 2)

    def test_contains(self):
        self.linked_list.push(1)
        self.linked_list.push(2)
        self.linked_list.push(3)

        self.assertTrue(2 in self.linked_list)
        self.assertTrue(1 in self.linked_list)
        self.assertTrue(3 in self.linked_list)
        self.assertFalse(4 in self.linked_list)

    def test_equal(self):
        self.linked_list.push(1)
        self.linked_list.push(2)
        self.linked_list.push(3)

        other_list = SingleLinkedList[int]()
        other_list.push(1)
        other_list.push(2)
        other_list.push(3)

        self.assertEqual(self.linked_list, other_list)

        other_list.pop()
        self.assertNotEqual(self.linked_list, other_list)  


if __name__ == "__main__":
    unittest.main()
