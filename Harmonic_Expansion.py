"""
Created on Tue Aug 16 17:13:34 2016
@author: Mohsen Feizabadi
"""
import os
import numpy
import math
from numpy.linalg import inv
os.system('cls')
print('******* HARMONIC LEAST SQURE EXPANSION TERM *******')

from HarmonicJacobian_Expansion import HarmonicJacobian_Expansion
from L_ApproximationExpansion import L_ApproximationExpansion

import Tkinter as tk
import tkFileDialog as filedialog

root = tk.Tk()
root.withdraw()
input_file = open(filedialog.askopenfilename(), "r")
data = numpy.loadtxt(input_file)

num_lines = sum(1 for line in data)

t = numpy.zeros(shape=(num_lines,1))
F_obs = numpy.zeros(shape=(num_lines,1))

for i in range(num_lines):
    t[i] = data[i][0]
    F_obs[i] = data[i][1] 

T1 = int(input('What is the Annual Period: '))
T2 = int(input('What is the Semiannual Period: '))

X = numpy.zeros(shape=(6,1))
App_value = numpy.zeros(shape=(6,1))
Jacob = numpy.zeros(shape=(num_lines,6))
F = numpy.zeros(shape=(num_lines,1))  

Iteration = 1
error = 1
while error > 10e-5:
    App_value[0] = X[0]     # X[0] = 0  a0
    App_value[1] = X[1]     # X[1] = 0  a1
    App_value[2] = X[2]     # X[2] = 0  A
    App_value[3] = X[3]     # X[3] = 0  B
    App_value[4] = X[4]     # X[4] = 0  C
    App_value[5] = X[5]     # X[5] = 0  D
    for i in range(num_lines):
        Jacob[i][:] = HarmonicJacobian_Expansion(T1,T2,t[i])
        F[i] = F_obs[i] - L_ApproximationExpansion(App_value[0],App_value[1],T1,T2,t[i],\
                                    App_value[2],App_value[3],App_value[4],App_value[5])

    X = inv(Jacob.T.dot(Jacob)).dot(Jacob.T.dot(F))
    X = X + App_value 
    Iteration = Iteration+1;
    error1 = abs(abs(X[0])-abs(App_value[0]));
    error2 = abs(abs(X[1])-abs(App_value[1]));
    error3 = abs(abs(X[2])-abs(App_value[2]));
    error4 = abs(abs(X[3])-abs(App_value[3]));
    error5 = abs(abs(X[4])-abs(App_value[4]));
    error6 = abs(abs(X[5])-abs(App_value[5]));
    error = ((error1**2+error2**2+error3**2+error4**2+error5**2+error6**2)/6)**0.5

Bias = X[0]
Trend = X[1]
Annual_Amp = (X[2]**2+X[3]**2)**0.5
Semiannual_Amp = (X[4]**2+X[5]**2)**0.5
Annual_Phase = 2*math.atan(X[3]/(X[2]+Annual_Amp))
#Annual_Phase = math.atan(X[3]/X[2])
Semiannual_Phase = 2*math.atan(X[5]/(X[4]+Semiannual_Amp))
#Semiannual_Phase = math.atan(X[5]/X[4])
Annual_Phase = Annual_Phase*180/math.pi;
Semiannual_Phase = Semiannual_Phase*180/math.pi;
if Annual_Phase<0: 
   Annual_Phase = 360+Annual_Phase;
if Semiannual_Phase<0:
   Semiannual_Phase = 360+Semiannual_Phase;

print('-----------------------------------------')
print('Iterations = ') , Iteration
print('-----------------------------------------')
print('Bias = ') , Bias
print('Trend = ') , Trend
print('Annual amplitude = ') , Annual_Amp
print('Annual phase = ') , Annual_Phase
print('Semiannual amplitude = ') , Semiannual_Amp
print('Semiannual phase = ') , Semiannual_Phase
print('-----------------------------------------')

