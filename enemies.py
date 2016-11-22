# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice
def iseasy(x):
    for i in range (2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
class Enemy(Attacker):
    def __init__ (self):
        self.experience = (10 * self._attack + self._health)//10


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_monster_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def __init__(self):
        self.object = 1
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'зелёный'
        super().__init__()
        

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 8
        self._color = 'красный'
        super().__init__()

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 150
        self._attack = 12
        self._color = 'черный'
        super().__init__()


    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
class Troll(Enemy):
    def __init__(self):
        self.object=2
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer
class BrownTroll(Troll):
    def __init__(self):

        self._health = 50
        self._attack = 7
        self._color = 'коричневый'
        super().__init__()

    def question(self):
        x = randint(1,5)
        self.__quest = "угадай число от 1 до 5"
        self.set_answer(x)
        return self.__quest
class BlueTroll(Troll):
    def __init__(self):

        self._health = 50
        self._attack = 10
        self._color = 'синий'
        super().__init__()
    def question(self):
        x = randint(1,100)
        self.__quest = str(x) + " - это число простое?"
        self.set_answer(iseasy(x))
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon, BrownTroll,BlueTroll]
