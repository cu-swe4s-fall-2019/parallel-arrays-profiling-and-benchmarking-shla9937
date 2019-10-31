import unittest
import random
import string
import os
import hash_functions


class TestAsciiHashFunctions(unittest.TestCase):

    def test_accepts_string(self):
        key = 'hello'
        N = 1
        r = hash_functions.h_ascii(key, N)
        self.assertNotEqual(r, -1)

    def test_accepts_string_rand(self):
        N = 5
        for k in range(100):
            rand_int = random.randint(1, 1000)
            key = ''.join([random.choice(string.ascii_letters + string.digits)
                          for n in range(rand_int)])
            r = hash_functions.h_ascii(key, N)
            self.assertNotEqual(r, -1)

    def test_rejects_list(self):
        N = 5
        key = ['hello', 'goodbye']
        r = hash_functions.h_ascii(key, N)
        self.assertEqual(r, -1)

    def test_rejects_int(self):
        N = 5
        key = 54
        r = hash_functions.h_ascii(key, N)
        self.assertEqual(r, -1)

    def test_rejects_float(self):
        N = 5
        key = 54.6
        r = hash_functions.h_ascii(key, N)
        self.assertEqual(r, -1)

    def test_rejects_boolean(self):
        N = 5
        key = True
        r = hash_functions.h_ascii(key, N)
        self.assertEqual(r, -1)

    def test_hash_returns_ascii(self):
        N = 5
        key = 'hello'
        r = hash_functions.h_ascii(key, N)
        self.assertEqual(r, 2)


class TestRollingHashFunctions(unittest.TestCase):

    def test_roll_returns_correct_value(self):
        N = 5
        key = 'hello'
        r = hash_functions.h_rolling(key, N)
        self.assertEqual(r, 1)


if __name__ == '__main__':
    unittest.main()
