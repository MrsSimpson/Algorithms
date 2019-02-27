from source.selection_sort import selection_sort, my_selection_sort
from source.insertion_sort import insertion_sort, another_insertions_sort
from source.bubble_sort import bubble_sort
from source.merge_sort import initial_merge_sort
from source import heap_sort
from source import quick_sort


def init_arrays(array1, array2, array3, array4):
    array1 = []
    array2 = [20]
    array3 = [60, 30]
    array4 = [20, 30, 10, 80, 60, 50, 40, 70]

    return array1, array2, array3, array4

def main():
    array1 = []
    array2 = [20]
    array3 = [60, 30]
    array4 = [20, 30, 10, 80, 60, 50, 40, 70]


    selection_sort(array4)
    print(array4)

    array1, array2, array3, array4 = init_arrays(array1, array2, array3, array4)
    my_selection_sort(array3)
    print(array3)

    array1, array2, array3, array4 = init_arrays(array1, array2, array3, array4)
    insertion_sort(array3)
    print(array3)

    array1, array2, array3, array4 = init_arrays(array1, array2, array3, array4)
    another_insertions_sort(array4)
    print(array4)

    array1, array2, array3, array4 = init_arrays(array1, array2, array3, array4)
    bubble_sort(array4)
    print(array4)

    array1, array2, array3, array4 = init_arrays(array1, array2, array3, array4)
    initial_merge_sort(array2)
    print(array2)


main()