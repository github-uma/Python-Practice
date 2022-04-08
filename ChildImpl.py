from ClassDemo import CalculatorDemo


class ChildImplementation(CalculatorDemo):
    num2 = 200

    def __init__(self):
        CalculatorDemo.__init__(self, 5, 10)

    def getDataImpl(self):
        return self.num2 + self.num + self.sumTwoNums()


obj = ChildImplementation()
print(obj.getDataImpl())
