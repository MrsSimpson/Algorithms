#Books implementation of insertion sort
def insertion_sort(test_array):
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


""" My implementation of an insertion sorting algorithm"""
def another_insertions_sort(test_array):
    array_len = len(test_array)
    if test_array != None and test_array != 1:
        for i in range(1, array_len):
            index2 = test_array[i]
            inner_range = i
            for j in range ((i-1), -1, -1):
                index1 = test_array[j]
                index2 = test_array[inner_range]
                if index1 > index2:
                    test_array[j], test_array[inner_range] = test_array[inner_range], test_array[j]
                inner_range = inner_range - 1