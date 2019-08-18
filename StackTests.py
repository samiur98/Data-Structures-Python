import unittest
from Stack import *
class StackTests(unittest.TestCase):
    #Test Cases for the Stack Data Structure.

    def test_is_empty(self):
        #Test Cases for the is_empty method.
        stack = Stack(10)
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())
        stack.push(2)
        self.assertFalse(stack.is_empty())
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_is_full(self):
        #Test Cases for the is_full method.
        stack = Stack(2)
        self.assertFalse(stack.is_full())
        stack.push(3)
        self.assertFalse(stack.is_full())
        stack.push(4)
        self.assertTrue(stack.is_full())
        stack.pop()
        self.assertFalse(stack.is_full())
        stack.push(5)
        self.assertTrue(stack.is_full())

    def test_peek(self):
        #Test Cases for the peek method.
        stack = Stack(10)
        self.assertEqual(stack.peek(), None)
        stack.push(6)
        self.assertEqual(stack.peek(), 6)
        stack.push(7)
        self.assertEqual(stack.peek(), 7)
        stack.pop()
        self.assertEqual(stack.peek(), 6)
        stack.pop()
        self.assertEqual(stack.peek(), None)

    def test_push(self):
        #Test Cases for the push method.
        stack = Stack(2)
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.peek(), None)
        self.assertFalse(stack.is_full())
        stack.push(8)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.peek(), 8)
        self.assertFalse(stack.is_full())
        stack.push(9)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.peek(), 9)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.push(10), None)

    def test_pop(self):
        #Test Cases for the pop method.
        stack = Stack(2)
        self.assertEqual(stack.pop(), None)
        stack.push(11)
        stack.push(12)
        self.assertEqual(stack.pop(), 12)
        self.assertEqual(stack.pop(), 11)
        self.assertEqual(stack.pop(), None)


if __name__ == '__main__':
    unittest.main()
