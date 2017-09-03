# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:36:30 2017
@author: David
"""
from  scipy import *
from  pylab import *

class Combat():
    def __init__(self, Team1, Team2):
        self.Team1 = Team1
        self.Team2 = Team2
        
        self.Initiative()
        
    def Initiative(self):
        
        ci = []  
        
        for c in self.Team1:
            ci = ci + [floor((c.AbilityScores[1] - 10) / 2)]
        
        if ci:
            ci, self.Team1 = zip(*sorted(zip(ci, self.Team1), reverse=True))
        
        ci = []        
        
        for c in self.Team2:
            ci = ci + [floor((c.AbilityScores[1] - 10) / 2)]
        
        if ci:
            ci, self.Team2 = zip(*sorted(zip(ci, self.Team2), reverse=True))
        