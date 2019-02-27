def bubble_sort(test_array):
    for i in range(0, len(test_array) - 1):
        for j in range(i+1, len(test_array)):
            if test_array[j] < test_array[i]:
                test_array[i], test_array[j] = test_array[j], test_array[i]

    return test_array