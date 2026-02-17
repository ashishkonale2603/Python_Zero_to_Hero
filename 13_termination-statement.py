'''
Intermediate Termination Statement:
    This statement are used to terminate the loop based on user requirement.

    We have three types of keywords:
    (i)break
    (ii)continue
    (iii)pass
'''

'''
(i)break
It is the intermediate termination which is used to stop once it is executed it will come out of the loop and it will not
run furthur lines of code also it will not go back to the loop again.
Ex.
    for i in range(1,6):
        if i==3:
            break
        print(i)

O/P:    1,2        
'''

'''
(ii)continue
It is used to skip the iteration here furthur lines of code will not get executed but it will go back to the loop again.
Ex.
    for i in range(1,6):
        if i==3:
            continue
        print(i)

O/P:    1,2,4,5
'''
