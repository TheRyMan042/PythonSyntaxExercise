#Ryan Hutchings
#Unit 21.1 - Python Syntax Exercise

def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    # YOUR CODE HERE
    total = 0 #adding all the numbers into this
    for number in nums:
        total += number
    return total

print("sum_nums returned", sum_nums([1, 2, 3, 4]))
print("sum_nums returned", sum_nums([4,7,8,12,-8,-2])) #Ans: 21
