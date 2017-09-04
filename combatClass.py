# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:36:30 2017
@author: David
"""
from  scipy import *
from  pylab import *

class Combat():
    def __init__(self, Combatants, BattleMap):
        self.Combatants = Combatants
        self.BattleMap = BattleMap
        
        self.Initiative()
        self.Position()
        
    def Initiative(self):
        d20 = dice(20)        
        
        ci = []  
        
        for c in self.Combatants:
            ci = ci + [floor((c.AbilityScores[1] - 10) / 2) + d20.roll()]
        print(ci)

        def getKey(item):
            return item[0]
        
        if ci:
            ci, self.Combatants = zip(*sorted(zip(ci, self.Combatants), reverse=True, key = getKey))
    
    def Position(self):
        for c in self.Combatants:
            self.BattleMap.put(c.Position, c.Team)
            print(c.Team)
    
    def run(self):
        fight = True

        counter = 1        
        
        while fight:
            print("Turn:",counter)
            for c in self.Combatants:
                fight = c.Behaviour(self)
                
                if not fight:
                    break
                
            counter = counter + 1
            
        pause(1)    
            