# -*- coding: utf-8 -*-

class fruits:
    def __init__(self, price):
        self.price = price
obj=fruits(50)
 
obj.quantity=10
obj.bags=2
 
print(obj.quantity+len(obj.__dict__))


class change:
    def __init__(self, x, y, z):
        self.a = x + y + z
 
x = change(1,2,3)
y = getattr(x, 'a')
setattr(x, 'a', y+1)
print(x.a)


class Demo:
    def __init__(self):
        pass
 
    def test(self):
        print(__name__)
 
obj = Demo()
obj.test()


class test:
     def __init__(self,a):
         self.a=a
 
     def display(self):
         print(self.a)
obj=test()
obj.display()