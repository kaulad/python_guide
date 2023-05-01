import pandas as pd
x = 1



class myrect:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height


# comment
''' comment '''
if __name__ == "__main__":
    print("hello world")
    rect = myrect(5,4)
    print(rect.area())