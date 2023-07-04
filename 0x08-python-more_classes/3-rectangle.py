#!/usr/bin/python3
'''0-rectangle.py'''


class Rectangle:
    '''Defines rectangle'''

    def __init__(self, width=0, height=0):
        '''Initialise instance'''
        '''Instance Arguments'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Width method'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets rectangles width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Height method'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets rectangles width'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Defines the area of the rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Finds the permeter of the rectangle'''
        if self.width == 0 or self.height == 0:
            perim = 0
        else:
            perim = 2 * (self.width + self.height)
        return perim

    def __str__(self):
        '''String representation of object'''
        if self.width == 0 or self.height == 0:
            return ''
        result = ''
        for i in range(self.height - 1):
            result += "#" * self.width + "\n"
            if i == self.height - 2:
                result += "#" * self.width
        return result
