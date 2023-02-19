from sympy import *
import eqparser
import differential
def IsTabularMethod(eq):
    expression = eqparser.str_to_func(eq)

    # check if function can be splitted into two parts
    # example x^(3)ln(x) can be splitted into x^(3) and ln(x)
    # if it can be splitted then it is a tabular method
    #     
    if expression.is_Mul:
        for i in range(len(expression.args)):
            if expression.args[i].is_Pow:
                if expression.args[i].args[1].is_Function:
                    pass

    # get term 1 and term 2 
    terms = expression.as_two_terms()
    term1 = terms[0]
    term2 = terms[1]

    # choose u and dv
    if differential.diff(term1, x, 1)[1] == True:
        u = term1
        dv = term2




    print(terms)

IsTabularMethod('x**3*ln(x**2)')





    

    


   
    
    
    

    
    