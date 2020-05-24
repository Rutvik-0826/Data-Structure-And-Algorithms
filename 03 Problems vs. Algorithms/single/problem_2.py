def rotated_array_search(input_list, number, mid=0):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    
    if input_list == []:
        return -1
    l = len(input_list)
    low = 0
    high = l
    while low <= high:
        pivot = (low+high) // 2
        #print('p', pivot)
        if input_list[0] < input_list[l-1] or pivot == l-1:
            pivot = 0
            break
        if input_list[pivot-1] > input_list[pivot]:
            break
        elif input_list[0] < input_list[pivot]:
            low = pivot
        elif input_list[0] > input_list[pivot]:
            high = pivot

    if input_list[pivot] <= number and input_list[l-1] >= number:
        low = pivot
        high = l
    else:
        low = 0
        high = pivot

    while low <= high:
        pivot = (low+high) // 2
        if input_list[pivot] == number:
            return pivot
        elif input_list[pivot] < number:
            low = pivot+1
        else:
            high = pivot-1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
        #print(rotated_array_search(input_list, number))

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 6, 7, 8], 10])
test_function([[], 7])
test_function([[7], 7])
test_function([[4], 7])
test_function([[4, 5], 7])
test_function([[6, 7], 7])
test_function([[6, 7, 8], 7])