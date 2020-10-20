#AMS129/joel-ams129-18fall/hw5/main.py
#AMS129 Fall 2018 hw5 Newton
#Joel Aoto
#MWF: 9:20 AM
#--------------------------------------------------------------------#
# main.py                                                            #
# Defines: function my_f, my_df                                      #
#--------------------------------------------------------------------#
import numpy as np
from newton import newtons
def my_f(x):
    f = 2.*x**7 + 4.*x**5 - 2.*x**3 + 3.*x + 1.
    return f

def my_df(x):
    df = 14.*x**6 + 20.*x**4 - 6.*x**2 + 3.
    return df

def run_newton(x, y, n):
    dx = 0.
    f = my_f(x)
    df = my_df(x)
    threshold = 1.E-8
    x_o = x
    x_n = y
    new_n = 0
    new_o = x_o
    dx = abs(x_n - x_o)
    width = 2
    print(" ", n,"|"," ".rjust(width,' '), x_o, "|"," ".rjust(width,' '),dx)
    n = n + 1
    if dx > threshold:
        new_n = newtons(my_f(x_o), my_df(x_o), x_o, threshold, dx)
        return run_newton(new_n, new_o, n)
    else:
        return new_n

initial_n = 0
initial_guess = 10.
initial_approx = 0.
print("  n|                     x|                    dx")
print("-------------------------------------------------")

run_newton(initial_guess, initial_approx, 0)



