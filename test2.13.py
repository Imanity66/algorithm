# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 21:51:36 2019

@author: Imanity
"""


input = ["(",1, "+", "(", 5, "*", 4, ")", ")"]
import operator
def arithetic_experssion_evaluation(terms):
    nums = []
    operators = []
    ops = {"+":operator.add,"-": operator.sub, "*":operator.mul, "/":operator.truediv}
    for i in terms:
        if i in ops:
            operators.append(i)
        elif i == ")":
           # right, left = nums.pop(), nums.pop()
            nums.append(ops[operators.pop()](nums.pop(), nums.pop()))
        elif i == "(":
            continue
        else:
            nums.append(i)
    return nums[0]


print(arithetic_experssion_evaluation(input))