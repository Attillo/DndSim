# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:35:44 2017
@author: David
"""
from  scipy import *
from  pylab import *

class Combatant():
    # Attack = [AttackBounus, Reach, DamageDice, NbrDice, DamageBonus]
    def __init__(self, HP, AC, Attack , AbilityScores = array(repeat(10,6)), Name = "Default", Team = 0):
        self.HP = HP
        self.AC = AC
        self.AttackBonus = Attack[0]
        self.Reach = Attack[1]
        self.DamageDice = Attack[2]
        self.NbrDice = Attack[3]
        self.DamageBonus = Attack[4]
        self.AbilityScores = array(AbilityScores)
        self.Name = Name
        self.Team = Team
        
    def Attack(self, Target):
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
        for c in Combat.Combatants:
            if c.Team != self.Team and c.HP > 0:
                self.Attack(c)
                return True
                
        return False
            
    
                
        
            
            