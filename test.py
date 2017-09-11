# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:53:23 2017
@author: David
"""
from  scipy import *
from  pylab import *

import diceClass
import battleMapClass
import combatClass
import combatantClass

d6 = dice(6)

Map = BattleMap(1000,1000)

Zombie1 = Combatant((4,4),22,8,[3,5,d6,1,1],[13,6,16,3,6,5], 4,"Zombie1",1)
Zombie2 = Combatant((4,100),22,8,[3,5,d6,1,1],[13,6,16,3,6,5], 4,"Zombie2",2)

TestCombat = Combat([Zombie1, Zombie2], Map)

TestCombat.run()

#a = Zombie1.Move(TestCombat)

