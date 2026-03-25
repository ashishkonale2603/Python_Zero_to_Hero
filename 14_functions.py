'''
Function:
    Functions are the set of instructions or blocks of code which are used to perform some specific task or operation.

    We have 2 types of functions:
    (1)In-build functions
    (2)User defined functions
'''

'''
(1)In-built functions
    The function which are predefined by the developer are called as in-built functions.
    We have 6 types of in-built functions:
    (i)Utility functions
    (ii)Functions on String
    (iii)Functions on List
    (iv)Functions on Tuple
    (v)Functions on Set
    (vi)Functions on Dictionary
'''
'''
    (i)Utility Functions
    The in-built functions which can be used on more then 1 datatype are called as Utility functions.
    Ex.
        print(), eval() ,id() ,bool() ,type(), len(), input()

    (ii)Functions on String
    The in-built functions which supports string datatypes are called as functions on string to check with all the in-functions which supports string datatypes.
    We can use dir(str).
    Ex.
        lower(), upper(), islower(), isupper(), split(), strip(), capitalise()

    (iii)Functions on List
    The functions which supports list datatypes are called as Functions on list.
    To check with all the in-built functions which support list datatypes we can use dir(list).
    Ex.
        insert(), append(), pop(), remove(), extend(), clear(), sort()

    (iv)Functions on Tuple
    The in-built functions which supports tuple datatypes are called as Functions on tuple.
    To check with all the in-built functions which support tuple datatypes we can use dir(tuple).
    Ex.
        count(), index()
    
    (v)Functions on Set
    The in-built functions which supports set datatypes are called as Functions on set.
    To check with all the in-built functions which support set datatypes we can use dir(set).
    Ex.
        union(), issubset(), issuperset(), add(), pop()

    (iv)Functions on Dictionary
    The in-built functions which supports dictionary datatypes are called as Functions on dictionary.
    To check with all the in-built functions which support dictionary datatypes we can use dir(dict).
    Ex.
        keys(), values(), items(), popitem()
        
'''

'''
(2)User-defined Function
    The function which are declred or defined by the user are called as user defined functions.

        def
        It is a keyboard which is used to define or declare the function.

        return
        It is a keyword which returns values or result directly to the function calling statement.
        return can return multiple values 
            Syntax: 
                    return value

    The user-defined function are classified into 4 types:
    (i)Function without argument and without return
    (ii)Function without argument and with return
    (iii)Function with argument and without return
    (iv)Function with argument and with return

'''

'''
    (i)Function without argument and without return
    The function which do not have arguments and do not have return keyword are called as Function without argument and without return.
    Syntax:
            def fname():
                statement block
            fname()

    Ex. 
        def add():
            a=10
            b=20
            print(a+b)
        add()

    Memory allocation:

        _______________________________________________
        |     main space      |     method space      |
        |---------------------------------------------|
        |                     |               0x11    |
        |      add()          |   ----------------    |
        |    ----------       |   |   a=10       |    |
        |    |  0x11  |<------|---|   b=20       |    |
        |    ----------       |   |   print(a+b) |    |
        |                     |   ----------------    |
        |_____________________|_______________________|

    (ii)Function with argument and without return
    The function which have arguments and do not have return keyword are called as Function with argument and without return.
    Syntax:
            def fname(a,b):
                statement block
            fname()

    Ex. 
        def add(a,b):
            print(a+b)
        add(10,20)

    Memory allocation:

        _______________________________________________
        |     main space      |     method space      |
        |---------------------------------------------|
        |                     |                       |
        |    add(10,20)       |             0x11      | 
        |    ----------       |   ----------------    |
        |    |  0x11  |<------|---|   print(a+b) |    |
        |    ----------       |   ----------------    |
        |_____________________|_______________________|

    (iii)Function without argument and with return
    The function which do not have arguments but has return keyword are called as Function without argument and with return.
    Syntax:
            def fname():
                statement block
                return val
            fname()

    Ex. 
        def add():
            a=10
            b=20
            return a+b
        add()

    Memory allocation:

        _______________________________________________
        |     main space      |     method space      |
        |---------------------------------------------|
        |                     |               0x11    |
        |      add()          |   ----------------    |
        |    ----------       |   |   a=10       |    |
        |    |  0x11  |<------|---|   b=20       |    |
        |    ----------       |   |   return(a+b)|    |
        |                     |   ----------------    |
        |_____________________|_______________________|

    (iv)Function with argument and with return
    The functions having arguments and returns some values are called as Function with argument and with return.
    Syntax:
            def fname(args):
                statement block
                return val
            fname(val)

    Ex. 
        def add(a,b):
            return a+b
        print(add(10,20))

    Memory allocation:

        _______________________________________________
        |     main space      |     method space      |
        |---------------------------------------------|
        |                     |                       |
        |     add(a,b)        |               0x11    |
        |    ----------       |   ----------------    |
        |    |  0x11  |<------|---|   return a+b |    |
        |    ----------       |   ----------------    |
        |_____________________|_______________________|
'''

