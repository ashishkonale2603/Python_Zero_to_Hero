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


#Complex(comp)
#These number are the number having real part and imaginary part.
#Syntax:   a+bj  or  a+bJ
#j and J are called as imaginary character.
#a snd b are a real number which consist either integer or float.
#The default value of complex number is 0j.

compNum=10j+11 #Syntax
print(compNum)

print(id(compNum)) #Output: 2894473633136

print(complex()) #Output: 0j

print(type(compNum)) #Output: <class 'complex'>

print(bool(compNum)) #Non-default Value so Output: True

compNum=0j
print(bool(compNum)) #Non-default Value so Output: False


#boolean
#It consist of boolean values that is True and False.
#True will be internally be considered as 1 and False will be internally be considered as 0.
#Default value os boolean is False.

#Where to use boolean datatype.
#(1)It can be used to store value inside a variable.
#(2)It can be used as a resultant for a given condition.

boolNum=True
print(boolNum) #Syntax

print(id(boolNum)) #Output: 140704581798656

print(bool()) #Output: False

print(type(boolNum)) #Output: <class 'bool'>

print(bool(boolNum)) #Non-default Value so Output: True

boolNum=False
print(bool(boolNum)) #Non-default Value so Output: False






temp=[11,12,23,27,32,36]
print(temp)
temp.append(40)
print(temp)
temp.insert(0,13)
print(temp)
temp.pop()
print(temp)
temp.remove(13)
print(temp)