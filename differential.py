from sympy import *

# create a function to compute n levels of differentiation and then return the result if the function returns 0 until the nth level of differentiation store each level of differentiation in a list
def diff(f, x, n):
    # create a list to store the levels of differentiation
    diff_list = []
    # create a variable to store the result of the nth level of differentiation
    result = 0
    # create a for loop to compute the nth level of differentiation
    for i in range(n):
        # compute the nth level of differentiation
        result = f.diff(x)
        # store the result in the list
        diff_list.append(result)
        # update the function to be the result of the nth level of differentiation
        f = result
    # return the list of levels of differentiation and if the function returns 0 until the nth level of differentiation
    is_tabular = True
    return diff_list
 