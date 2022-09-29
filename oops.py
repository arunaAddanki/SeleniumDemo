#class is a blueprint for creating objects
#methods,class variables,instance variables,constructor etc
#objects for classes


#self keyword is mandetory for calling variable names into methods
#class variables and instance variables(attached to object) are used for whole different purpose
#constructor name should be unique __init__
#new keyword is not required when you create an object

class Calculator:
    num = 1000 #Class Variable

    def __init__(self, a, b):
        self.a=a #instance variable
        self.b=b #instance variable
        print("I am called automaticaly when an object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.a+self.b+Calculator.num

obj = Calculator(2,3)
obj.getData()
print(obj.num)
print(obj.Summation())

obj1 = Calculator(10,20)
obj1.getData()
print(obj1.num)
print(obj1.Summation())