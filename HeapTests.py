import unittest
from Heaps import *
class HeapTests(unittest.TestCase):
    #Test Cases for the MinHeap Data Structure.

    def test_is_empty(self):
        #Test Cases for the is_empty method.
        heap = MinHeap()
        self.assertTrue(heap.is_empty())
        heap.insert(1)
        self.assertFalse(heap.is_empty())
        heap.insert(2)
        self.assertFalse(heap.is_empty())
        heap.delMin()
        self.assertFalse(heap.is_empty())
        heap.delMin()
        self.assertTrue(heap.is_empty())

    def test_perc_up(self):
        #Test Cases for the percUp method.
        heap = MinHeap()
        heap.elements.append(3)
        heap.elements.append(4)
        heap.elements.append(5)
        heap.size = 3
        self.assertEqual(heap.elements[1], 3)
        self.assertEqual(heap.elements[2], 4)
        self.assertEqual(heap.elements[3], 5)
        heap.percUp(2)
        heap.percUp(3)
        self.assertEqual(heap.elements[1], 3)
        self.assertEqual(heap.elements[2], 4)
        self.assertEqual(heap.elements[3], 5)
        heap2 = MinHeap()
        heap2.elements.append(5)
        heap2.elements.append(4)
        heap2.elements.append(3)
        heap2.size = 3
        self.assertEqual(heap2.elements[1], 5)
        self.assertEqual(heap2.elements[2], 4)
        self.assertEqual(heap2.elements[3], 3)
        heap2.percUp(3)
        self.assertEqual(heap2.elements[1], 3)
        self.assertEqual(heap2.elements[2], 4)
        self.assertEqual(heap2.elements[3], 5)
        heap3 = MinHeap()
        heap3.elements.append(4)
        heap3.elements.append(3)
        heap3.elements.append(5)
        heap3.size = 3
        self.assertEqual(heap3.elements[1], 4)
        self.assertEqual(heap3.elements[2], 3)
        self.assertEqual(heap3.elements[3], 5)
        heap3.percUp(2)
        self.assertEqual(heap3.elements[1], 3)
        self.assertEqual(heap3.elements[2], 4)
        self.assertEqual(heap3.elements[3], 5)
        heap4 = MinHeap()
        heap4.elements.append(29)
        heap4.elements.append(18)
        heap4.elements.append(17)
        heap4.elements.append(30)
        heap4.elements.append(41)
        heap4.elements.append(3)
        heap4.elements.append(44)
        heap4.size = 7
        self.assertEqual(heap4.elements[1], 29)
        self.assertEqual(heap4.elements[3], 17)
        self.assertEqual(heap4.elements[6], 3)
        heap4.percUp(6)
        self.assertEqual(heap4.elements[1], 3)
        self.assertEqual(heap4.elements[3], 29)
        self.assertEqual(heap4.elements[6], 17)

    def test_insert(self):
        #Tests Cases for the insert method.
        heap = MinHeap()
        self.assertTrue(heap.is_empty())
        heap.insert(5)
        self.assertFalse(heap.is_empty())
        self.assertEqual(heap.elements[1], 5)
        self.assertEqual(heap.size, 1)
        heap.insert(17)
        self.assertEqual(heap.elements[2], 17)
        self.assertEqual(heap.size, 2)
        heap.insert(18)
        self.assertEqual(heap.elements[3], 18)
        self.assertEqual(heap.size, 3)
        heap.insert(23)
        self.assertEqual(heap.elements[4], 23)
        self.assertEqual(heap.size, 4)
        heap.insert(3)
        self.assertEqual(heap.elements[1], 3)
        self.assertEqual(heap.elements[2], 5)
        self.assertEqual(heap.elements[5], 17)
        self.assertEqual(heap.size, 5)
        heap.insert(7)
        self.assertEqual(heap.elements[1], 3)
        self.assertEqual(heap.elements[3], 7)
        self.assertEqual(heap.elements[6], 18)

    def test_perc_down(self):
        #Test Cases for the perc_down method.
        heap = MinHeap()
        heap.elements.append(5)
        heap.elements.append(3)
        heap.elements.append(4)
        heap.size = 3
        self.assertEqual(heap.elements[1], 5)
        self.assertEqual(heap.elements[2], 3)
        self.assertEqual(heap.elements[3], 4)
        heap.percDown(1)
        self.assertEqual(heap.elements[1], 3)
        self.assertEqual(heap.elements[2], 5)
        self.assertEqual(heap.elements[3], 4)
        heap2 = MinHeap()
        heap2.elements.append(5)
        heap2.elements.append(4)
        heap2.elements.append(3)
        heap2.size = 3
        self.assertEqual(heap2.elements[1], 5)
        self.assertEqual(heap2.elements[2], 4)
        self.assertEqual(heap2.elements[3], 3)
        heap2.percDown(1)
        self.assertEqual(heap2.elements[1], 3)
        self.assertEqual(heap2.elements[2], 4)
        self.assertEqual(heap2.elements[3], 5)
        heap3 = MinHeap()
        heap3.elements.append(3)
        heap3.elements.append(4)
        heap3.elements.append(5)
        self.assertEqual(heap3.elements[1], 3)
        self.assertEqual(heap3.elements[2], 4)
        self.assertEqual(heap3.elements[3], 5)
        heap3.percDown(1)
        self.assertEqual(heap3.elements[1], 3)
        self.assertEqual(heap3.elements[2], 4)
        self.assertEqual(heap3.elements[3], 5)
        heap4 = MinHeap()
        heap4.elements.append(30)
        heap4.elements.append(33)
        heap4.elements.append(25)
        heap4.elements.append(43)
        heap4.elements.append(44)
        heap4.elements.append(28)
        heap4.elements.append(27)
        heap4.size = 7
        self.assertEqual(heap4.elements[1], 30)
        self.assertEqual(heap4.elements[3], 25)
        self.assertEqual(heap4.elements[7], 27)
        heap4.percDown(1)
        self.assertEqual(heap4.elements[1], 25)
        self.assertEqual(heap4.elements[3], 27)
        self.assertEqual(heap4.elements[7], 30)

    def test_del_min(self):
        #Test Cases for the delMin method.
        heap = MinHeap()
        self.assertTrue(heap.is_empty())
        value1 = heap.delMin()
        self.assertEqual(value1, None)
        heap.insert(7)
        value2 = heap.delMin()
        self.assertEqual(value2, 7)
        self.assertTrue(heap.is_empty())
        heap.insert(3)
        heap.insert(12)
        heap.insert(15)
        heap.insert(23)
        heap.insert(21)
        heap.insert(29)
        heap.insert(35)
        value3 = heap.delMin()
        self.assertFalse(heap.is_empty())
        self.assertEqual(heap.size, 6)
        self.assertEqual(value3, 3)
        self.assertEqual(heap.elements[1], 12)
        self.assertEqual(heap.elements[2], 21)
        self.assertEqual(heap.elements[3], 15)
        self.assertEqual(heap.elements[4], 23)
        self.assertEqual(heap.elements[5], 35)
        self.assertEqual(heap.elements[6], 29)
        value4 = heap.delMin()
        self.assertFalse(heap.is_empty())
        self.assertEqual(heap.size, 5)
        self.assertEqual(value4, 12)
        self.assertEqual(heap.elements[1], 15)
        self.assertEqual(heap.elements[2], 21)
        self.assertEqual(heap.elements[3], 29)
        self.assertEqual(heap.elements[4], 23)
        self.assertEqual(heap.elements[5], 35)
        value5 = heap.delMin()
        self.assertFalse(heap.is_empty())
        self.assertEqual(heap.size, 4)
        self.assertEqual(value5, 15)
        self.assertEqual(heap.elements[1], 21)
        self.assertEqual(heap.elements[2], 23)
        self.assertEqual(heap.elements[3], 29)
        self.assertEqual(heap.elements[4], 35)
        value6 = heap.delMin()
        self.assertFalse(heap.is_empty())
        self.assertEqual(heap.size, 3)
        self.assertEqual(value6, 21)
        self.assertEqual(heap.elements[1], 23)
        self.assertEqual(heap.elements[2], 35)
        self.assertEqual(heap.elements[3], 29)
        value7 = heap.delMin()
        self.assertFalse(heap.is_empty())
        self.assertEqual(heap.size, 2)
        self.assertEqual(value7, 23)
        self.assertEqual(heap.elements[1], 29)
        self.assertEqual(heap.elements[2], 35)
        value8 = heap.delMin()
        self.assertFalse(heap.is_empty())
        self.assertEqual(heap.size, 1)
        self.assertEqual(value8, 29)
        self.assertEqual(heap.elements[1], 35)
        value9 = heap.delMin()
        self.assertTrue(heap.is_empty())
        self.assertEqual(heap.size, 0)
        self.assertEqual(value9, 35)
        self.assertEqual(heap.delMin(), None)


if __name__ == '__main__':
    unittest.main()
