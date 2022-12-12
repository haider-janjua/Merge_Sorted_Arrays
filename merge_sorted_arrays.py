import sys

def merge_sorted_arrays(arr1, arr2):
  # Create a new empty list to hold the combined and sorted elements of the input arrays
  combined = []

  # Create iterators for each array
  arr1_iter = iter(arr1)
  arr2_iter = iter(arr2)

  # Get the first element from each iterator
  arr1_elem = next(arr1_iter, None)
  arr2_elem = next(arr2_iter, None)

  # Repeat until at least one iterator is exhausted
  while arr1_elem is not None or arr2_elem is not None:
    # If one of the arrays is exhausted, append the remaining elements of the other array
    if arr1_elem is None:
      combined.append(arr2_elem)
      arr2_elem = next(arr2_iter, None)
    elif arr2_elem is None:
      combined.append(arr1_elem)
      arr1_elem = next(arr1_iter, None)
    # Otherwise, append the smaller of the two current elements, and advance the iterator of the array from which the element was taken
    elif arr1_elem <= arr2_elem:
      combined.append(arr1_elem)
      arr1_elem = next(arr1_iter, None)
    else:
      combined.append(arr2_elem)
      arr2_elem = next(arr2_iter, None)

  # Return the combined and sorted array
  return combined

if __name__ == "__main__":
  # Parse the input arrays from the command-line arguments
  if sys.argv[1] == "[]":
    arr1 = []
  else:
    arr1 = list(map(int, sys.argv[1][1:-1].split(",")))

  if sys.argv[2] == "[]":
    arr2 = []
  else:
    arr2 = list(map(int, sys.argv[2][1:-1].split(",")))

  # Combine and sort the arrays
  combined = sorted(merge_sorted_arrays(arr1, arr2))

  # Print the combined array
  print(combined)
