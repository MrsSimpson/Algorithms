# My implementation of an insertion sorting algorithm
"""If the array has more than one element in it, the outer for loop will begin with i starting at the second element
in the array. The outer for loop will run until the end of the array. The inner for loop will begin at the index behind
the outer for loop. and decrement by 1 until the 0 index of the array is reached. The index1 (left index) will be set
to the j counter. and the index2 (right index) will be set to the i value. If the left element is larger than the
right then the elements will be swapped. The inner range variable will be decremented by 1 and the inner for loop will
continue until the 0 index of the array is reached. When the inner for loop finishes, the outer loop will increment it's
counter by 1 and the process will repeat until all of the elements in the array have been sorted."""

def insertion_sort(test_array):
    array_len = len(test_array)
    if array_len > 1:
        for i in range(1, array_len):
            inner_range = i
            for j in range ((i-1), -1, -1):
                index1 = test_array[j]
                index2 = test_array[inner_range]
                if index1 > index2:
                    test_array[j], test_array[inner_range] = test_array[inner_range], test_array[j]
                inner_range = inner_range - 1

    return test_array


#Books implementation of insertion sort
def book_insertion_sort(test_array):
    array_length = len(test_array)
    if array_length != 0 or array_length != 1:
        for i in range(1, array_length):
            current = test_array[i]
            j = i - 1

            while j >= 0 and test_array[j] > current:
                test_array[j+1] = test_array[j]
                j = j - 1

            test_array[j + 1] = current

        return test_array