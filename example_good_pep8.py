"""
This module is to show example of pylint
"""

class MyRect:
    """ This class is used for rectangle. """
    def __init__(self, width: float, height: float) -> None:
        """ init a rectangle

        :param float width: width of rectangle
        :param float height: height of rectangle
        """
        self.width = width
        self.height = height

    def compute_area(self) -> float:
        """compute area

        :return float: area = width * height
        """
        return self.width*self.height


if __name__ == "__main__":
    print("hello world")
    rect = MyRect(4,5)
    print(rect.compute_area())
