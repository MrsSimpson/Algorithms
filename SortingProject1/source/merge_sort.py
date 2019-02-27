from math import floor


"""1. Find the middle point and divide the array in to
   2. Call merge_sort on left_array
   3. Call merge_sort on right_array
   4. Merge left and right array """

def merge_sort(test_array, new_array):

    if len(test_array) == 1:
        return
    else:
            middle = floor(len(test_array)/2)
            left_array = test_array[0: middle]
            right_array = test_array[middle: ]
            merge_sort(left_array, new_array)
            merge_sort(right_array, new_array)
            merge(left_array, right_array, new_array)

    return new_array


def merge(left_array, right_array, new_array):
    i = 0
    j = 0

    total_length = len(left_array) + len(right_array)
    for k in range(0, len(left_array)):
        if left_array[i] <= right_array[j]:
            new_array.append(left_array[i])
            i = i + 1
        else:
            new_array.append(right_array[j])
            j = j + 1

    return new_array

"""
def merge(test_array, left, middle, right):
    total_length = len(test_array)
    left_array_len = (middle - left) + 1
    right_array_len = (right - middle)

    left_array = test_array[0:left_array_len+1]
    right_array = test_array[right_array_len: total_length+1]

    left_array.append(-1000)
    right_array.append(-1000)




"""