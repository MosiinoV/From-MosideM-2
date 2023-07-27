"""
Created on Tue Aug 16 17:00:17 2016
@author: Mohsen Feizabadi
"""

def L_ApproximationExpansion(a0,a1,T1,T2,t,A,B,C,D):
    
    import math

    L = a0 + a1*t + A*math.cos((2*math.pi/T1)*t) + B*math.sin((2*math.pi/T1)*t) + \
        C*math.cos((2*math.pi/T2)*t) + D*math.sin((2*math.pi/T2)*t);
    return L