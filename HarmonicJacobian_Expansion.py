"""
Created on Tue Aug 16 17:10:54 2016
@author: Mohsen Feizabadi
"""

def HarmonicJacobian_Expansion(T1,T2,t):
    
    import math
    import numpy
    
    J = numpy.zeros(shape=(1,6))
    J[0][0] = 1;
    J[0][1] = t;
    J[0][2] = math.cos((2*math.pi/T1)*t);
    J[0][3] = math.sin((2*math.pi/T1)*t);
    J[0][4] = math.cos((2*math.pi/T2)*t);
    J[0][5] = math.sin((2*math.pi/T2)*t);
    return J