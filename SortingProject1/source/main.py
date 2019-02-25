def main():

    test_array1 = []
    test_array2 = [60, 30]
    test_array3 = [20, 30, 10, 80, 60, 50, 40, 70]


    selection_sort(test_array2)
    print(test_array2)
    insertion_sort(test_array3)
    print(test_array3)
    test_array3 = [20, 30, 10, 80, 60, 50, 40, 70]
    bubble_sort(test_array3)
    print(test_array3)

#
def selection_sort(test_array):
    for i in range(0, len(test_array)):
        smallest = i

        for j in range(i+1, len(test_array)):
            if test_array[j] < test_array[smallest]:
                smallest = j

        if (smallest != i):
            test_array[i], test_array[smallest] = test_array[smallest], test_array[i]

    return test_array

#Finished
def insertion_sort(test_array):
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

def bubble_sort(test_array):
    for i in range(0, len(test_array) - 1):
        for j in range(i+1, len(test_array)):
            if test_array[j] < test_array[i]:
                test_array[i], test_array[j] = test_array[j], test_array[i]

    return test_array


main()