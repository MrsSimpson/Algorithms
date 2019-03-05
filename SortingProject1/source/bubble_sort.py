"""The bubble sort algorithm simply compares side by side elements using a nested for loop. This process causes the
larger elements to "sink" and the "smaller" elements to rise in terms of the array index position. My version of bubble
sort begins at the 0 index of the array with the outer for loop and will continue to the next to last element of the
array. The inner for loop begins at the element beside the i index element and proceeds to the last element of the
array. If the right element of the array is less than the right element then swap the values. After the inner for loop
runs through all of the elements, the outer for loop will increment it's counter and the process will repeat until the
array is sorted from least to greatest."""
def bubble_sort(test_array):
    for i in range(0, len(test_array) - 1):
        for j in range(i+1, len(test_array)):
            if test_array[j] < test_array[i]:
                test_array[i], test_array[j] = test_array[j], test_array[i]

    return test_array
