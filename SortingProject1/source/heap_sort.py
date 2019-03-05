from math import floor


class Heap:
    def __init__(self, the_array):
        self.array = the_array
        self.root = 0
        self.heap_size = 0

        self.parent = None
        self.left = None
        self.right = None

    def the_parent(self, i):
        self.parent = floor((i - 1) / 2)
        return self.parent

    def left_child(self, i):
        self.left = (2 * i) + 1
        if self.left >= self.heap_size:
            return None
        else:
            return self.left

    def right_child(self, i):
        self.right = (2 * i) + 2
        if self.right >= self.heap_size:
            return None
        else:
            return self.right

def max_heapify(the_heap, i):
    left = the_heap.left_child(i)
    right = the_heap.right_child(i)

    if left != None and left <= the_heap.heap_size and the_heap.array[left] > the_heap.array[i]:
        largest = left

    else:
        largest = i

    if right != None and right <= the_heap.heap_size and the_heap.array[right] > the_heap.array[largest]:
        largest = right

    if largest != i:
        the_heap.array[i], the_heap.array[largest] =  the_heap.array[largest], the_heap.array[i]
        max_heapify(the_heap, largest)

def build_max_heap(the_array):
    the_array.heap_size = len(the_array.array)
    beginning_range = floor(len(the_array.array) / 2) -1
    for i in range(beginning_range, -1, -1):
        max_heapify(the_array, i)

def heapsort(the_heap, the_array):
    if not the_array:
        return

    build_max_heap(the_heap)
    array_length = len(the_array) - 1
    for i in range(array_length, -1, -1):
        the_heap.array[0], the_heap.array[i] = the_heap.array[i], the_heap.array[0]
        the_heap.heap_size = the_heap.heap_size - 1
        max_heapify(the_heap, 0)


