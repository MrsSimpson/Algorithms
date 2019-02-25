def main():

    test_array1 = []
    test_array2 = [60, 30]
    test_array3 = [20, 30, 10, 80, 60, 50, 40, 70]

    root_element = test_array3[0]
    test_array = insertion_sort(test_array3)
    print(test_array3)

    test_array3 = [20, 30, 10, 80, 60, 50, 40, 70]
    test_array = insertion_sort2(test_array3)
    print(test_array3)


def insertion_sort(test_array):
    array_length = len(test_array)
    if test_array != None and test_array != 1:
        for j in range(1, array_length):
            key = test_array[j]
            i = j -1
            while i >= 0 and test_array[i] > key:
                test_array[i+1] = test_array[i]
                i = i - 1

            test_array[i + 1] = key

    return test_array
#
def insertion_sort2(test_array):
    array_length = len(test_array)
    if array_length != 0 or array_length != 1:
        for i in range(1, array_length):
            current = test_array[i]
            j = i - 1

            while j >= 0 and test_array[j] > current:
                test_array[j+1] = test_array[j]
                j = j - 1

            test_array[j + 1] = current

        return test_array

main()