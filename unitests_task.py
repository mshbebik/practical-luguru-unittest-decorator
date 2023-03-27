import unittest


def main(a):
    list = []
    list = a.split()
    return list


class TestMain(unittest.TestCase):
    def test_no_root(self):
       res = main("It is me your tiny decorator")
       self.assertEqual(len(res), 6)

if __name__ == '__main__':
    unittest.main()