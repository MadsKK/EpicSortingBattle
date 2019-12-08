import unittest
import sorteringsAlgoritmer


class TestSortAlgorithm(unittest.TestCase):

    def setUp(self):
        self.testList = [9, 4, 6, 2, 5, 4, 8, 7, 3, 4, 9, 1, 5, 4, 2, 6, 7, 8, 6,
                         4, 8, 1, 2, 6, 7, 3, 489, 4, 1, 568, 4, 1, 8, 4, 1, 348, 435156, 468]

    def testInsertionSort(self):
        self.sortedList = sorteringsAlgoritmer.insertionSort(self.testList)
        self.assertEqual(self.sortedList, sorted(self.testList))

    def testBubbleSort(self):
        self.sortedList = sorteringsAlgoritmer.bubbleSort(self.testList)
        self.assertEqual(self.sortedList, sorted(self.testList))


if __name__ == '__main__':
    unittest.main()
