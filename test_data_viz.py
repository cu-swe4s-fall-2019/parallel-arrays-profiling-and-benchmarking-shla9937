import unittest
import random
import os
import data_viz


class TestDataViz(unittest.TestCase):

    def test_takes_list(self):
        L = [[1, 2, 3], [2, 2, 2], [3, 1, 2]]
        ticks = [1, 2, 3]
        r = data_viz.boxplot(L, 'test_outputfile.png', 'T', 'x', 'y', ticks)
        path = 'test_outputfile.png'
        isFile = os.path.isfile(path)
        self.assertTrue(isFile)
        os.remove('test_outputfile.png')

    def test_takes_rand_list(self):
        L = []
        M = []
        for i in range(10):
            for j in range(10):
                rand_int = random.randint(1, 10)
                M.append(rand_int)
                L.append(M)
            M = []
        ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        r = data_viz.boxplot(L, 'test_outputfile_rand.png', 'T', 'x', 'y',
                             ticks)
        path = 'test_outputfile_rand.png'
        isFile = os.path.isfile(path)
        self.assertTrue(isFile)
        os.remove('test_outputfile_rand.png')

    def test_skips_improper_lists(self):
        ticks = [1, 2, 3]
        L = [[1, 2, 3], ['red', 'blue', 'yellow'], [4, 2, 2]]
        r = data_viz.boxplot(L, 'test_outputfile_improper.png', 'T', 'x', 'y',
                             ticks)
        path = 'test_outputfile_improper.png'
        isFile = os.path.isfile(path)
        self.assertTrue(isFile)
        os.remove('test_outputfile_improper.png')


if __name__ == '__main__':
    unittest.main()
