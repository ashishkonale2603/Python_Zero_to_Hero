'''
Looping Statement
    Looping Statement are the types of control statements which is used to control the flow of execution by repeating the task again and again for specified n number of times.

    We have two types of looping it:
    (i)while loop
    (ii)for loop
'''

'''
(i)while loop
    It is a type of looping statement which is used to perform same task repeatatively unless and until the given condition becomes False.
    In while loop, initialization and updation is mandatory.
    Synatx:
            initialization          ->starting point
            while condition:        ->ending point
                statement block
                updation            ->incremental/decremental

    Flowchart:
                            |
                      initialization
                            |
            --------------while -----<------
            |            condition         |
            |               |              |
            | False         |True          |
            |         Statement block      ^
            |               |              |
            |           Updation----->-----|
            |               |

    Ex.
'''
# #(1)
# i=0
# while i<5:
#     print('python')
#     i+=1

# #(2)
# n=int(input('Enter the value:'))
# i=1
# while i<n:
#     print(i*n)
#     i+=1

# #(3)
# n=int(input('Enter the value:'))
# i=1
# while i<10:
#     print(i*n)
#     i+=1

# #(4)
# n=int(input('Enter the value:'))
# i=1
# store=0
# while i<=n:
#     store=store+i
#     i+=1
# print(store)


'''
(ii)for loop
    for loop is called as self-iterative loop.
    Incase of while loop, initialization or updation are mandaetory but here in for loop intialization or updation are
    not mandetory, that is why, we call it as self-iterative loop.
    The loop is initialized and updated automatically.
'''
'''
Q.  Why to use for loop when we have while loop?
Ans.
    We can traverse through a list string or tuple by using while loop.
    But to traverse through set and dictionary while loop will not work so we will go for for loop.
'''

'''
range()
    It is used to create sequence of numbers with in the given limit.
    Syntax:
            var.range(SI,EI,Updation)
    Ex.
        a.range(1,10+1,1)
        range(1,11,1)
        range(1,11)

    If the starting index is equal to 0 and updation is equal to 1 then we can skip writing it.
    range() will not have it's own proper structure but we can provide an artificial structure but we can provide an artifical structure by using typecasting.
    Ex.
'''
print(list(range(1,11)))


'''
    Syntax for for loop:
        for var in collection:
            Statement Block

        where,
            var is the looping variable which follows identifer rule
            collection can be collection datatypes

    In for loop the number of iterations will be exactly equal to the number of values present inside the collection(length of collection).

    Flowchart:
                                |
            ------>------ for variable ----->------
            |             in collection            |until all values from
            ^modify             |                  |collection has been iterated
            |values             |                  |
            |            Statement block    

    Ex.  
'''
# #(1)
# a='sam'
# count=0
# for i in a:
#     count+=1
# print(count)

# #(2)
# a=eval(input("Enter list: "))
# store=[]
# for i in a:
#     if type(i)== int:
#          store.append(i)
# print(store)

# #(3)
# #to find the length oh homogenous tuple
# count=0
# a=eval(input("Enter tuple: "))
# for i in a:
#     count+=1
# print(count)

# #(4)
# a=eval(input("Enter list: "))
# store=[]
# for i in a:
#   if type(i)==int:
#       if i%2==0:
#              store.append(i)
# print(store)

'''
Nested for loop:
    -When we have one for loop written inside another for loop we call it as nested for loop.
    -We can write programs by using nested while loop still we go for nested for loop because in the case of while loop
     each and every time we have to initialize and update it.
    -If we miss the initialization or updation one single time it might result to cause an error or an infinite loop.
    -Nested for is use to traverse to value for more than one collection simultaniously and to perform required operation on it.

    -Syntax:
            for i in collection:
                for j in collection:
                    Statement Block
'''