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
'''

