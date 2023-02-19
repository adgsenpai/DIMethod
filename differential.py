from sympy import *

# create a function to compute n levels of differentiation and then return the result if the function returns 0 until the nth level of differentiation store each level of differentiation in a list
def diff(f, n):
    x = Symbol('x')
    # create a list to store the levels of differentiation
    diff_list = [f]
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
        # break the loop if the function returns 0
        if result == 0:
            break
    # return the list of levels of differentiation and if the function returns 0 until the nth level of differentiation
    
    if result == 0:
        return {
            'diff_list': diff_list,
            'is_zero': True
        }
    else:
        return {
            'diff_list': diff_list,
            'is_zero': False
        }

