from sympy import *

# convert the string to a function
def str_to_func(f):
    # create a variable to store the function
    func = 0
    # create a try/except block to catch any errors
    try:
        # convert the string to a function
        func = sympify(f)
    # catch any errors
    except:
        # print an error message
        print('Error: invalid function')
    # return the function
    return func


#print(str_to_func('x**2+2*x+1'))

