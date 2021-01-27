# Please note that this code is minimal and is only meant for 􏰇→ demonstration.
# It contains no error checking, and the functions could be written in a 􏰇→ generalized fashion. I encourage you to rewrite this more formally 􏰇→ if you are familiar with programming.

##########
########## Please don't change this code. It will change for everyone on the class.
########## Thank you!!!!!!
##########
import math
import numpy as np


def vecLength(v):
    tempSum = 0.0
    for x in v:
        tempSum += x[0]**2
    return math.sqrt(tempSum)


def f(A, b, x, y):
    temp = np.matrix([[x], [y]])
    return np.matrix(np.dot(A, temp) - b)


def grad(A, b, x, y):
    vec = np.matrix([[x], [y]])
    return np.matrix(2 * np.dot(np.transpose(A), np.dot(A, vec) - b))


def main():
    gamma = .01
    A = np.matrix([[3, 1], [2, -1]])
    b = np.matrix([[-1], [1]])
    x = 0.5
    y = -0.5


    step = 0
    while vecLength(grad(A, b, x, y)) > .01:
        step += 1
        x = (np.matrix([[x], [y]]) - gamma * grad(A, b, x, y)).item(0)
        y = (np.matrix([[x], [y]]) - gamma * grad(A, b, x, y)).item(1)
        print("(x,y) = (", x, ", ", y, ")")
        print(
            "The magnitude squared (length) of the output of f, i.e.,||f(x,y)||^2=L(x,y) at step",
            step, " is ",
            vecLength(f(A, b, x, y))**2)
        print("The magnitude (length) of the gradient at step ", step, " is ",
              vecLength(grad(A, b, x, y)), '\n')


main()