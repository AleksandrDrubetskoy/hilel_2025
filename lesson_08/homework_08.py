def sum_elements(list_with_string_elements):
    '''
    This function returns the list with sums of numbers in elements of list.
    :param list_with_string_elements: the list with incoming values
    :return: list with sums of elements in the list_int_num_elements
    '''
    try:
        result = []
        for string_element in list_with_string_elements:
            inner_sum = sum([int(el) for el in string_element.split(',')])
            result.append(inner_sum)
        return result
    except ValueError:
        print("Не можу це зробити!")
        print("Value Error")

list_strings = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
print("_"*33)
print("Example 1")
print(sum_elements(list_strings))
print("_"*33)
list_strings = ['1,2,3,4', '1,2,3,4,50', '1,2,3']
print("Example 2")
print(sum_elements(list_strings))
print("_"*33)