from math import floor


"""1. Find the middle point and divide the array in to
   2. Call merge_sort on left_array
   3. Call merge_sort on right_array
   4. Merge left and right array """

def merge_sort(test_array):

    if len(test_array) == 1:
        return
    else:
            middle = floor(len(test_array)/2)
            left_array = test_array[0: middle]
            right_array = test_array[middle: ]
            merge_sort(left_array)
            merge_sort(right_array)
            merge(left_array, right_array)

#         if left < right:
#            middle = floor(((len(test_array))/2))
#            merge_sort(test_array, left, middle)
#            merge_sort(test_array, (middle + 1), right)
#            merge(test_array, left, middle, right)


def merge(left_array, right_array):
    i = 0
    j = 0
    test_array = [None]
    total_length = len(left_array) + len(right_array)
    for k in range(0, total_length):
        if left_array[i] <= right_array[j]:
            test_array[k] = left_array[i]
            i = i + 1
        else:
            test_array[k] = right_array[j]
            j = j + 1

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