# class name
class Circle:
    pi = 3.14    # π
    # Method of the class -- Define an area method that takes two parameters (self and radius)
    def area(self, radius):
        # return area given formula π*r^2
        return self.pi * radius**2

# Class instance
circle = Circle()

# New variable .... and .... call the method --- Pizza examples! The only circles that matter tbh    
pizza_area = circle.area(16 / 2)   # radius = diameter / 2
print(pizza_area)
# output 200.96

