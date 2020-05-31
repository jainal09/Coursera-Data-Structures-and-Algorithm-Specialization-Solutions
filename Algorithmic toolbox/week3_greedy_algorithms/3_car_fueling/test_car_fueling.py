import unittest
from .car_fueling import compute_min_refills

class MyTestCase(unittest.TestCase):
    def test_compute_min_refills(self):
        result = compute_min_refills(
            1000, 1000, [100, 200, 300, 400]
        )
        print(result)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
