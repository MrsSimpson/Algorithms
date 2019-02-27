#implementation 1
def selection_sort(test_array):
    for i in range(0, len(test_array) - 1):
        smallest = i

        for j in range(i+1, len(test_array)):
            if test_array[j] < test_array[smallest]:
                smallest = j

        if (smallest != i):
            test_array[i], test_array[smallest] = test_array[smallest], test_array[i]

    return test_array

#implementation 2 (my original)
def my_selection_sort(test_array):
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


