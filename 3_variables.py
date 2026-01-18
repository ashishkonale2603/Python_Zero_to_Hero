"""
    Variables:
    Variables are named memory location which are used to store values inside them.
    Syntax:
        var_name = val_value
    Ex.
        var=10

    Inside block of memory we can store only 1 value or 1 address at a time.
    

    Multiline Variable Creation:
    It is a phenomennon of creating multiple variables in one single line.
    In pyhron , while doing multiline variable creation the number of values should be exactly equal to the number of variables.
                no. of variables=no. of values
    Syntax:
        var1,var2,....,varN=val1,val2,....,valN
    Ex.
        num1,num2,num3=10,20,30

    
    id()
    It is an in-built function which used to fetch the address of values stored in the varaible.
    Syntax:
        id(var/val)
    Ex.
        id(a)
        >>140716829472152

    
    Identifiers:
    Identifiers are the meaningful names givento the variables, class and functions.

    Rules for Creating Identifiers:
    (1) It shouldn't be a keyword.
        Ex.
            if=10     Error
            True=10   Error
        
    (2) It shouldn't start with number.
        Ex.
            2a=10     Error
            a2=10     Accepted

    (3) It shouldn't have space in between or at beginning.
        Ex.
            a b=10    Error
             ab=10    Bad practice but no error

    (4) It shouldn't have special symbol except "_".
        Ex.
            @abc=10   Error
            a_b=10    Accepted

    (5) We can have Uppercase letters(A-Z), Lowercase lettters(a-z), numbers(0-9) except at beginning, "_", and alphanumericals.

    (6) According to ISR(Industrial Standard Rules):
        Length of the identifer should be upto 79 characters.

"""

#variable creation
var=10
print(var)

#Multiline Variable Creation
num1, num2, num3 = 10,20,30
print(num1,num2,num3)

#id()
print(id(var))
print(id(num1))


#Scenario 1:
    #More values than variables
    #Ex.
#num1,num2,num3=10,20,30,40
#Error: Too many values to unpack


#Scenario 2:
    #More varibales then values
    #Ex.
#num1,num2,num3,num4=10,20,30
#Error: Too enough values to unpack


#Scenario 3:
    #Multiple variables with single values
    #Ex.
a,b,c=10,11,10
print(id(a))
print(id(b))
print(id(c))
#140714200823192
#140714200823224
#140714200823192    same as a and reference count(RC) for 10 is 2


#Scenario 4:
    #Multiple variables assigned to single variable
    #Ex.
d,d,d=10,11,12
print(d)
# d=12 which is the latest/newest value