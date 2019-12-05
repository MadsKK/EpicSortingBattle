import unittest
import sorteringsAlgoritmer


class TestSortAlgorithm(unittest.TestCase):

    def setUp(self):
        self.testList = [9, 4, 6, 2, 5]

    def testInsertionSort(self):
        self.sortedList = sorteringsAlgoritmer.insertionSort(self.testList)
        self.assertEqual(self.sortedList, sorted(self.testList))

    def testBubbleSort(self):
        self.sortedList = sorteringsAlgoritmer.bubbleSort(self.testList)
        self.assertEqual(self.sortedList, sorted(self.testList))


if __name__ == '__main__':
    unittest.main()
