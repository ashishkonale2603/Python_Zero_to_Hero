# OOPS

'''
    OOPS stands for Object Oriented Programming System.

    It is an approach which is used to solve real world problems in virtual way(by creating software) with use of classes and objects.

        Class:
        It is a blueprint or template which consist of properties and functionalities of an object.

        Object:
        It is a real-time entity or an instance of a class.

    Syntax:
        class class_name:
            properties and functionalities

        object_name=classname(args)

    Ex.
'''
class Car:
    car_brand='Tesla'
    car_model='Model S'
    fuel_type='Electric'
car1=Car()
car2=Car()

'''
Accessing Properties:

    Syntax:
        class_name.property_name
        object_name.property_name

    Ex.
'''
# class Company:
#     company_name='TestYantra'
#     company_loc='Pune'
#     company_email='company@testyantra.com'
# emp1=Company()
# emp2=Company()
# print(Company.company_name,Company.company_loc,Company.company_email)

'''
Modification of properties:
    If we modify a property using class name modification will happen in object as well as class memory.

    If we modify a property using object name modification will happen in particular object memory. 

    Syntax:
        class_name.property_name=value
        object_name.property_name=value
'''
class Company:
    company_name='TestYantra'
    company_loc='Pune'
    company_email='company@testyantra.com'
emp1=Company()
emp2=Company()

Company.company_loc='Mumbai'
emp1.company_loc='Hyderabad'

print(Company.company_name,Company.company_loc,Company.company_email)
print(emp1.company_name,emp1.company_loc,emp1.company_email)
print(emp2.company_name,emp2.company_loc,emp2.company_email)

'''
Types of states:
(i)Class Method
    These are the members which are commen for all the object.
    Ex. Consider a class Bank
        Members such as bank_name,location,email,ifsc_code,etc are class members.

(ii)Object Method
    These are the members which are different for all the object.
    Ex. Consider a class Bank
        Members such as customer_name,phone_no,email,account_number,aadhar_num,PAN,etc are object members.

Ex.
'''
