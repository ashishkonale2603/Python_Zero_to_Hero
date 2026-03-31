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
class Company:
    company_name='TestYantra'
    company_loc='Pune'
    company_email='company@testyantra.com'
emp1=Company()
emp2=Company()
print(Company.company_name,Company.company_loc,Company.company_email)
