from math import floor


"""1. Find the middle point and divide the array in to
   2. Call merge_sort on left_array
   3. Call merge_sort on right_array
   4. Merge left and right array """

def initial_merge_sort(test_array):
    beginning = 0
    ending = len(test_array) - 1
    merge_sort(test_array, beginning, ending)

def merge_sort(test_array, beginning, ending):

    if beginning < ending:
        middle = floor((beginning + ending) / 2)
        merge_sort(test_array, beginning, middle)
        merge_sort(test_array, middle+1, ending)
        merge(test_array, beginning, middle, ending)



def merge(test_array, beginning, middle, ending):

    middle += 1
    left_array = test_array[beginning: middle]
    right_array = test_array[middle:ending+1]
    i = 0
    j = 0
    left_array.append(10000)
    right_array.append(10000)

    for k in range(beginning, ending + 1):
        if left_array[i] <= right_array[j]:
            test_array[k] = left_array[i]
            i += 1
        else:
            test_array[k] = right_array[j]
            j += 1
