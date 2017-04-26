"""
This calculator script is Part 3 of the Hackbright Prep functions exercise. Please 
complete the functions below. This first one is completed for you. Remember to 
write a sentence in your docstrings that describes what the function does. 

In further study, you'll be asked to complete the doctests as well! 
"""

#########################################################################
# This one has been completed for you
def add(num1, num2):
    """Returns the sum of two numbers.

    >>> add(7, 12)
    19
    >>> add(add(2,4), 1)
    7
    """
    sum = num1 + num2

    return sum

#########################################################################
# Complete all of the functions below

def subtract(num1, num2):

    sum = num1 - num2
    return sum


def multiply(num1, num2):

    sum = num1 * num2
    return sum



def divide(num1, num2):
    
    sum = num1 / num2
    return sum


def modulo(num1, num2):

    sum = num1 % num2
    return sum


def power(base, exponent):

    sum = base ** exponent
    return sum


def square(num1):

    sum = num1 ** 2
    return sum

#####################################################################
# Uncomment this code below when you get to further study
# This code will allow us to run our doctests

# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"