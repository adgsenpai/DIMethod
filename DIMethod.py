from sympy import *
import eqparser
import differential

def ComputeTabularMethod(eq, iters=1000):
    # Convert input equation to a SymPy expression
    expression = eqparser.str_to_func(eq)
    # Check if function can be splitted into two parts.
    # If it can be splitted, then it is a tabular method.
    if expression.is_Mul:
        for i in range(len(expression.args)):
            if expression.args[i].is_Pow:
                if expression.args[i].args[1].is_Function:
                    pass
        # TODO: Handle case where function can be splitted into two parts
        #return {'message': 'Function can be splitted into two parts'}

    # Get term 1 and term 2    
    terms = expression.as_two_terms()
    term1 = terms[0]
    term2 = terms[1]

    # Choose u and dv
    tOneCheck = differential.diff(term1, iters)
    tTwoCheck = differential.diff(term2, iters)

    # Check if tOneCheck or tTwoCheck is zero
    opt = {'is_zero': False, 'minlenDiff': 0, 'termNum': None, 'diff_list': []}

    if tOneCheck['is_zero'] == True:
        opt['is_zero'] = True
        opt['minlenDiff'] = len(tOneCheck['diff_list'])
        opt['termNum'] = 1
        opt['diff_list'] = tOneCheck['diff_list']

    if tTwoCheck['is_zero'] == True:
        if opt['is_zero'] == False:
            opt['is_zero'] = True
            opt['minlenDiff'] = len(tTwoCheck['diff_list'])
            opt['termNum'] = 2
            opt['diff_list'] = tTwoCheck['diff_list']
        elif len(tTwoCheck['diff_list']) < opt['minlenDiff']:
            opt['minlenDiff'] = len(tTwoCheck['diff_list'])
            opt['termNum'] = 2
            opt['diff_list'] = tTwoCheck['diff_list']

    if opt['is_zero'] == True:
        u = None
        dv = None
        # Choose u and dv based on the term with the most zeros in the differential list
        if opt['termNum'] == 1:
            u = term1
            dv = term2
        elif opt['termNum'] == 2:
            u = term2
            dv = term1
        print('u =', u)
        print('dv =', dv)
        # Get the differential list
        diff_list = opt['diff_list']        
        x = Symbol('x')
        # for each item in diff_list, compute the integral
        integral_list = []
        integral_list.append(dv)
        for i in range(len(diff_list)):        
            dv = integrate(dv, x)
            integral_list.append(dv)            
        print('diff_list =', diff_list)
        print('integral_list =', integral_list)        
        signs = []
        for i in range(len(integral_list)):
            signs.append((-1)**i)                
        # init the result with 1 constant
        result = 1        
        for i in range(len(diff_list)-1):
            if not i == len(diff_list)-1:                        
                result += diff_list[i]*integral_list[i+1]*signs[i]
             
        # simplify the result and also remove the constant
        result = simplify(result-1)
                                                                           
        return {'message': 'Function can be splitted into two parts and the solution is: '+str(result)+' + C', 'u': u, 'dv': dv, 'diff_list': diff_list, 'integral_list': integral_list,'result': result}

    else:
        ans = str(integrate(expression))
        return {'message': 'Function cannot be splitted into two parts but the solution is: '+ans+' + C', 'u': None, 'dv': None, 'diff_list': None, 'integral_list': None, 'result': ans}

if __name__ == '__main__':
    eq = 'sin(2*x+1)*(2*x)'
    print(ComputeTabularMethod(eq,100))
