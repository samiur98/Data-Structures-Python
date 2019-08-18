from Queue import *
import unittest
class QueueTests(unittest.TestCase):
    #Test Cases for the Queue Data Structure.

    def test_is_empty(self):
        #Test Cases for the is_empty method.
        queue = Queue(2)
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
        queue.enqueue(2)
        self.assertFalse(queue.is_empty())
        queue.dequeue()
        queue.dequeue()
        self.assertTrue(queue.is_empty())

    def test_is_full(self):
        #Test Cases for the is_full method.
        queue = Queue(2)
        self.assertFalse(queue.is_full())
        queue.enqueue(3)
        self.assertFalse(queue.is_full())
        queue.enqueue(4)
        self.assertTrue(queue.is_full())
        queue.dequeue()
        self.assertFalse(queue.is_full())
        queue.enqueue(5)
        self.assertTrue(queue.is_full())

    def test_peak(self):
        #Test Cases for the peak method.
        queue = Queue(2)
        self.assertEqual(queue.peek(), None)
        queue.enqueue(6)
        self.assertEqual(queue.peek(), 6)
        queue.enqueue(7)
        self.assertEqual(queue.peek(), 6)
        queue.dequeue()
        self.assertEqual(queue.peek(), 7)
        queue.dequeue()
        self.assertEqual(queue.peek(), None)

    def test_enqueue(self):
        #Test Cases for the enqueue method.
        queue = Queue(2)
        self.assertFalse(queue.is_full())
        self.assertTrue(queue.is_empty())
        self.assertEqual(None, queue.peek())
        queue.enqueue(8)
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.is_full())
        self.assertEqual(queue.peek(), 8)
        queue.enqueue(9)
        self.assertEqual(queue.peek(), 8)
        self.assertFalse(queue.is_empty())
        self.assertTrue(queue.is_full())
        self.assertEqual(queue.enqueue(10), None)
        queue.dequeue()
        self.assertEqual(queue.peek(), 9)
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.is_full())

    def test_dequeue(self):
        #Test Cases for the dequeue method.
        queue=Queue(3)
        self.assertFalse(queue.is_full())
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.dequeue(), None)
        queue.enqueue(11)
        queue.enqueue(12)
        queue.enqueue(13)
        self.assertTrue(queue.is_full())
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.peek(), 11)
        value_1=queue.dequeue()
        self.assertEqual(queue.peek(), 12)
        self.assertEqual(value_1, 11)
        value_2=queue.dequeue()
        self.assertEqual(queue.peek(), 13)
        self.assertEqual(value_2, 12)
        value_3=queue.dequeue()
        self.assertEqual(queue.peek(), None)
        self.assertEqual(value_3, 13)
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.dequeue(), None)

if __name__ == '__main__':
    unittest.main()
