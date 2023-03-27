import unittest


# Якщо вказанне число 'a' є простим то кінцем функції буде True, інакше False
def main (a):
  for b in range(2, a):
    if (a % b) == 0:
        print("Це число не є простим")
        return False
    else:
        print("Це число є простим")
        return True  


class TestMain(unittest.TestCase):
    def test_no_root(self):
       res = main(11)
       self.assertEqual(res, True)

if __name__ == '__main__':
    unittest.main()




