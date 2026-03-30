# Scope of Variable

'''
Variables are classified into two parts:
(1)Global Variables
(2)Local Variables
'''

'''
(1)Global Variables
    -The variable which is declared outside the function is called as Global Variable.
    -The scope of global variable is from starting of the file to the end of the file.
    -We can access the global variable outside the function and also we cam modify it but we can only access the global
        variable inside the function but cannot modify it.
    -To modify the global variable inside the function we use the keyword 'global'.

    Ex.
'''
a=10
print(a)
def add():
    global a
    a=20
add()
print(a)