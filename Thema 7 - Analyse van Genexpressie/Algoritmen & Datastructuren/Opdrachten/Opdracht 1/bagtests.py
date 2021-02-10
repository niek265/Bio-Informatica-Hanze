'''Tests for classes in module bag'''

import unittest
import bag

ITEMS = [0, 1, 2, 3, 4, 5, 'a', 'aap']

class BagTestCase(unittest.TestCase):
    '''Tests for bag.Bag'''


    def setUp(self):
        '''create a Bag to use in all  tests'''
        self.bag = bag.Bag()
        for item in ITEMS:
            self.bag.add_item(item)

    def test_add_items(self):
        '''test if items are correctly added'''
        self.assertListEqual(ITEMS, self.bag.items)

    def test_add_double_item(self):
        '''tests if a duplicate can be added'''
        self.bag.add_item('noot')
        self.bag.add_item('noot')
        count = 0
        for i in self.bag.items:
            if i == 'noot':
                count += 1
        self.assertEqual(count, 2)

    def test_get_item(self):
        '''tests get_item'''
        #TODO test for randomness
        item = self.bag.get_item()
        self.assertIn(item, ITEMS)
        self.assertListEqual(ITEMS, self.bag.items)

    def test_remove_item(self):
        '''tests the remove method'''
        self.bag.remove_item('aap')
        self.assertNotIn('aap', self.bag.items)

        self.bag.add_item('a')
        self.bag.remove_item('a')
        self.assertIn('a', self.bag.items)

def add_tests():
    '''indicate tests to be run'''
    suite = unittest.TestSuite()
    suite.addTest(BagTestCase('test_add_items'))
    suite.addTest(BagTestCase('test_add_double_item'))
    suite.addTest(BagTestCase('test_get_item'))
    suite.addTest(BagTestCase('test_remove_item'))
    return suite

if __name__ == '__main__':
    RUNNER = unittest.TextTestRunner()
    RUNNER.run(add_tests())
