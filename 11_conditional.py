'''
Conditional Statements
    These are the statements which are used to control the flow of execution of a given program.
'''

'''
(1)Simple if
    It is a type of conditional statement where we have one condition to be satisfied and one statement block to be executed.
    It the condition becomes it will be executed True statement block or else it will ignore the true statement block.

    Syntax:
            if condition:
                True Statement Block

    Flowchart:
                    |
                    | 
                   if  ________________
                   cond                |
                    |                  |
                    |                  |
             True Statement Block      |
                    |                  |

    Ex.
'''
# (1)
# a=int(input('Enter number for square:'))
# if a%2==0:
#     print(a*a)

# (2)
# b=input('Enter a single character:')
# if b in "aeiouAEIOU":
#     print(b)

# (3)
# c=input('Enter a single character:')
# if 'A' <= c <= 'Z':
#     print(ord(c))


'''
(2)if else
    It is a type of conditional statement where we will be having one condition to check with and 2 statement block to be executed.
    Syntax:
            if condition:
                True Statement Block
            else:
                False Statement Block

    Flowchart:
    Flowchart:
                    |
                    | 
                   if  _____________________________
                   cond         False               |
                    |                               |
                    |True                           |
                    |                               |
             True Statement Block         False Statement Block
                    |                               |
    Ex.
'''
# #(1)
# a=eval(input('enter the values:'))
# if a in [str,tuple]:
#     print("Immutable")
# else:
#     print("Mutable")

# #(2)
# a=input("Enter tha char:")
# if '0' <= a <= '9':
#     print('Present')
# else:
#     print('Not Present')

# #(3)
# a=input("Enter tha char:")
# if ('a'<= a <= 'z') or ('A' <= a <= 'Z') or ('0'<= a <= '9'):
#     print('Not special Symbol')
# else:
#     print('Special Symbol')

# # (4)
# a=eval(input('enter the values:'))
# if len(a)%2==0:
#     print('No middle value')
# else:
#     print('Middle value')