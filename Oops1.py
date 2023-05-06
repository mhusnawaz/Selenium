# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purposes
# constructor name should be __init__
# new keyword is not required when you create an object

class Calculator:
    num = 100

    #default constructor
    def __init__(self, a, b):
        self.firstNumber= a
        self.secondNumber= b
        print('I am called automatically when object is created')


    def getData(self):
        print('I am now executing as method in class')


    def Summation(self):
        return self.firstNumber+ self.secondNumber+ Calculator.num

obj= Calculator(2, 3)
obj.getData()
print(obj.Summation())


obj1= Calculator(4, 5)
obj1.getData()
print(obj1.Summation())