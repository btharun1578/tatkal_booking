class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length+self.width)*2
    
rectangle=Rectangle(5,4)
print(rectangle.perimeter())