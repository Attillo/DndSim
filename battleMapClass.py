# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:05:15 2017
@author: David
"""
from  scipy import *
from  pylab import *

class BattleMap():
    def __init__(self, width = 10, height = 10):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(width)] for y in range(height)]
        
    def put(self, location, team):
        """
        Add combatant position, denote by team number 
        """

        row, col = location        
        
        self.map[row][col] = team
        
    def get(self, location):
        """
        Get team of position
        """
        
        row, col = location
        
        return self.map[row,col]