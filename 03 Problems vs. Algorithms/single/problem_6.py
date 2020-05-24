def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return
    #       maximum         minimum
    ans = [-float('inf'), float('inf')]
    for num in ints:
        if num > ans[0]:
            ans[0] = num
        if num < ans[1]:
            ans[1] = num
    return (ans[1], ans[0])

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max_by_sorting(l)) else "Fail")
print ("Pass" if ((0, 0) == get_min_max_by_sorting([0])) else "Fail")
print ("Pass" if (None == get_min_max_by_sorting([])) else "Fail")
print ("Pass" if ((1, 0) == get_min_max_by_sorting([1, 0])) else "Fail")
print ("Pass" if ((0, 9) == get_min_max_by_sorting([5, 3, 2, 1, 9, 0, 7])) else "Fail")
print ("Pass" if ((-2, 2) == get_min_max_by_sorting([-2, -1, 0, 1, 2])) else "Fail")
print ("Pass" if ((5, 5) == get_min_max_by_sorting([5])) else "Fail")