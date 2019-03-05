"""The quick_sort algorithm uses a pivot to effectively sort the array into a sorted side and unsorted side.
"""
"""The left index is set to zero and the right index is set to the last element in the array.
As long as the left index is less than the right, we know that we are in bounds.
We set the temporary x value to the partition function call which returns an integer value.
The quick_sort function is then called on the left side of the partition."""
def init_quick_sort(the_array):
    left = 0
    right = len(the_array) - 1
    if left < right:
        x = partition(the_array, left, right)
        quick_sort(the_array, left, x -1)

    return the_array

"""This quick_sort function is called recursively with the left and right index markers after the partition index is
created."""
def quick_sort(the_array, left, right):
    if left < right:
        x = partition(the_array, left, right)
        quick_sort(the_array, left, x - 1)
        quick_sort(the_array, x + 1, right)

"""The pivot index is set to the position of the array[right] index. I is then set to be equal to left - 1
A for loop is then started to run from the left index to the right index. if the array[j] is less than the pivot's value then
i is incremented and the array positions are swapped at the i and j indexes. """
def partition(the_array, left, right):
    pivot = the_array[right]
    i = left - 1
    for j in range(left, right):
        if the_array[j] <= pivot:
            i = i + 1
            the_array[i], the_array[j] = the_array[j], the_array[i]

#this makes sure that the last two elements get swapped.
    the_array[i+1], the_array[right] = the_array[right], the_array[i+1]
    return i + 1