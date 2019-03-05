#implementation 2 (my original)
"""my_selection_sort algorithm takes an array as a 1D array as an argument. The length of the
array is stored and then the smallest index is set to the first element in the array by
default. If the array length is equal to 0 or 1, the for loops will be skipped over and the
program will return to main. If the array has more than 1 element in it, the algorithm will drop
into the outer for loop which runs until the next to last element. The smallest variable is set
to the counter for the outer loop. We then drop into the inner for loop. The j index will be set
to 1 + i so that we are looking at 1 element ahead of the outer loops index. If the array[j] element is
smaller than the smallest element, then the smallest index is now set to the j counter.
After the remainder of the array is iterated through, I have an if statement to check and make sure
that the smallest variable is not the same as the array[i] index. If it is not, the values in the
array will be swapped in place. If they are the same, the counter for i will increment and the
process will repeat by comparing the next index with the rest of the elements in the array looking for the smallest
value to place at the new i index."""
def selection_sort(test_array):
    array_length = len(test_array)
    smallest_index = 0
    if array_length != 0 and array_length != 1:
        for i in range(0, array_length - 1):
            smallest = test_array[i]

            for j in range((i+1), array_length):
                if test_array[j] < smallest:
                    smallest = test_array[j]
                    smallest_index = j

            if smallest != test_array[i]:
                test_array[smallest_index], test_array[i] = test_array[i], test_array[smallest_index]

    return test_array


