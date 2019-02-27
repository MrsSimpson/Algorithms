from math import floor


"""1. Find the middle point and divide the array in to
   2. Call merge_sort on left_array
   3. Call merge_sort on right_array
   4. Merge left and right array """

def merge_sort(test_array, left, right):
    if test_array[0] == 1:
        return
    else:
        if left < right:

            middle = floor(len(test_array)/2)
            left_array = test_array[0: middle]
            right_array = test_array[middle-1: -1]
            merge_sort(left_array, left_array[0], left_array[-1])
            merge_sort(right_array, right_array[0], right_array[-1])

#         if left < right:
#            middle = floor(((len(test_array))/2))
#            merge_sort(test_array, left, middle)
#            merge_sort(test_array, (middle + 1), right)
#            merge(test_array, left, middle, right)


def merge(test_array, left, middle, right):
    total_length = len(test_array)
    left_array_len = (middle - left) + 1
    right_array_len = (right - middle)

    left_array = test_array[0:left_array_len+1]
    right_array = test_array[right_array_len: total_length+1]

    left_array.append(-1000)
    right_array.append(-1000)


    i = 1
    j = 1
    test_array = None
    for k in range(left, right):
        if left_array[i] <= right_array[j]:
            test_array[k] = left_array[i]
            i = i + 1
        else:
            test_array[k] = right_array[j]
            j = j + 1

