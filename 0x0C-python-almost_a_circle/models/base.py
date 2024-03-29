#!/usr/bin/python3
'''This class will be the “base” of all other classes in this project'''


class Base:
    '''The goal of it is to manage id attribute
        in all your future classes and to avoid
        duplicating the same code (by extension, same bugs)
    '''
    '''Class attribute'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialization of instances'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
