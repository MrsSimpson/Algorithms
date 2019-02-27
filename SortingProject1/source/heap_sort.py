from math import floor

def parent(i):
    return floor(i / 2)

def left(i):
    return 2*i

def right(i):
    return (2 * i) + 1

def max_heapify(the_array, i):
    left_child = left(i)
    right_child = right(i)

    if left_child <= the_array.heap_size and the_array[left_child] > the_array[right_child]:
        largest = left_child

    else:
        largest = i

    if right_child <= the_array.heap_size and the_array[right_child] > the_array[largest]:
        largest = right_child

    if largest != i:
        the_array[i], the_array[largest] =  the_array[largest], the_array[i]
        max_heapify(the_array, largest)

def build_max_heap(the_array):
    Heap.heap_size = len(the_array)
    for i in range(floor(len(the_array)/2), 0):
        max_heapify(the_array, i)

def heapsort(the_array):
    build_max_heap(the_array)
    for i in range(len(the_array), 1, -1):
        the_array[0], the_array[i] = the_array[i], the_array[0]
        max_heapify(the_array, 0)

class Heap:
    def __init__(self, the_array):
        self.heap_size = 0
