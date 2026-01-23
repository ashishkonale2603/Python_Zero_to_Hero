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


    Default and Non-default Values: 
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

    Indexing:
        It is phenomenon or process of giving subaddress to the values present inside the collection.
        (i) Positive Indexing
            -It goes from left to right direction.
            -It starts with 0 and ends with [len(variable)-1].

        (ii)Negative Indexing
            -It goes from right to left direction.
            -It starts with -1 and ends with [-len(variable)].

    Mutable and Immutable Datatype:
        Mutable Datatype
        -The datatype in which we can perform modification(adding data, removing data or replacing data)
         are called as mutable datatype.

        Immutable Datatype
        -The datatype in which we cannot perform modification are called as mutable datatype.
        
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
print(bool(boolNum)) #Default Value so Output: False


#String
#String is collection of characters enclosed within single quote(''), double quote("") or triple
# quote(''' ''').
#Default value of String is ''.
#We go for double quote("") when we have single quotes included within string.
#When we want to store the data in the document form then go with triple quotes. So this string
# is also called as 'Doc String'
#To get the count of values inside your given string use 'length()'
#    eg. a='Qspiders'
#        >>len(a)
#        >>8
#String is immutable datatype.

string='Qspiders'   #Syntax
print(string)

print(id(string))   #Output: 1828745103536

default=str()
print(default)   #Output: ''

print(type(string))   #Output: <class 'str'>

print(bool(string))   #Non-default Value so Output: True

string=''
print(bool(string))   #Default Value so Output: False


#List
#List is an collection of homogenous or heterogenousvalues enclosed within square braces.
#Syntax:   var_name=[val1,val2,val3,...,val4]
#Default value of list is [].
#List is a mutable type of collection so we can perform modification.

temp=[1,2,3,4,5]   #Syntax
print(temp)

print(id(temp))   #Output: 2724270029120

print(list())   #Output: []

print(type(temp))   #Output: <class 'list'>

print(bool(temp))   #Non-default Value so Output: True

temp=[]
print(bool(temp))   #Default Value so Output: False


temp=[11,12,23,27,32,36]
print(temp)   #Output: [11, 12, 23, 27, 32, 36]

#adding data
'''
append()
-It is in-built function which is used to add the given value st the lost position in the list.
-Syntax: variable.append(value)
-Ex.
'''
temp.append(40)
print(temp)   #Output: [11, 12, 23, 27, 32, 36, 40]

'''
insert()
-It is in-built function which is used to add the given value at the specified index.
-Syntax: variable.insert(value)
-Ex.
'''
temp.insert(0,13)
print(temp)   #Output: [13, 11, 12, 23, 27, 32, 36, 40]

#removing data
'''
pop()
-It is in-built function which is used to remove the last value from the given list.
-Syntax: variable.pop()
-Ex.
'''
temp.pop()
print(temp)   #Output: [13, 11, 12, 23, 27, 32, 36]

'''
remove()
-It is in-built function which is used to remove the specified value from the collection.
-Syntax: variable.remove(value)
-Ex.
'''
temp.remove(13)
print(temp)   #Output: [11, 12, 23, 27, 32, 36]

#replace data
'''
var[index]=new_value
Ex.
'''
temp[2]=24
print(temp)   #Output: [11, 12, 24, 27, 32, 36]


#Tuple
#Tuple is the collection of homogenous or heterogenous values enclosed within paranthesis.
#Syntax:  var=(val1,val2,...,valn)
#Default values of tuple is ().
#It is a immutable type of collection.
#It is also called as secured datatype.

tup=(1,2,3,4,5)   #Syntax
print(tup)

print(id(tup))   #Output: 2168494787648

print(tuple())   #Output: ()

print(type(tup))   #Output: <class 'tuple'>

print(bool(tup))   #Non-default Value so Output: True

tup=()
print(bool(tup))   #Default Value so Output: False


#Set
#Set is the unordered collection of homogenous or heterogenous values enclosed within curlt braces.
#Syntax: variable={val1,val2,...,valn}
#The default value of set is set().
#Set will not support indexing.
#Set will not allow duplicates.
#It is a mutable type of collection.

myset={5,4,3,1,2}   #Syntax
print(myset)

print(id(myset))   #Output: 2089716490400

print(set())   #Output: set()

print(type(myset))   #Output: <class 'set'>

print(bool(myset))   #Non-default Value so Output: True

myset={}
print(bool(myset))   #Default Value so Output: False

tom={27,91,55,100}
print(tom)   #Syntax
#Output: {91, 27, 100, 55}

#adding data
'''
add()
It is in-built function which is used to add the value at any random position in a given set.
Syntax: variable.add(value)
Ex.
'''
tom.add(45)
print(tom)   #Output: {100, 27, 45, 55, 91}

#removing data
'''
pop()
It is in-built function which is used to remove the first value from set.
Syntax: variable.pop()
Ex.
'''
tom.pop()
print(tom)   #Output: {27, 45, 55, 91}

'''
remove()
It is in-built function which is used to remove any specified value from set.
Syntax: variable.remove(value)
Ex.
'''
tom.remove(91)
print(tom)   #Output: {27, 45, 55}


#Dictionary
#It is a collection of homogenous and heterogenous type of data which is in the form of keys and 
# values enclosed within curly braces.
#Syntax: var={'val1':val1,'val2':val2,...'valn':valn}
#Duplicates are not allowed in the dictionary.
#Indexes are not present in the dictionary.
'''
Key:
    Keys are the visible layer inside the dictionary.
    Keys must be unique and immutable.

Values:
    Values can be anything.
'''
#Dictionary is a mutable type of collection with respect to values.
