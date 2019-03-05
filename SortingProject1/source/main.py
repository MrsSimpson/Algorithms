from source.selection_sort import selection_sort
from source.insertion_sort import insertion_sort
from source.bubble_sort import bubble_sort
from source.merge_sort import init_merge_sort
from source.heap_sort import heap_sort
from source.quick_sort import init_quick_sort

def main():

    print("Selection Sort")
    print(selection_sort([]))
    print(selection_sort([20]))
    print(selection_sort([60, 30]))
    print(selection_sort([20, 30, 10, 80, 60, 50, 40, 70]))

    print("\n Insertion Sort")
    print(insertion_sort([]))
    print(insertion_sort([20]))
    print(insertion_sort([60, 30]))
    print(insertion_sort([20, 30, 10, 80, 60, 50, 40, 70]))

    print("\n Bubble Sort")
    print(bubble_sort([]))
    print(bubble_sort([20]))
    print(bubble_sort([60, 30]))
    print(bubble_sort([20, 30, 10, 80, 60, 50, 40, 70]))

    print("\n Merge Sort")
    print(init_merge_sort([]))
    print(init_merge_sort([20]))
    print(init_merge_sort([60, 30]))
    print(init_merge_sort([20, 30, 10, 80, 60, 50, 40, 70]))

    print("\n Heap Sort")
    print(heap_sort([]))
    print(heap_sort([20]))
    print(heap_sort([60, 30]))
    print(heap_sort([20, 30, 10, 80, 60, 50, 40, 70]))

    print("\n Quick Sort")
    print(init_quick_sort([]))
    print(init_quick_sort([20]))
    print(init_quick_sort([60, 30]))
    print(init_quick_sort([20, 30, 10, 80, 60, 50, 40, 70]))

    exit()

main()

