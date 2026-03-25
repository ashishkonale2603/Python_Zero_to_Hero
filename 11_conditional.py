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


'''
(3)elif
    It is a type of a control statement which is used to provide out when we have multiple condition to check with and multiple statement blocks to be executed.
    Syntax:
            if condition:
                True Statement Block
            elif condition:
                True Statement Block
            
            else:
                False Statement Block

            (Else block is optional)

    Flowchart:
                    |
                    |
                    if _________________________elif____________ _ _ _ __________
                   cond   False                 cond    False      n             |
                    |                            |                               |
                    |                            |                               |
                    |True                        |                               |
                    |                            |                               |
             True Statement Block      True Statement Block            False Statement Block
                    |                            |                               |
    Ex.
'''
# a=(input("Enter the char:"))
# if 'a' <= a <= 'z':
#     print("Lower Case")
# elif 'A' <= a <= 'Z':
#     print("Upper Case")
# elif '0' <= a <= '9':
#     print("Digit")
# else:
#     print("Special Symbol")


'''
(4)Nested if
    When we have one if condition written inside another if condition, we call it as nested if.
    Syntax:
            if condition:
                if condition:
                    True Statement Block
                else:
                    False Statement Block 2
            else:
                False Statement Block 1

    Flowchart:
                    |
                    |
                    if _________________________ if ____________ _ _ _ __________
                   cond   True                  cond               n             |
                    |                            |                               |
                    |                            |                               |
                    |False                       |False                          |True
                    |                            |                               |
            False Statement Block      False Statement Block            True Statement Block
                    |                            |                               |              
    Ex.     
'''
# a=input('Enter the Char:')
# if 'A' <= a <= 'Z' or 'a' <= a <= 'z':
#     if a in 'AEIOUaeiou':
#         print('Vowel')
#     else:
#         print('Consonent')
# else:
#     print('Not a character')

# a=input('Enter the Username:')
# if a=='ashish23':
#     b=input('Enter the password:')
#     if b=='password':
#         print('Login Sucessful')
#         print('Welcome to Instagram')
#     else:
#         print('Invalid Password')
# else:
#     print('Invalid Username')
