import numpy as np
def chinese_zodiac(year):
    animal = ['Rat','Ox','Tiger','Rabbit', 'Dragon','Snake','Horse','Goat','Monkey','Rooster','Dog','Pig']
    diff = year - 1924
    a = np.floor(diff/12)
    i = int(diff-12*a)
    sign = animal[i]
    g1 = i+4
    if g1 >11:
        g1 = g1 -12
    g2 = g1+4
    if g2 >11:
        g2 = g2 -12
    guardian_animal1 = animal[g1]
    guardian_animal2 = animal[g2]
    bf = i + 5
    if bf >11:
        bf = bf -12
    best_friend = animal[bf]
    return print(sign, guardian_animal1, guardian_animal2, best_friend)

chinese_zodiac(1994)
