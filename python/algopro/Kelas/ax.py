# Create calculator
class Calculator:
    def __init__(self, value):
        self.value = value
    def power(self, power):
        return self.value ** power
    def product(self, product):
        return self.value * product
    def sum(self, sum):
        return self.value + sum
    def difference(self, difference):
        return self.value - difference
    def quotient(self, quotient):
        return self.value / quotient
    def remainder(self, remainder): 
        return self.value % remainder
    def sqrt(self, sqrt):
        return self.value ** (1/sqrt)
    def log(self, log):
        return self.value ** (1/log)

a=55
b=3
calc = Calculator(a)
print(calc.sum(b))