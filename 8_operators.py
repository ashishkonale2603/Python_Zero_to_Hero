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


'''
    (iii)Logical not(not)
    It is used to print reverse or opposite.
    Syntax:  not(operand)
    Truth Table:
                |------------------|
                |  Input  | Output |
                |------------------|
                |    0    |    1   |
                |    1    |    0   |
                |------------------|

    Conditions:
    1.if operand1 == True
        output == False
    2.if operand1 == False
        output == True
    
    Ex.
'''
print("Logical not example:")
print(not(0))
print(not(10))


'''
(d)Bitwise Operator
    This operator are useful to perform bitwise operations on the given values.

    We have 6 types of bitwise operators:
    (i)Bitwise and(&)
    (ii)Bitwise or(|)
    (iii)Bitwise not(~)
    (iv)Bitwise XOR(^)
    (v)Bitwise left-shift(<<)
    (vi)Bitwise right-shift(>>)
'''


'''
    (i)Bitwise and(&)
    This operator is used to convert integer to binary and then perform bitwise and operation on it.
    Syntax:  operand1 & operand2
    Ex.
        7 & 10

        8  4  2  1
        0  1  1  1  =>  7
        1  0  1  0  =>  10
       ------------
        0  0  1  0  =>  2
'''
print("Bitwise and example:")
print(7 & 10)


'''
    (ii)Bitwise or(|)
    This operator is used to convert integer to binary and then perform bitwise or operation on it.
    Syntax:  operand1 | operand2
    Ex.
        7 | 10

        8  4  2  1
        0  1  1  1  =>  7
        1  0  1  0  =>  10
       ------------
        1  1  1  1  =>  15
'''
print("Bitwise or example:")
print(7 | 10)


'''
    (iii)Bitwise XOR(^)
    This operator is used to convert integer to binary and then perform bitwise XOR operation on it.
    Syntax:  operand1 ^ operand2
    Ex.
        7 ^ 10

        8  4  2  1
        0  1  1  1  =>  7
        1  0  1  0  =>  10
       ------------
        1  1  0  1  =>  13
'''
print("Bitwise XOR example:")
print(7 ^ 10)


'''
    (iv)Bitwise not(~)
    By providing negation to the given value and by adding 1 it will work.
    It is used to perform bitwise not operation.
    Syntax:  -(operand + 1)
    Ex.
            ~(10)
        =>    -(10+1)
        =>    -(11)
        =>    -11

            ~(-10)
        =>    -(-10+1)
        =>    -(-9)
        =>    -9
'''
print("Bitwise not example:")
print(~(10))
print(~(-10))


'''
    (v)Bitwise left-shift(<<)
    It is used to convert integers to binary and then shift values to left side for specific n number of times.
    Syntax:  operand << n
    Ex.    12 << 2
            32   16   8   4   2   1
                      1   1   0   0
                  1   1   0   0   0
             1    1   0   0   0   0  => 48
'''
print("Bitwise left-shift")
print(12 << 2)


'''
    (vi)Bitwise right-shift(>>)
    It is used to convert integers to binary and then shift values to right side for specific n number of times.
    Syntax:  operand >> n
    Ex.    12 >> 2
            8   4   2   1
            1   1   0   0
                1   1   0   0
                    1   1   0   0  => 3
'''
print("Bitwise right-shift")
print(12 >> 2)


'''
(e)Assignment Operator(=)
    This operator is used to assign or store the value in the given variable.
    The symbol of assignment operator is '='.
    Ex.
        a=10


        Argumented assignment operator:
        This operator are used to modify the values of a given variable and by performing arithmatic or relational operations on it.
        (+=, -=, *=, /=, //=, %=)
        Ex.
            a=10         a=20
            a+=10        a-=10
            >>20         >>10
'''


'''
(f)Identity Operator
    This operators are used to check whether the given value are pointing to the same memory location or not.

    We have two types of identity operator:
    (i) is
    (ii)is not
'''


