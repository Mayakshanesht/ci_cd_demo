import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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
    
    a = int(input("enter the first number "))
    b = int(input("enter the second number "))
    
    calc = calculator(a,b)
    ops = input("enter the operation as a string: ")
    if ops == "add":
        answer = calc.add()
        print("Answer is : ", answer)
    # elif ops == "multiply":
    #     answer = calc.multiply()
    #     print("Answer is :", answer)
    else:
        print(" Operation is not valid")

  


