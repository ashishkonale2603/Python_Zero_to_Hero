# Types of Arguments

'''
We have four types of arguments:
(1)Positional Argument
(2)Keyword Argument
(3)Default Argument
(4)Variable Length Argument

'''

'''
(1)Positional Argument
    Positional arguments are the arguments which are used to store the value inside the formal arguments depending upon the position.
    It stores values based on position.
    Positional arguments are the first argument written inside a function.
    Ex.
        def fname(name,roll):
            print(name,roll)
        fname('ashish',27)

(2)Keyword Argument
    This is the argument where we pass the value to the variable in the form key and value pair in the function calling statement.
    Ex.
        def fname(name,roll):
            print(name,roll)
        fname(roll=27,name='ashish')

(3)Default Argument
    This is the type of arguments where we pass the default value to a variable in the function declaration and it should be the last argument.
    Ex.
        def fname(name,roll=1):
            print(name,roll)
        fname('ashish',27)

(4)Variable Length Argument
    This argument are used to work when we want to use both positional argument and keyboard argument in single function.
    We have two types of variable length arguments i.e. Packing and Unpacking.
    Here, the length of values may vary so we call them as variable length arguments.
    
'''




