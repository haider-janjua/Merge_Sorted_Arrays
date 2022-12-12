### Introduction ###

# Python script to combine two sorted arrays into a singular sorted array. 

### Python Script Usage ###

# Invoke from the command line with 2 sorted arrays as the arguments
    # python3 merge_sorted_arrays.py "[1, 2, 7, 9]" "[3, 6, 8]"
        # > [1, 2, 3, 6, 7, 8, 9]

### Unit Testing ###

# Invoke from the command line with the following command:
    # python3 -m unittest test_merge_sorted_arrays -v
        # > ... Ran 5 tests in 0.000s

### Docker ###

# To build the image, run the following command:
    # docker build -t merge-sorted-arrays .

# To run the image and pass in the input arrays, use the following command:
    # docker run merge-sorted-arrays "[1, 2, 7, 9]" "[3, 6, 8]"
        # > [1, 2, 3, 6, 7, 8, 9]
