import math

class calculator:
    def __init__(self,a, b):
        self.a = a
        self.b = b
    
    def add(self):
        c = self.a + self.b
        return c
    
    def multiply(self):
        c = self.a * self.b
        return c

if __name__== '__main__':
    
    a = 4 # int(input("enter the first number "))
    b = 5 #int(input("enter the second number "))
    
    calc = calculator(a,b)
    ops = "add" # input("enter the operation as a string: ")
    if ops == "add":
        answer = calc.add()
        print("Answer is : ", answer)
    # elif ops == "multiply":
    #     answer = calc.multiply()
    #     print("Answer is :", answer)
    else:
        print(" Operation is not valid")

  


