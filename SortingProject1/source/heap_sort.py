from math import floor

"""Class Heap is used to build an heap object with a root, heap_size, left and right child, and the array. """
class Heap:
    def __init__(self, the_array):
        self.array = the_array
        self.root = 0
        self.heap_size = 0
        self.left = None
        self.right = None

#method of the class to set the left child of the heap. This formula works because the heap is a balanced binary tree
# data structure If the left value is set to be greater than what the actual heap_size is, then
#I know that this node in the tree is a leaf so I set self.left = to None
    def left_child(self, i):
        self.left = (2 * i) + 1
        if self.left >= self.heap_size:
            return None
        else:
            return self.left

# method of the class to set the right child of the heap. This formula works because the heap is a balanced binary tree
# data structure. If the right value is set to be greater than what the actual heap_size is, then
# I know that this node in the tree is a leaf so I set self.right = to None
    def right_child(self, i):
        self.right = (2 * i) + 2
        if self.right >= self.heap_size:
            return None
        else:
            return self.right


"""The heap_sort algorithm
1st we check to make sure the array is not empty. If it is empty, we are finished. If the array is not empty, we will 
call the max heap function with the_heap object. The build_max_heap will call the max_heapify function. When the call
returns to heap_sort, we will begin at the end of the array and work our way backwards by making swaps so that the
largest elements float to the top of the heap. The max_heapify will be recursively called until the heap is sorted. 
This sorting algorithm probably gave me the most trouble out of the 6 that we had to implement. """
def heap_sort(the_array):
    if not the_array:
        return the_array

    the_heap = Heap(the_array)

    build_max_heap(the_heap)
    array_length = len(the_array) - 1
    for i in range(array_length, -1, -1):
        the_heap.array[0], the_heap.array[i] = the_heap.array[i], the_heap.array[0]
        the_heap.heap_size = the_heap.heap_size - 1
        max_heapify(the_heap, 0)

    return the_array


"""max_heapify sets the left and right child of the parent node that is passed in. If there is a left child, and if 
left is less than the_heap.heap_size and the array element at the left child position is greater than parent then the 
largest variable is set to the left child, else the largest is still the parent (i) that was passed in. We then check
the right child of the parent (i) if all conditions are met then largest is the right child. If largest is not == to 
the parent node then we swap the values at the largest index and the parent index. We then recursively call 
max_heapify upon itself and repeat the process."""
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


"""I set the heap size to the length of the array and I set the beginning range to the parent of the last leaf node.
I then begin calling max_heapify which will recursively call upon itself until the array is sorted."""
def build_max_heap(the_array):
    the_array.heap_size = len(the_array.array)
    beginning_range = floor(len(the_array.array) / 2) -1
    for i in range(beginning_range, -1, -1):
        max_heapify(the_array, i)



