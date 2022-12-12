import unittest
from merge_sorted_arrays import merge_sorted_arrays

class TestMergeSortedArrays(unittest.TestCase):
  def test_empty_input_arrays(self):
    self.assertEqual(merge_sorted_arrays([], []), [])

  def test_input_arrays_with_one_element_each(self):
    self.assertEqual(merge_sorted_arrays([1], [2]), [1, 2])
    self.assertEqual(merge_sorted_arrays([2], [1]), [1, 2])

  def test_input_arrays_with_multiple_elements(self):
    self.assertEqual(merge_sorted_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
    self.assertEqual(merge_sorted_arrays([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
    self.assertEqual(merge_sorted_arrays([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6])

  def test_input_arrays_with_repeated_elements(self):
    self.assertEqual(merge_sorted_arrays([1, 1, 2, 3], [1, 2, 2, 4]), [1, 1, 1, 2, 2, 2, 3, 4])
    self.assertEqual(merge_sorted_arrays([1, 2, 2, 4], [1, 1, 2, 3]), [1, 1, 1, 2, 2, 2, 3, 4])

  def test_input_arrays_with_different_lengths(self):
    self.assertEqual(merge_sorted_arrays([1, 2, 3], [4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
    self.assertEqual(merge_sorted_arrays([4, 5, 6, 7], [1, 2, 3]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == "__main__":
  unittest.main()
