
class Rectangle:
    def  __init__(self, length, width):
     '''Initialise the Rectangle with the given side'''
     self.length = length
     self.width = width

    def area(self):
         return self.length*self.width
    
    def circumference(self):
        return 2*(self.length+self.width)
    
