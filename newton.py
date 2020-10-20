#AMS129/joel-ams129-18fall/hw5/newton.py
#AMS129 Fall 2018 hw5 Newton
#Joel Aoto
#MWF: 9:20 AM

#--------------------------------------------------------------------#
# Define the functions                                               #
# Defines: function newtons(f, df, initial_guess, threshold)         #
#--------------------------------------------------------------------#
import numpy as np

def newtons(f, df, initial_guess, threshold, dx):
    fdf = f / df
    new_approx = initial_guess
    next_approx = 0.
    width = 20  
    next_approx = new_approx - fdf
    return next_approx

