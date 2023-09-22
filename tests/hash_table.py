import unittest

from datastructures import HashTable


class TestHashTable(unittest.TestCase):

    def test_init(self):
        table = HashTable[str, str]()
        self.assertIsInstance(table, HashTable)

    def test_set_and_get(self):
        table = HashTable[str, str]()
        table['key1'] = 'value1'
        self.assertEqual(table['key1'], 'value1')

    def test_set_with_collision(self):
        table = HashTable[str, str]()
        table['key1'] = 'value1'
        table['key2'] = 'value2'

        self.assertEqual(table['key1'], 'value1')
        self.assertEqual(table['key2'], 'value2')

    def test_get_with_default(self):
        table = HashTable()
        self.assertEqual(table.get('non_existent_key'), None)
        self.assertEqual(
            table.get('non_existent_key', 'default_value'),
            'default_value'
        )

    def test_contains(self):
        table = HashTable[str, str]()
        table['key1'] = 'value1'

        self.assertTrue('key1' in table)
        self.assertFalse('key2' in table)

    def test_delitem(self):
        table = HashTable[str, str]()
        table['key1'] = 'value1'
        del table['key1']

        self.assertFalse('key1' in table)

    def test_str(self):
        table = HashTable[str, str]()
        table['key1'] = 'value1'
        table['key2'] = 'value2'

        expected_str_pattern = r"{'key1': 'value1', 'key2': 'value2'}|{'key2': 'value2', 'key1': 'value1'}"

        self.assertRegex(str(table), expected_str_pattern)

    def test_values(self):
        table = HashTable[str, str]()
        table['key1'] = 'value1'
        table['key2'] = 'value2'

        values = table.values()
        expected_values = ['value1', 'value2']

        self.assertEqual(sorted(values), expected_values)

    def test_items(self):
        table = HashTable[str, str]()
        table['key1'] = 'value1'
        table['key2'] = 'value2'

        items = table.items()
        expected_items = [('key1', 'value1'), ('key2', 'value2')]

        self.assertEqual(sorted(items), expected_items)

    def test_keys(self):
        table = HashTable[str, str]()
        table['key1'] = 'value1'
        table['key2'] = 'value2'

        keys = table.keys()
        expected_keys = ['key1', 'key2']

        self.assertEqual(sorted(keys), expected_keys)

    def test_resize(self):
        table = HashTable[int, str]()

        for i in range(1000):
            table[i] = f'value_{i}'

        self.assertEqual(len(table), 1000)


if __name__ == '__main__':
    unittest.main()
