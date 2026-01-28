'''
Copy Operation:

    The process of coping the content from one variable to another is called as copy operation.

    There are 3 types of copy:
    (1) General Copy
    (2) Shallow Copy
    (3) Deep Copy
'''

'''
General Copy:
It is the process of coping the content from one variable to another with same address.
Syntax: dest_var = source_var

Drawback:
In general copy, if values from one variable is modified another variable as well.

Ex.
'''
a=[1,2,[3,4,7]]
print(a)

b=a
print(b)

a[1]=8
print(a)
print(b)

a[2][1]=17
print(a)
print(b)