# Recurrsion

'''
    It is the process of function calling inself n number of times unless and until the termination condition becomes true.

    Syntax:
            def fname():
                if termination cond:
                    return val
                else:
                    return fname()
            fname()
    Ex. 
        Q. Find the factorial of given number. 
            5!=5*4**2*1 
            3!=3*2*1
'''
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n+fact(n-1)
fact(3)