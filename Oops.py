class Calculator:
    num = 100

    # Default constructor
    def __init__(self):
        print('I am called automatically when object is created')

    def getData(self):
        print('I am now executing method in class')


obj = Calculator()      # Syntax to create objects in python
obj.getData()
print(obj.num)        # int object is NOT callable so use print()


