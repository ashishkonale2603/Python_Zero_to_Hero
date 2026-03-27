# Packing and Unpacking

'''
Packing:

It is the process of combining the values into a collection.

Wrapping up the data/values togetherly inside a collection is called as Packing.
It can be done by using all the five collection datatypes.

There are two types of packing:
(1)Single Pack
(2)Double Pack
'''

'''
(1)Single Pack
    The process of combining the single values in the form of tuple is called as Single Packing.
    As it combines the values in the form of tuple it is alse called tuple packing.
    Syntax:
            def fname(*args):
                statement block
            fanme(val1,val2,...,valn)

    Ex.
            def single(*a):
                print(a)
            single(1,2,3,4,5,6,7,8,9,10)

(2)Double Pack
    it is the phenomenon of grouping key value pairs of the form of dictionary.
    As it combines the data in the form of dictionary, it is also called as dictionary packing.
    Syntax:
            def fname(**args):
                statement block
            fname(key=value)

    Ex.
        def store(**a,**b):
            print(a,b)
        store(a=20,b=10)
'''

'''
Q.  Differentiate between single pack and double pack.
    _____________________________________________________________________________
    |            single pack              |           double pack                |
    |----------------------------------------------------------------------------|
    |It collects positional arguments.    |It collects keyword arguments.        |
    |                                     |                                      |
    |Stores values in tuples.             |Stores values in dictionary.          |
    |                                     |                                      |
    |Symbol is *                          |Symbol is **                          |
    |_____________________________________|______________________________________|
'''