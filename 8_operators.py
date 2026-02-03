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

'''
        3.Modulus(%)
        It is used when we want to fetch the remainder part of the quotient5_.
        Syntax:  operand % n
        Ex.
'''
print('Modulus')
print(11 % 3)
print(47 % 2)

'''
    (v)Power(**)
    It is used when we want to multiple the operand with itself with specified n number of times.
    Syntax:   operand ** n
    Ex.
'''
print(4**3)
print(16**2)
print(5**5)


'''
(b)Relational Operator
    Relational operators are used to check relation between the provided operand.

    We have 6 types of Relational Operator:
    (i)Equal to(==)
    (ii)Not equal to(!=)
    (iii)Grater than(>)
    (iv)Less than(<)
    (v)Greater than equal to(>=)
    (vi)Less then equal to(<=)
'''

'''
    (i)Equal to(==)
    This operator is used to check weather the given values are equal or not.
    Syntax:   operand1 == operand2
    Ex.
'''
print(10 == 10.0)
print(17 == 179)


'''
    (ii)Not equal to(!=)
    This operator is used to check weather the two given values are equal or not.
    Syntax:  operand1 != operand2
    Ex:
'''
print(10 != 10.0)
print(17 != 179)


'''
    (iii)Greater than(>)
    This operator is used to check weather the operand1 is greater than operand2 or not.
    Syntax:  operand1 > operand2
    Ex:
'''
print(16 > 179)
print(19 > 18)


'''
    (iv)Less than(<)
    This operator is used to check weather the operand1 is lesser than operand2 or not.
    Syntax:  operand1 < operand2
    Ex:
'''
print(16 < 179)
print(19 < 18)


'''
    (v)Greater than egual to(>=)
    This operator is used to check weather the operand1 is greater than or equal to operand2 or not.
    Syntax:  operand1 >= operand2
    Ex:
'''
print(17 >= 18)
print(17 <= 12)
print(17 >= 17)


'''
    (vi)Less than equal to(<=)
    This operator is used to check weather the operand1 is lesser than or equal to operand2 or not.
    Syntax:  operand1 <= operand2
    Ex:
'''
print(91 <= 93)
print(94 <= 80)
print(12 <= 12)


'''
(c)Logical Operator
    Logical Operator are used to perform logical operations on the given operands.

    There are 3 types of logical operation:
    (i)Logical and(and)
    (ii)Logical or(or)
    (iii)Logical not(not)
'''

'''
    (i)Logical and(and)
    Both inputs are true then only it will return true,
    if either one input is false then it will return false.
    Syntax:  operand1 and operand2
    Truth Table:
                |--------------------------------|
                |       Input         |  Output  |
                |---------------------|          |
                |  Input1  |  Input2  |    0     |
                |--------------------------------|
                |    0     |    0     |    0     |
                |    0     |    1     |    0     |
                |    1     |    0     |    0     |
                |    1     |    1     |    1     |
                |--------------------------------|

    Conditions:
    1.if operand1 == False
        output == operand1
    2.if operand1 == True
        output == operand2

    Ex.
'''
print(11 and 0)
print(11 and 10)
print(0 and 10)


'''
    (ii)Logical or(or)
    Both inputs are false then only it will return false,
    if either one input is true then it will return true.
    Syntax:  operand1 or operand2
    Truth Table:
                |--------------------------------|
                |       Input         |  Output  |
                |---------------------|          |
                |  Input1  |  Input2  |          |
                |--------------------------------|
                |    0     |    0     |    0     |
                |    0     |    1     |    1     |
                |    1     |    0     |    1     |
                |    1     |    1     |    1     |
                |--------------------------------|

    Conditions:
    1.if operand1 == False
        output == operand2
    2.if operand1 == True
        output == operand1

    Ex.
'''
print(11 or 0)
print(11 or 10)
print(0 or 10)