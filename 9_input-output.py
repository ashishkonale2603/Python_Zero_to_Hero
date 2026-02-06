
#Input/Output
'''
Input:

    The statements which are used to take data in a form of input from user are called as input statement.
    We use input in-built function to take the data from the user.
    It is a in-built function which is used to take values from the user to make the code dynamic.

    Syntax:  var_name = input('message')
                                  ^
                                  |
                                  |-----optional
    
    Message in the in-built function is optional.
    Whenever we are using input function, data will be stored in the form of String.
    To take the data from the user in a specified datatype, it is required to typecast.

    Ex.
        a=input('Enter no:')
        

        ----------------------------------------------------------------------------------------------------------------------
        |--------------------------------------------------------------------------------------------------------------------|
        |                                                                                                                    |
        |   eval()                                                                                                           |
        |   It is an in-built function which is used to evaluate the input datatype and store in the form of same datatype.  |
        |   Syntax:  var_name = eval(input('message'))                                                                       |
        |                                                                                                                    |
        |   weight=eval(input('Enter Weight:'))                                                                              |
        |   print(weight, type(weight))                                                                                      |
        |                                                                                                                    |
        |   Ex.                                                                                                              |
        |           10                              2.3                                                                      |
        |           >>10,int                        >>2.3,float                                                              |
        |                                                                                                                    |
        |--------------------------------------------------------------------------------------------------------------------|
        ----------------------------------------------------------------------------------------------------------------------
''' 

'''
Output:
    
    print()
    It is an in-built function which is used to give output to user.

    It has two attributes:
    (i)separator(sep)
    (ii)end
    
    print statement accepts multiple values.


    (i)separator(sep)
    This operator is used to separator multiple values inside a print statement.
    Default value of separator is space ' '.
    We can modify the value of separator.
    Syntax:  sep = new_value
    Ex.  sep = '***'

    (ii)end
    This attribute is used to end multiple print statements.
    The default value of end is '\n'.
    We can modify the value of end attribute.
    Syntax:  end = new_value
    Ex.  end = '***'

    Example:
'''
print('Output')
print('I am Ashish','I live in Pune')
print('I love to eat')
print('I am Ashish','I live in Pune',sep='-',end='***')
print('I love to eat')