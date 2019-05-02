# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:42:20 2019

@author: s140121038
"""




def cusped():
    limit = np.deg2rad(15) # 15 degrees approximation
    upper_slope = (y[0]-y[1])/(x[0]-x[1])
    lower_slope = (y[-1]-y[-2])/(x[-1]-x[-2])
    ml_slope = (ml[-1]-ml[-2]) / (x_upper[-1]-y_upper[-2])
    theta1 = np.arctan(upper_slope)-np.arctan(ml_slope)
    theta2 = np.arctan(ml_slope)-np.arctan(lower_slope)
    print(theta1, theta2, abs(theta1+theta2))
    
    if abs(theta1+theta2) <= limit:
        return True
    return False

cusped()