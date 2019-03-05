from math import floor

""" Begin the merge sort by setting the beginning and ending to the first and last elements of the array passed in. Then
    call merge sort recursively using the following steps. 
   1. Find the middle point and divide the array in to
   2. Call merge_sort on left_array
   3. Call merge_sort on right_array
   4. Merge left and right array """

#initial_merge_sort is the inital call function to begin the merge sort.
def init_merge_sort(test_array):
    beginning = 0
    ending = len(test_array) - 1
    merge_sort(test_array, beginning, ending)

    return test_array

#merge_sort is the recursive function that is called upon itself after the array is divided in two pieces after
#being split in the middle.
def merge_sort(test_array, beginning, ending):

    if beginning < ending:
        middle = floor((beginning + ending) / 2)
        merge_sort(test_array, beginning, middle) #the left side of the split
        merge_sort(test_array, middle+1, ending)  #the right side of the split

        # merge two arrays after the array initial array has been spit into many single element arrays
        merge(test_array, beginning, middle, ending)


"""The merge function takes the passed in array with the beginning index, the middle index, and the last index of 
the array. 1 is added to the middle index value. This is done so that the correct values are copied to the left_array
and right array due to the way python copies arrays. I set the i an j counters to 0 and append a sentinel value onto
the end of the left and right arrays. I then begin a for loop that will run from the beginning element to the last element
in the array. If the left_array[i] element is less than the right_array[j] element then the element in the original array
will be set equal to the element at the left_array[i] position. i will be incremented. If left_array[i] is not less
than or equal to right_array[j] then we know that the original array element at [k] should be replaced with the
right_array element at [j] and then the [j] counter will be incremented."""
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

