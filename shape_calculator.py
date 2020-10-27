### My solution 

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ("*" * self.width + "\n")  * self.height 
    
    def get_amount_inside(self, another_shape):
        width_inside = self.width // another_shape.width
        height_inside = self.height // another_shape.height
        return width_inside * height_inside

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        new_width = str(self.width)
        new_height = str(self.height)
        if new_width == new_height:
            return 'Square(side=' + new_width + ')'
        else:
            return 'Mis-shaped Square(width=' + new_width + ',height=' + new_height + ')'
