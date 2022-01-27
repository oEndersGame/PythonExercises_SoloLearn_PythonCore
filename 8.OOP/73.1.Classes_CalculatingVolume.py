# Problem:
'''
Given a Rectangle class, create a program to take two integer numbers as input, assign them as the width and height of a Rectangle object and output the volume of the resulting rectangle.
class Rectangle:
def __init__(self, width, height):
     self.w = width
      self.h = height

Sample Input:
5
4
Sample Output:
20

NOTE: The volume of a rectangle is equal to its height multiplied by its width.
'''
#---------------------------------------------#

# CODE:

class Rectangle:

    def __init__(self, width, height):
        self.w = width
        self.h = height

    def vol(self):
        # return volume
        v = self.w * self.h
        return v


w = int(input())
h = int(input())

obj = Rectangle(w, h)

# call the function
print(obj.vol())
