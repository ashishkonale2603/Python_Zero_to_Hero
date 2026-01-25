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
a='Python Programming Language'

print(a[:7:1])
print(a[7:14:1])
print(a[11:15:1])
print(a[:8:2])
print(a[5:1:-1])

print(a[:-21:1])
print(a[-20:-13:1])
print(a[-16:-12:1])
print(a[:-22:2])
print(a[-22:-26:-1])