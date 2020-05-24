def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    l = len(input_list)
    if l <= 1:
        return [-1, -1]

    input_freq = [0] * 10
    for num in input_list:
        input_freq[num] += 1

    a1 = []
    a2 = []
    first = 1
    if l % 2 != 0:
        first = 2
    for i in range(9, -1, -1):
        while input_freq[i]:
            if first:
                a1.append(str(i))
                first -= 1
            else:
                first += 1
                a2.append(str(i))
            input_freq[i] -= 1
    #print(a1, a2)
    return [int(''.join(a1)), int(''.join(a2))]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_function([[], [-1, -1]])
test_function([[0], [-1, -1]])
test_function([[0, 0], [0, 0]])
test_function([[0, 0, 1, 1, 5, 5], [510, 510]])