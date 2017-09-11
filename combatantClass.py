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
            
    def checkAdjacent(self, Combat):
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
                
        combatants = Combat.Combatants
        targetFound = False   
        target = None
        
        for c in combatants:
            for a in adjacent:
                if c.Position == a and c.Team != self.Team and c.HP > 0:
                    targetFound = True
                    target = c
                    break
            if targetFound:
                break
            
        return target
        
            
    def Behaviour(self, Combat):
        self.Move(Combat)
        target = self.checkAdjacent(Combat)
            
        if target != None:
            self.Attack(target)
                
        return False
            
    def Move(self, Combat):
        row0, col0 = self.Position  
        closestDist = inf
        closestTarget = None
        
        for c in Combat.Combatants:
            if c.Team != self.Team and c.HP > 0:
                row1, col1 = c.Position                
                temp = sqrt((row1 - row0)**2 + (col1 - col0)**2)
                
                if temp < closestDist:
                    closestDist = temp
                    closestTarget = c
        
        if closestTarget == None:
            return False
            
        maxMove = self.Movement
        row1, col1 = closestTarget.Position
        
        for n in range(1,maxMove+1):
            row0, col0 = self.Position
            
            rowDist = abs(row1 - row0)
            colDist = abs(col1 - col0)
            
            if rowDist >= colDist and rowDist > 1:
                self.Position = (row0 + sign(row1 - row0), col0)
                print(self.Name,"moved to",self.Position)
                
            elif colDist > rowDist and colDist > 1:
                self.Position = (row0, col0 + sign(col1 - col0))
                print(self.Name,"moved to",self.Position)
                
        return True
        
    def Continue(self, Combat):
#        if self.HP == 0:
#            return False
#        
        enemyLeft = False
        for c in Combat.Combatants:
            if c.Team != self.Team and c.HP > 0:
                enemyLeft = True
                
        return enemyLeft
        
            