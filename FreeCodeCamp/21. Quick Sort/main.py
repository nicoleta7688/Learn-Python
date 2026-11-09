import random

def pivot_first(array):
    return array[0]

def pivot_last(array):
    return array[-1]

def pivot_median_way(array):
    first = array[0]
    middle = array[len(array) // 2]
    last = array[-1]

    return first + middle + last - min(first, middle, last) - max(first, middle, last)
    # return sorted([first, middle, last])[1]    #another way

def pivot_randomize_way(array):
    return random.choice(array)


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = pivot_median_way(array)
    smaller_than_pivot = []
    equal_to_pivot = []
    bigger_than_pivot = []

    for e in array:
        if e < pivot:
            smaller_than_pivot.append(e)
        elif e > pivot:
            bigger_than_pivot.append(e)
        else:
            equal_to_pivot.append(e)
    
    sorted_array = []

    sorted_array.extend(quick_sort(smaller_than_pivot))
    sorted_array.extend(equal_to_pivot)
    sorted_array.extend(quick_sort(bigger_than_pivot))

    return sorted_array



print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))