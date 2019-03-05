from source.selection_sort import selection_sort, my_selection_sort
from source.insertion_sort import insertion_sort, another_insertions_sort
from source.bubble_sort import bubble_sort
from source.merge_sort import initial_merge_sort
from source.heap_sort import Heap, heapsort
from source.quick_sort import quick_sort


def init_arrays():
    array1 = []
    array2 = [20]
    array3 = [60, 30]
    array4 = [20, 30, 10, 80, 60, 50, 40, 70]

    return array1, array2, array3, array4

def main():

    array1, array2, array3, array4 = init_arrays()
    selection_sort(array4)
    print(array4)

    array1, array2, array3, array4 = init_arrays()
    my_selection_sort(array2)
    print(array2)

    array1, array2, array3, array4 = init_arrays()
    insertion_sort(array3)
    print(array3)

    array1, array2, array3, array4 = init_arrays()
    another_insertions_sort(array4)
    print(array4)

    array1, array2, array3, array4 = init_arrays()
    bubble_sort(array4)
    print(array4)

    array1, array2, array3, array4 = init_arrays()
    initial_merge_sort(array4)
    print(array4)

    array1, array2, array3, array4 = init_arrays()
    the_heap = Heap(array4)
    heapsort(the_heap, array4)
    print(the_heap.array)

    array1, array2, array3, array4 = init_arrays()
    quick_sort(array4, 0, len(array4) - 1)
    print(array4)

    
main()