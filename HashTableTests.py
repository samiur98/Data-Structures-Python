import unittest
from HashTable import *
class HashTests1(unittest.TestCase):
    #Test Cases for HashTable1

    def test_is_empty(self):
        #Test Cases for the is_empty method.
        table = HashTable1()
        self.assertTrue(table.is_empty())
        table.insert("one", 1)
        self.assertFalse(table.is_empty())
        table.insert("two", 2)
        self.assertFalse(table.is_empty())
        table.delete("two")
        self.assertFalse(table.is_empty())
        table.delete("one")
        self.assertTrue(table.is_empty())

    def test_load_factor(self):
        #Test Cases for the load factor method.
        table = HashTable1()
        self.assertEqual(table.load_factor(), 0)
        table.insert("three", 3)
        self.assertEqual(table.load_factor(), 0.1)
        table.insert("four", 4)
        self.assertEqual(table.load_factor(), 0.2)
        table.insert("five", 5)
        self.assertEqual(table.load_factor(), 0.3)
        table.delete("five")
        self.assertEqual(table.load_factor(), 0.2)
        table.delete("four")
        self.assertEqual(table.load_factor(), 0.1)
        table.delete("three")
        self.assertEqual(table.load_factor(), 0)

    def test_search(self):
        #Test Cases for the search method.
        table = HashTable1()
        self.assertEqual(table.search("six"), None)
        table.insert("six", 6)
        self.assertEqual(table.search("six"), 6)
        self.assertEqual(table.search("seven"), None)
        table.insert("seven", 7)
        self.assertEqual(table.search("seven"), 7)
        self.assertEqual(table.search("eight"), None)
        table.insert("eight", 8)
        self.assertEqual(table.search("eight"), 8)
        self.assertEqual(table.search("nine"), None)
        table.delete("eight")
        self.assertEqual(table.search("eight"), None)
        table.delete("six")
        self.assertEqual(table.search("six"), None)
        table2 = HashTable1()
        self.assertEqual(table2.search("ten"), None)
        table2.insert("ten", 10)
        table2.insert("net", 100)
        table2.insert("etn", 1000)
        self.assertEqual(table2.search("ten"), 10)
        self.assertEqual(table2.search("net"), 100)
        self.assertEqual(table2.search("etn"), 1000)
        table2.delete("net")
        self.assertEqual(table2.search("ten"), 10)
        self.assertEqual(table2.search("net"), None)
        self.assertEqual(table2.search("etn"), 1000)

    def test_insert(self):
        #Test Cases for the insert method.
        table = HashTable1()
        self.assertTrue(table.is_empty())
        table.insert("eleven", 11)
        self.assertFalse(table.is_empty())
        table.insert("twelve", 12)
        table.insert("thirteen", 13)
        self.assertEqual(table.size, 3)
        self.assertEqual(table.table[3].key, "twelve")
        self.assertEqual(table.table[3].value, 12)
        self.assertEqual(table.table[7].key, "thirteen")
        self.assertEqual(table.table[7].value, 13)
        self.assertEqual(table.table[9].key, "eleven")
        self.assertEqual(table.table[9].value, 11)
        table.insert("a", 111)
        table.insert("b", 122)
        table.insert("c", 1222)
        table.insert("d", 545)
        self.assertEqual(table.size, 7)
        self.assertEqual(table.load_factor(), 0.7)
        self.assertEqual(len(table.table), 10)
        table.insert("e", 1998)
        self.assertEqual(table.size, 8)
        self.assertEqual(table.load_factor(), 0.4)
        self.assertEqual(len(table.table), 20)
        table2 = HashTable1()
        table2.insert("cat", 14)
        table2.insert("tac", 15)
        table2.insert("act", 16)
        self.assertEqual(table2.table[2].key, "cat")
        self.assertEqual(table2.table[2].value, 14)
        self.assertEqual(table2.table[3].key, "tac")
        self.assertEqual(table2.table[3].value, 15)
        self.assertEqual(table2.table[4].key, "act")
        self.assertEqual(table2.table[4].value, 16)

    def test_delete(self):
        #Test Cases for the delete method.
        table = HashTable1()
        table.insert("seventeen", 17)
        table.insert("eighteen", 18)
        table.insert("twentyone", 21)
        self.assertEqual(table.size, 3)
        self.assertEqual(table.table[1].flag, False)
        self.assertEqual(table.table[3].flag, False)
        self.assertEqual(table.table[5].flag, False)
        self.assertEqual(table.delete("seventeen"), True)
        self.assertEqual(table.delete("eighteen"), True)
        self.assertEqual(table.delete("nineteen"), False)
        self.assertEqual(table.delete("twenty"), False)
        self.assertEqual(table.delete("twentyone"), True)
        self.assertEqual(table.size, 0)
        self.assertEqual(table.table[1].key, None)
        self.assertEqual(table.table[1].value, None)
        self.assertEqual(table.table[1].flag, True)
        self.assertEqual(table.table[3].key, None)
        self.assertEqual(table.table[3].value, None)
        self.assertEqual(table.table[3].flag, True)
        self.assertEqual(table.table[5].key, None)
        self.assertEqual(table.table[5].value, None)
        self.assertEqual(table.table[5].flag, True)
        table2 = HashTable1()
        table2.insert("trex", 221)
        table2.insert("rext", 117)
        table2.insert("extr", 114)
        table2.insert("xtre", 120)
        self.assertEqual(table2.size, 4)
        self.assertEqual(table2.table[1].key, "trex")
        self.assertEqual(table2.table[1].value, 221)
        self.assertEqual(table2.table[1].flag, False)
        self.assertEqual(table2.table[2].key, "rext")
        self.assertEqual(table2.table[2].value, 117)
        self.assertEqual(table2.table[2].flag, False)
        self.assertEqual(table2.table[3].key, "extr")
        self.assertEqual(table2.table[3].value, 114)
        self.assertEqual(table2.table[3].flag, False)
        self.assertEqual(table2.table[4].key, "xtre")
        self.assertEqual(table2.table[4].value, 120)
        self.assertEqual(table2.table[4].flag, False)
        self.assertEqual(table2.delete("extr"), True)
        self.assertEqual(table2.size, 3)
        self.assertEqual(table2.delete("re"), False)
        self.assertEqual(table2.table[3].key, None)
        self.assertEqual(table2.table[3].value, None)
        self.assertEqual(table2.table[3].flag, True)
        self.assertEqual(table2.delete("rext"), True)
        self.assertEqual(table2.size, 2)
        self.assertEqual(table2.delete("er"), False)
        self.assertEqual(table2.table[2].key, None)
        self.assertEqual(table2.table[2].value, None)
        self.assertEqual(table2.table[2].flag, True)
        self.assertEqual(table2.delete("xtre"), True)
        self.assertEqual(table2.size, 1)
        self.assertEqual(table2.delete("red"), False)
        self.assertEqual(table2.table[4].key, None)
        self.assertEqual(table2.table[4].value, None)
        self.assertEqual(table2.table[4].flag, True)

class HashTests2(unittest.TestCase):
    #Test Cases for HashTable2

    def test_is_empty(self):
        #Test Cases for the is_empty method.
        table = HashTable2()
        self.assertTrue(table.is_empty())
        table.insert("one", 1)
        self.assertFalse(table.is_empty())
        table.insert("two", 2)
        self.assertFalse(table.is_empty())
        table.delete("two")
        self.assertFalse(table.is_empty())
        table.delete("one")
        self.assertTrue(table.is_empty())

    def test_load_factor(self):
        #Test Cases for the load factor method.
        table = HashTable2()
        self.assertEqual(table.load_factor(), 0)
        table.insert("three", 3)
        self.assertEqual(table.load_factor(), 0.1)
        table.insert("four", 4)
        self.assertEqual(table.load_factor(), 0.2)
        table.insert("five", 5)
        self.assertEqual(table.load_factor(), 0.3)
        table.delete("five")
        self.assertEqual(table.load_factor(), 0.2)
        table.delete("four")
        self.assertEqual(table.load_factor(), 0.1)
        table.delete("three")
        self.assertEqual(table.load_factor(), 0)

    def test_search(self):
        #Test Cases for the search method.
        table = HashTable2()
        self.assertEqual(table.search("six"), None)
        table.insert("six", 6)
        self.assertEqual(table.search("six"), 6)
        self.assertEqual(table.search("seven"), None)
        table.insert("seven", 7)
        self.assertEqual(table.search("seven"), 7)
        self.assertEqual(table.search("eight"), None)
        table.insert("eight", 8)
        self.assertEqual(table.search("eight"), 8)
        self.assertEqual(table.search("nine"), None)
        table.delete("eight")
        self.assertEqual(table.search("eight"), None)
        table.delete("six")
        self.assertEqual(table.search("six"), None)
        table2 = HashTable1()
        self.assertEqual(table2.search("ten"), None)
        table2.insert("ten", 10)
        table2.insert("net", 100)
        table2.insert("etn", 1000)
        self.assertEqual(table2.search("ten"), 10)
        self.assertEqual(table2.search("net"), 100)
        self.assertEqual(table2.search("etn"), 1000)
        table2.delete("net")
        self.assertEqual(table2.search("ten"), 10)
        self.assertEqual(table2.search("net"), None)
        self.assertEqual(table2.search("etn"), 1000)

    def test_insert(self):
        #Test Cases for the insert method.
        table = HashTable2()
        self.assertTrue(table.is_empty())
        table.insert("eleven", 11)
        self.assertFalse(table.is_empty())
        table.insert("twelve", 12)
        table.insert("thirteen", 13)
        self.assertEqual(table.size, 3)
        self.assertEqual(table.table[3].key, "twelve")
        self.assertEqual(table.table[3].value, 12)
        self.assertEqual(table.table[7].key, "thirteen")
        self.assertEqual(table.table[7].value, 13)
        self.assertEqual(table.table[9].key, "eleven")
        self.assertEqual(table.table[9].value, 11)
        table.insert("a", 111)
        table.insert("b", 122)
        table.insert("c", 1222)
        table.insert("d", 545)
        self.assertEqual(table.size, 7)
        self.assertEqual(table.load_factor(), 0.7)
        self.assertEqual(len(table.table), 10)
        table.insert("e", 1998)
        self.assertEqual(table.size, 8)
        self.assertEqual(table.load_factor(), 0.4)
        self.assertEqual(len(table.table), 20)
        table2 = HashTable2()
        table2.insert("cat", 14)
        table2.insert("tac", 15)
        table2.insert("act", 16)
        table2.insert("tca", 17)
        self.assertEqual(table2.table[2].key, "cat")
        self.assertEqual(table2.table[2].value, 14)
        self.assertEqual(table2.table[3].key, "tac")
        self.assertEqual(table2.table[3].value, 15)
        self.assertEqual(table2.table[6].key, "act")
        self.assertEqual(table2.table[6].value, 16)
        self.assertEqual(table2.table[1].key, "tca")
        self.assertEqual(table2.table[1].value, 17)

    def test_delete(self):
        #Test Cases for the delete method.
        table = HashTable2()
        table.insert("seventeen", 17)
        table.insert("eighteen", 18)
        table.insert("twentyone", 21)
        self.assertEqual(table.size, 3)
        self.assertEqual(table.table[1].flag, False)
        self.assertEqual(table.table[3].flag, False)
        self.assertEqual(table.table[5].flag, False)
        self.assertEqual(table.delete("seventeen"), True)
        self.assertEqual(table.delete("eighteen"), True)
        self.assertEqual(table.delete("nineteen"), False)
        self.assertEqual(table.delete("twenty"), False)
        self.assertEqual(table.delete("twentyone"), True)
        self.assertEqual(table.size, 0)
        self.assertEqual(table.table[1].key, None)
        self.assertEqual(table.table[1].value, None)
        self.assertEqual(table.table[1].flag, True)
        self.assertEqual(table.table[3].key, None)
        self.assertEqual(table.table[3].value, None)
        self.assertEqual(table.table[3].flag, True)
        self.assertEqual(table.table[5].key, None)
        self.assertEqual(table.table[5].value, None)
        self.assertEqual(table.table[5].flag, True)
        table2 = HashTable2()
        table2.insert("trex", 221)
        table2.insert("rext", 117)
        table2.insert("extr", 114)
        table2.insert("xtre", 120)
        self.assertEqual(table2.size, 4)
        self.assertEqual(table2.table[1].key, "trex")
        self.assertEqual(table2.table[1].value, 221)
        self.assertEqual(table2.table[1].flag, False)
        self.assertEqual(table2.table[2].key, "rext")
        self.assertEqual(table2.table[2].value, 117)
        self.assertEqual(table2.table[2].flag, False)
        self.assertEqual(table2.table[5].key, "extr")
        self.assertEqual(table2.table[5].value, 114)
        self.assertEqual(table2.table[5].flag, False)
        self.assertEqual(table2.table[0].key, "xtre")
        self.assertEqual(table2.table[0].value, 120)
        self.assertEqual(table2.table[0].flag, False)
        self.assertEqual(table2.delete("extr"), True)
        self.assertEqual(table2.size, 3)
        self.assertEqual(table2.delete("re"), False)
        self.assertEqual(table2.table[5].key, None)
        self.assertEqual(table2.table[5].value, None)
        self.assertEqual(table2.table[5].flag, True)
        self.assertEqual(table2.delete("rext"), True)
        self.assertEqual(table2.size, 2)
        self.assertEqual(table2.delete("er"), False)
        self.assertEqual(table2.table[2].key, None)
        self.assertEqual(table2.table[2].value, None)
        self.assertEqual(table2.table[2].flag, True)
        self.assertEqual(table2.delete("xtre"), True)
        self.assertEqual(table2.size, 1)
        self.assertEqual(table2.delete("red"), False)
        self.assertEqual(table2.table[0].key, None)
        self.assertEqual(table2.table[0].value, None)
        self.assertEqual(table2.table[0].flag, True)


class HashTests3(unittest.TestCase):
    #Test Cases for HashTable3

    def test_is_empty(self):
        #Test Cases for the is_empty method.
        table = HashTable3()
        self.assertTrue(table.is_empty())
        table.insert("one", 1)
        self.assertFalse(table.is_empty())
        table.insert("two", 2)
        self.assertFalse(table.is_empty())
        table.delete("two")
        self.assertFalse(table.is_empty())
        table.delete("one")
        self.assertTrue(table.is_empty())

    def test_search(self):
        #Test Cases for the search method.
        table = HashTable3()
        self.assertEqual(table.search("three"), None)
        table.insert("three", 3)
        self.assertEqual(table.search("three"), 3)
        self.assertEqual(table.search("four"), None)
        table.insert("four", 4)
        self.assertEqual(table.search("four"), 4)
        table.delete("three")
        table.delete("four")
        self.assertEqual(table.search("three"), None)
        self.assertEqual(table.search("four"), None)
        table.insert("three", 3)
        table.insert("four", 4)
        table.insert("ruof", 44)
        table.insert("rufo", 444)
        table.insert("hreet", 33)
        self.assertEqual(table.search("three"), 3)
        self.assertEqual(table.search("four"), 4)
        self.assertEqual(table.search("ruof"), 44)
        self.assertEqual(table.search("rufo"), 444)
        self.assertEqual(table.search("hreet"), 33)
        self.assertEqual(table.search("cats"), None)
        self.assertEqual(table.search("and"), None)
        self.assertEqual(table.search("dogs"), None)

    def test_insert(self):
        #Test Cases for the insert method.
        table = HashTable3()
        self.assertTrue(table.is_empty())
        table.insert("five", 5)
        table.insert("six", 6)
        table.insert("seven", 7)
        self.assertFalse(table.is_empty())
        self.assertEqual(table.table[0].key, "six")
        self.assertEqual(table.table[0].value, 6)
        self.assertEqual(table.table[5].key, "seven")
        self.assertEqual(table.table[5].value, 7)
        self.assertEqual(table.table[6].key, "five")
        self.assertEqual(table.table[6].value, 5)
        self.assertEqual(table.size, 3)
        self.assertEqual(table.table[0].next, None)
        self.assertEqual(table.table[5].next, None)
        table.insert("xis", 66)
        table.insert("sveen", 77)
        self.assertEqual(table.size, 5)
        self.assertEqual(table.table[0].next.key, "xis")
        self.assertEqual(table.table[0].next.value, 66)
        self.assertEqual(table.table[5].next.key, "sveen")
        self.assertEqual(table.table[5].next.value, 77)
        table.insert("vesen", 777)
        self.assertEqual(table.table[5].next.next.key, "vesen")
        self.assertEqual(table.table[5].next.next.value, 777)
        self.assertEqual(table.size, 6)

    def test_delete(self):
        #Test Cases for the delete method.
        table = HashTable3()
        table.insert("eight", 8)
        table.insert("nine", 9)
        table.insert("ten", 10)
        self.assertEqual(table.is_empty(), False)
        self.assertEqual(table.table[6].key, "nine")
        self.assertEqual(table.table[6].value, 9)
        self.assertEqual(table.table[7].key, "ten")
        self.assertEqual(table.table[7].value, 10)
        self.assertEqual(table.table[9].key, "eight")
        self.assertEqual(table.table[9].value, 8)
        self.assertEqual(table.size, 3)
        self.assertEqual(table.delete("nine"), True)
        self.assertEqual(table.size, 2)
        self.assertEqual(table.table[6].key, None)
        self.assertEqual(table.table[6].value, None)
        self.assertEqual(table.delete("ten"), True)
        self.assertEqual(table.size, 1)
        self.assertEqual(table.table[7].key, None)
        self.assertEqual(table.table[7].value, None)
        self.assertEqual(table.delete("foo"), False)
        self.assertEqual(table.delete("eight"), True)
        self.assertEqual(table.table[9].key, None)
        self.assertEqual(table.table[9].value, None)
        self.assertEqual(table.size, 0)
        self.assertEqual(table.delete("lamda"), False)
        table.insert("eight", 8)
        table.insert("nine", 9)
        table.insert("ten", 10)
        table.insert("net", 100)
        table.insert("etn", 1000)
        table.insert("inne", 99)
        self.assertEqual(table.delete("pow"), False)
        self.assertEqual(table.delete("inne"), True)
        self.assertEqual(table.table[6].next, None)
        self.assertEqual(table.size, 5)
        self.assertEqual(table.delete("etn"), True)
        self.assertEqual(table.table[7].next.next, None)
        self.assertEqual(table.size, 4)
        self.assertEqual(table.delete("net"), True)
        self.assertEqual(table.table[7].next, None)
        self.assertEqual(table.size, 3)


if __name__ == '__main__':
    unittest.main()
