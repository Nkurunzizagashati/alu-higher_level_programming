#!/usr/bin/python3
# a function that returns the list of available attributes and methods of an object
''' this program will print the list of available attributes and methods of an object '''


class List:
    ''' we will not pass attributes to this class so we will use pass to avoid errors '''
    pass
    
    def lookup(obj):
        ''' this function or module is the one which will helps us to print the list of available attribute and methods '''
        return dir(obj)
