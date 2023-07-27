"""
Created on Wed Aug 17 09:12:30 2016
@author: Mohsen Feizabadi
"""

def HarmonicJacobian_cosine(T1,T2,t,A,B,fi_a,fi_b):
    
    import math
    import numpy
    
    J = numpy.zeros(shape=(1,6))
    J[0][0] = 1;
    J[0][1] = t;
    J[0][2] = math.cos((2*math.pi/T1)*t-fi_a);
    J[0][3] = math.cos((2*math.pi/T1)*t-fi_b);
    J[0][4] = A*math.sin((2*math.pi/T2)*t-fi_a);
    J[0][5] = B*math.sin((2*math.pi/T2)*t-fi_b);
    return J    
