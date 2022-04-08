class CalculatorDemo:
    num = 100

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am in parameterized class constructor")


    def getData(self):
        print("I am in class method")

    def sumTwoNums(self):
        return self.firstNumber + self.secondNumber+CalculatorDemo.num


obj = CalculatorDemo(3,4)
print(obj.num)
print(obj.getData())
print(obj.sumTwoNums())
