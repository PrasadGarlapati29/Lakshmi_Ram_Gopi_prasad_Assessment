# Problem-1 : Small Calculator using Class

class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "add":
            print("Addition:", self.a + self.b)
        elif self.operation == "sub":
            print("Subtraction:", self.a - self.b)
        elif self.operation == "mul":
            print("Multiplication:", self.a * self.b)
        elif self.operation == "div":
            if self.b != 0:
                print("Division:", self.a / self.b)
            else:
                print("Error: Division by zero")
        else:
            print("Invalid Operation")

# Example Run
c1 = Calculator(10, 5, "add")
c1.calculate()


