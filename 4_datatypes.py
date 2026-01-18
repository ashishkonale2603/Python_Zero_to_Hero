"""
    Datatypes are used to specify the type and size of data that is to be stored in the variable.

    Types of Dattypes:

    Datatypes
    |
    |-Single-value Datatype(Individual Datatype)
    | |
    | |-Numeric
    | | |-Integer(int)
    | | |-Float(float)
    | | |-Complex(comp)
    | |
    | |-Boolean
    |   |-bool
    |
    |-Multi-value Datatype(Collection Datatype)
      |-String(str)
      |-List(list)
      |-Tuple(tuple)
      |-Set(set)
      |-Dictionary(dict)

      
    Default Value:
    Default values are the initial values that are internally considered False.

    Non-default Values:
    Non-default values are the values that are internally considered True.
    All the values except Default Value are called as Non-default Values.

    Important Functions:
        (1)datatypeOf()[int()]
           It is used to check the default values of specified datatype.
           Ex. int()
               >>0
        
        (2)type()
           It is an in-built function which used to check the datatype of variable.
           Ex. type(a)
               >>int

        (3)id()
           It is an in-built function which used to fetch the address of values stored in the varaible.
           Ex. id(a)
               >>140716829472152

        (4)bool()
           It is an in-built function which used to check the values stored in the variable are default or not.
           If it is default it will return False, if it is not default it will return True.
           Ex. If a=10,   bool(a)
                          >>True
               If a=0,    bool(a)
                          >>False
        
"""


#Single-value Datatype

#Integer(int)
#They are real numbers without any decimal points.
#Range: -∞ to +∞
#Default Value: 0

intVar=100 #Syntax
print(intVar) #Output: 100

print(int()) #Output: 0

print(type(intVar)) #Output: <class 'int'>

print(bool(intVar)) #Non-default Value so Output: True

intVar=0
print(bool(intVar)) #Default Value so Output: False


#Float(float)
#They are real numbers with decimal points.
#Range: -∞ to +∞
#Default Value: 0.0

floatVar=100.0 #Syntax
print(floatVar) #Output: 100.0

print(float()) #Output: 0.0

print(type(floatVar)) #Output: <class 'float'>

print(bool(floatVar)) #Non-default Value so Output: True

intVar=0.0
print(bool(intVar)) #Default Value so Output: False