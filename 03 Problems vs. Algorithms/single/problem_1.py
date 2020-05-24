def sqrt(number):
    """
    Calculate the floored square root of a number
    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        warn = "Number must be non-negative, else returns None."
        print(warn)
        return None
        
    if number <= 1:
        return number
    
    if number ** 2 == number:
        return number
    low = 0
    high = number
    while low <= high:
        mid = (low + high) // 2
        if (mid**2 == number) or (mid**2 <= number and (mid+1)**2 > number):
            return mid
        elif (mid**2 > number):
            high = mid
        else:
            low = mid

print ("Pass" if  (3 == sqrt(9)) else "Fail")   # Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")   # Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")




print ("Pass" if  (2 == sqrt(4)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")

print ("Pass" if  (7 == sqrt(49)) else "Fail")
print ("Pass" if  (7 == sqrt(50)) else "Fail")
print ("Pass" if  (10 == sqrt(100)) else "Fail")
print ("Pass" if  (10 == sqrt(102)) else "Fail")
print (sqrt(-3)) 