def quick_sort(the_array, left, right):

    if left < right:
        pivot = partition(the_array, left, right)
        quick_sort(the_array, left, pivot -1)
        quick_sort(the_array, pivot + 1, right)


def partition(the_array, left, right):
    temporary = the_array[right]
    i = left - 1
    for j in range(left, right):
        if the_array[j] <= temporary:
            i = i + 1
            the_array[i], the_array[j] = the_array[j], the_array[i]

    the_array[i+1], the_array[right] = the_array[right], the_array[i+1]
    return i + 1