from source.selection_sort import selection_sort, my_selection_sort
from source.insertion_sort import insertion_sort, another_insertions_sort
from source.bubble_sort import bubble_sort
from source.merge_sort import merge_sort, merge
from source import heap_sort
from source import quick_sort


def main():

    test_array1 = []
    test_array2 = [60, 30]
    test_array3 = [20, 30, 10, 80, 60, 50, 40, 70]


    selection_sort(test_array3)
    print(test_array3)

    test_array3 = [20, 30, 10, 80, 60, 50, 40, 70]
    my_selection_sort(test_array3)
    print(test_array3)

    insertion_sort(test_array3)
    print(test_array3)

    test_array3 = [20, 30, 10, 80, 60, 50, 40, 70]
    another_insertions_sort(test_array3)
    print(test_array3)

    test_array3 = [20, 30, 10, 80, 60, 50, 40, 70]
    bubble_sort(test_array3)
    print(test_array3)

    test_array3 = [20, 30, 10, 80, 60, 50, 40, 70]
    left = test_array3[0]
    right = test_array3[-1]
    merge_sort(test_array3, left, right)
    print(test_array3)


main()