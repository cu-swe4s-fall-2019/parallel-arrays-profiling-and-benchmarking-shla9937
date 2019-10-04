import unittest
import random
import plot_gtex


class TestPlotGtex(unittest.TestCase):

    def test_linear_search_easy(self):
        key = 'blue'
        L = ['red', 'blue', 'yellow']
        r = plot_gtex.linear_search(key, L)
        self.assertEqual(r, 1)

    def test_linear_search_easy_not_in_list(self):
        key = 'green'
        L = ['red', 'blue', 'yellow']
        r = plot_gtex.linear_search(key, L)
        self.assertEqual(r, -1)

    def test_linear_search_rand(self):
        for k in range(100):
            rand_int = random.randint(1, 1000)
            rand_idx = random.randint(1, 99)
            key = rand_int
            L = []
            for i in range(100):
                rand_int_for_list = random.randint(1, 1000)
                if rand_int_for_list != rand_int:
                    L.append(rand_int_for_list)
                else:
                    continue
            L = list(dict.fromkeys(L))
            rand_idx = random.randint(1, len(L)-1)
            L[rand_idx] = rand_int
            r = plot_gtex.linear_search(key, L)
            self.assertEqual(r, rand_idx)

    def test_linear_search_rand_not_in_list(self):
        for k in range(100):
            rand_int = random.randint(1001, 2001)
            key = rand_int
            L = []
            for i in range(100):
                rand_int_for_list = random.randint(1, 1000)
                if rand_int_for_list != rand_int:
                    L.append(rand_int_for_list)
                else:
                    continue
            L = list(dict.fromkeys(L))
            rand_idx = random.randint(1, len(L)-1)
            r = plot_gtex.linear_search(key, L)
            self.assertEqual(r, -1)

    def test_binary_search_easy(self):
        key = 'blue'
        L = ['red', 'orange', 'blue', 'yellow']
        L.sort()
        r = plot_gtex.binary_search(key, L)
        self.assertEqual(r, 0)

    def test_binary_search_easy_not_in_list(self):
        key = 'green'
        L = ['red', 'blue', 'orange', 'yellow']
        L.sort()
        r = plot_gtex.binary_search(key, L)
        self.assertEqual(r, -1)

    def test_binary_search_rand(self):
        for k in range(100):
            rand_int = random.randint(1, 1000)
            key = rand_int
            L = []
            for i in range(100):
                rand_int_for_list = random.randint(1, 1000)
                if rand_int_for_list != rand_int:
                    L.append(rand_int_for_list)
                else:
                    continue
            L = list(dict.fromkeys(L))
            L.sort()
            idx = 0
            for j in L:
                if j == key or j > key:
                    break
                else:
                    idx += 1
            if key > L[-1]:
                idx = len(L)-1
            L[idx] = key
            r = plot_gtex.binary_search(key, L)
            self.assertEqual(r, idx)

    def test_binary_search_rand_not_in_list(self):
        for k in range(100):
            rand_int = random.randint(1, 1000)
            key = rand_int
            L = []
            for i in range(100):
                rand_int_for_list = random.randint(1, 1000)
                if rand_int_for_list != rand_int:
                    L.append(rand_int_for_list)
                else:
                    continue
            L = list(dict.fromkeys(L))
            L.sort()
            idx = 0
            for j in L:
                if j == key or j > key:
                    break
                else:
                    idx += 1
            r = plot_gtex.binary_search(key, L)
            self.assertEqual(r, -1)

    def test_nested_binary_search_easy(self):
        key = 'blue'
        L = [['red', 'green'], ['orange', 'pink'], ['blue', 'white'],
             ['yellow', 'black']]
        L.sort()
        r = plot_gtex.nested_binary_search(key, L)
        self.assertEqual(r, 'white')

    def test_nested_binary_search_easy_not_in_list(self):
        key = 'purple'
        L = [['red', 'green'], ['orange', 'pink'], ['blue', 'white'],
             ['yellow', 'black']]
        L.sort()
        r = plot_gtex.nested_binary_search(key, L)
        self.assertEqual(r, -1)

    def test_nested_binary_search_rand(self):
        for k in range(100):
            rand_int = random.randint(1, 1000)
            rand_int1 = random.randint(1, 1000)
            key = rand_int
            L = []
            M = []
            for i in range(100):
                for k in range(2):
                    rand_int_for_list = random.randint(1, 1000)
                    if rand_int_for_list != rand_int:
                        M.append(rand_int_for_list)
                    else:
                        continue
                L.append(M)
                M = []
            L.sort(key=lambda x: x[0])
            idx = 0
            for j in L:
                if j[0] == key or j[0] > key:
                    break
                else:
                    idx += 1
            if key > L[-1][0]:
                idx = len(L)-1
            L[idx] = [key, rand_int1]
            r = plot_gtex.nested_binary_search(key, L)
            self.assertEqual(r, rand_int1)

    def test_nested_binary_search_rand_not_in_list(self):
        for k in range(100):
            rand_int = random.randint(1, 1000)
            rand_int1 = random.randint(1, 1000)
            key = rand_int
            L = []
            M = []
            for i in range(100):
                for k in range(2):
                    rand_int_for_list = random.randint(1, 1000)
                    if rand_int_for_list != rand_int:
                        M.append(rand_int_for_list)
                    else:
                        continue
                L.append(M)
                M = []
            L.sort(key=lambda x: x[0])
            idx = 0
            for j in L:
                if j[0] == key or j[0] > key:
                    break
                else:
                    idx += 1
            r = plot_gtex.nested_binary_search(key, L)
            self.assertEqual(r, -1)


if __name__ == '__main__':
    unittest.main()
