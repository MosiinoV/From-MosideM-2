"""
Created on Wed Aug 17 09:15:33 2016
@author: Mohsen Feizabadi
"""

def L_ApproximationCosine(a0,a1,T1,T2,t,A,B,fi_a,fi_b):
    
    import math

    L = a0 + a1*t + A*math.cos((2*math.pi/T1)*t-fi_a) + B*math.cos((2*math.pi/T2)*t-fi_b) 
    return L    