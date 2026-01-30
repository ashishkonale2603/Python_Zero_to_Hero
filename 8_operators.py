'''
Operators:
    Operators are the special symbols or keywords which are used to perform some specific task(predefined task)
    by the developer.

    Operators are one of the type of library function.

    Operands:
    Operands are the values on which operator will perform the task.
    Number of operands required to perform a specific task depends upon the type of operator which is to be used.

    We have 7 types of operator:
    (a) Arithmatic Operator
    (b) Relational Operator
    (c) Logical Operator
    (d) Bitwise Operator
    (e) Assignment Operator
    (f) Identity Operator
    (g) Membership Operator
'''

'''
(a) Arithmatic Operators:
    It is used to perform arithmatic operations on the given operands.
    (i)Addition(+)
    (ii)Substraction(-)
    (iii)Multiplication(*)
    (v)Division
        1.True Division(/)
        2.Floor Division(//)
        3.Modulus(%)
    (v)Power(**)
'''

'''
    (i)Addition(+)
    Incase of single value datatypes it will perform addition operation, whereas incase of multivalue datatype
    it is going to perform concatination operation.
    Syntax:  operand1 + operand2
    Ex.
'''
print('Addition')
print(11+9)
print([11,12,13,14] + [15,16,17,18])
print((10+11j) + (20+10j))

#Addition will not support set and dictionary.


'''
    (ii)Substraction(-)
    It is used to find the difference between the operands.
    Syntax:  operand1 - operand2
    Ex.
'''
print('Substraction')
print(10 - 9)
print({11,12,13,14,15} - {14,15,16,17})
print(True - False)

#Substraction does not support any multivalue datatype except Set datatype.


'''
    (iii)Multiplication(*)
    This operators is used to find the product of the operands.
    Syntax:  operand1 * operand2    =>  (Single-value Datatype)
             operand1 * N           =>  (Multi-value Datatype)
    Ex.
'''
print('Multiplication')
print(20 * 7)
print([1,2,3,4] * 2)


'''
    (iv)Division
    This operator is used to perform division operation for operands.
    We have 3 types of division:
    1. True Division(/)
    2. Floor Division(//)
    3. Modulus(%)
'''
print('Division')
'''
        1.True Division(/)
        It is used when we want to fetch complete quotient value(floating number as well).
        Syntax:  operand / n
        Ex.
'''
print('True Division')
print(11 / 3)
print(47 / 2)

'''
        2.Floor Division(//)
        It is used to fetch only the integer part of the quotient.
        Syntax:  operand // n
        Ex.
'''
print('Floor Division')
print(11 // 3)
print(47 // 2)

