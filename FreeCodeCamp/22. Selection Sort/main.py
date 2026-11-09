def selection_sort(array):

    sorted_index = 0

    while sorted_index < (len(array) - 1):
        min_element_index = sorted_index

        #search minimum element from the list
        for index, element in enumerate(array[sorted_index:], sorted_index):
            if element < array[min_element_index]:
                min_element_index = index

        #swap elements in place
        if sorted_index != min_element_index:
            array[sorted_index], array[min_element_index] = array[min_element_index], array[sorted_index]

        # print(f'arr[{sorted_index}] = {array[sorted_index]}, arr[{min_element_index}] = {array[min_element_index]}')
        # print(array)

        sorted_index += 1

    return array

arr = [5, 16, 99, 12, 567, 23, 15, 72, 3]
print(selection_sort(arr))