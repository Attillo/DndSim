# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:14:31 2017
@author: David
"""
from  scipy import *
from  pylab import *

class dice():
    def __init__(self, sides = 6):
        self.sides = sides
        
    def roll(self, number = 1):
        return floor(rand(1,number) * self.sides + 1)
        
        