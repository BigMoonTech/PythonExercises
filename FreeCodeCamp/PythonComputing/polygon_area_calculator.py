class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        output = ''
        width = self.width
        height = self.height

        if width > 50 or height > 50:
            return "Too big for picture."
        else:
            for h in range(height):
                for w in range(width):
                    output += '*'
                output += '\n'
        return output

    def get_amount_inside(self, shape):
        first_area = self.get_area()
        insert_area = shape.get_area()
        return first_area // insert_area


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f'Square(side={self.height})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
