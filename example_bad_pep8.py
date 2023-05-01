import pandas as pd
import os
import log

x = 1


class myrect:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def testFunc(var1, var2, var3):
    print('hello')


# comment
""" comment """
if __name__ == "__main__":
    print("hello world")
    rect = myrect(5, 4)
    print(rect.area())


# for testing yapf and black
x = {  'a':37,'b':42,

'c':927}

y = 'hello ''world'
z = 'hello '+'world'
a = 'hello {}'.format('world')
class foo  (     object  ):
  def f    (self   ):
    return       37*-+2
  def g(self, x,y=42):
      return y
def f  (   a ) :
  return      37+-+a[42-x :  y**3]