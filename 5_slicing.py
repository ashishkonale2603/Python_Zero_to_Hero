'''
Slicing
    It is a process of fetching out part of a collection in a sequential manner.
    Syntax: var[SI:EI:Updation]
            where SI is Starting Index
                  EI is Ending Index
                  Updation is number of steps

    Slicing can be done with only those datatypes which support indexing.
'''

'''
Shortforms for using Slicing syntax:
    -If Starting Index is the first value we can skip writing it.
    -If Ending Index is the last value we can skip writing it.
    -if updation is 1 then we can skip writing it.
    -To fetch the value of even indexing:
        Syntax: var[ : :2]
    -To fetch the value of even indexing:
        Syntax: var[1: :2]
    -To reverse the given collection we will use the
        Syntax: var[ : :-1]
'''