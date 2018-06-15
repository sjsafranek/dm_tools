import random

def rollDice(n=1, d=2):
    return sum([rollDie(d)for _ in range(n)])

def rollDie(d=2):
    return random.randint(1,d)

def d4(n=1):
    return rollDice(n, 4)

def d6(n=1):
    return rollDice(n, 6)

def d8(n=1):
    return rollDice(n, 8)

def d10(n=1):
    return rollDice(n, 10)

def d12(n=1):
    return rollDice(n, 12)

def d20(n=1):
    return rollDice(n, 20)

def d100(n=1):
    return rollDice(n, 100)


class Dice(object):

    def rollDice(self, n=1, d=2):
        return sum([rollDie(d)for _ in range(n)])

    def rollDie(self, d=2):
        return random.randint(1,d)

    def d4(self, n=1):
        return rollDice(n, 4)

    def d6(self, n=1):
        return rollDice(n, 6)

    def d8(self, n=1):
        return rollDice(n, 8)

    def d10(self, n=1):
        return rollDice(n, 10)

    def d12(self, n=1):
        return rollDice(n, 12)

    def d20(self, n=1):
        return rollDice(n, 20)

    def d100(self, n=1):
        return rollDice(n, 100)

dice = Dice()
