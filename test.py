import unittest
from algo.quick_sort import Quicksort

class TestQuicksort(unittest.TestCase):

    def test_sort(self):
        arr = [1, 2, 56, 45, -9, 78, 11]
        manager = Quicksort()
        self.assertEqual(manager.quicksort(arr, "asc"), [-9, 1, 2, 11, 45, 56, 78])

    def test_desc_to_asc(self):
        arr = [78, 56, 45, 11, 2, 1, -9]
        manager = Quicksort()
        self.assertEqual(manager.quicksort(arr, "asc"), [-9, 1, 2, 11, 45, 56, 78])

    def test_desc_to_desc(self):
        arr = [78, 56, 45, 11, 2, 1, -9]
        manager = Quicksort()
        self.assertEqual(manager.quicksort(arr, "desc"), [78, 56, 45, 11, 2, 1, -9])

    def test_asc_to_desc(self):
        arr = [-9, 1, 2, 11, 45, 56, 78]
        manager = Quicksort()
        self.assertEqual(manager.quicksort(arr, "desc"), [78, 56, 45, 11, 2, 1, -9])

    def test_asc_to_asc(self):
        arr = [-9, 1, 2, 11, 45, 56, 78]
        manager = Quicksort()
        self.assertEqual(manager.quicksort(arr, "asc"), [-9, 1, 2, 11, 45, 56, 78])
