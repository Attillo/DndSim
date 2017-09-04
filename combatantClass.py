# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:35:44 2017
@author: David
"""
from  scipy import *
from  pylab import *

class Combatant():
    # Attack = [AttackBounus, Reach, DamageDice, NbrDice, DamageBonus]
    def __init__(self, Position, HP, AC, Attack , AbilityScores = array(repeat(10,6)), Movement = 6, Name = "Default", Team = 0):
        self.Position = Position        
        self.HP = HP
        self.AC = AC
        self.AttackBonus = Attack[0]
        self.Reach = Attack[1]
        self.DamageDice = Attack[2]
        self.NbrDice = Attack[3]
        self.DamageBonus = Attack[4]
        self.AbilityScores = array(AbilityScores)
        self.Movement = Movement
        self.Name = Name
        self.Team = Team
        
    def Attack(self, Target):
        if self.HP == 0:
            return
            
        d20 = dice(20)
        
        toHit = d20.roll() + self.AttackBonus        
        damage = sum(self.DamageDice.roll(self.NbrDice)) + self.DamageBonus 
        
        (hit, damageDealt) = Target.Hit(toHit, damage)
        
        print(self.Name, "attacks", Target.Name)
        print("Hit:", hit)
        print("Damage:",damageDealt)
        print("Remaining HP:",Target.HP)
        
    def Hit(self, toHit, damage):
        if toHit < self.AC:
            return (False, 0)
        else:
            self.HP = self.HP - damage
            if self.HP < 0:
                self.HP = 0
                
            return (True, damage)
            
    def Behaviour(self, Combat):
        adjacent = []
        row, col = self.Position        
        
        adjacent = adjacent +  [(row -1, col)]
        adjacent = adjacent +  [(row -1, col -1)]
        adjacent = adjacent +  [(row -1, col +1)]
        adjacent = adjacent +  [(row , col -1)]
        adjacent = adjacent +  [(row , col +1)]
        adjacent = adjacent +  [(row +1, col)]
        adjacent = adjacent +  [(row +1, col -1)]
        adjacent = adjacent +  [(row +1, col +1)]
    
        for i in range(7,-1,-1):
            if adjacent[i][0] < 0 or adjacent[i][0] > Combat.BattleMap.height -1:
                del adjacent[i]
            elif adjacent[i][1] < 0 or adjacent[i][1] > Combat.BattleMap.width -1: 
                del adjacent[i]
                
        return adjacent
#        distances = []        
#        x0, y0 = self.Position        
#        
#        for c in Combat.Combatants:
#            if c.Team == self.Team or c.HP <= 0:
#                distances = distances + nan
#            else
#                x1, y1 = c.Position
#                distances = distances + sqrt( (x1 - x0)**2 + (y1 - y0)**2 )
#
#        distances = array(distances)
#        closest = distances.argmin()
#        
#        Target = Combat.Combatants(closest)
#        
#        if distances(closest) > (self.Reach * 1.5):
#            self.Move(Target)
#     
#        for c in Combat.Combatants:              
#            if c.Team != self.Team and c.HP > 0:
#                self.Attack(c)
#                return True
                
        return False
            
            
            