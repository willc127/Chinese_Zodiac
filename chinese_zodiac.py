import numpy as np
def chinese_zodiac(year):
    #Define the zodiac animals
    animal = ['Rat','Ox','Tiger','Rabbit', 'Dragon','Snake','Horse','Goat','Monkey','Rooster','Dog','Pig']
    #Calculate the difference between the year and reference (1924: Rat)
    diff = year - 1924
    #Calculate the index of the animal
    a = np.floor(diff/12)
    i = int(diff-12*a)
    sign = animal[i]
    print('Your zodiac animal is {}\n'.format(sign))
    
    #Determine the two guardian animals
    g1 = i+4
    if g1 >= 12:
        g1 = g1 - 12

    g2 = g1+4
    if g2 >= 12:
        g2 = g2 - 12
    guardian_animal1 = animal[g1]
    guardian_animal2 = animal[g2]
    print('Your guardian animals are {} and {}\n'.format(guardian_animal1, guardian_animal2))
    
    #Determine the best friend animal
    bf = i + 5
    if bf >11:
        bf = bf - 12
    best_friend = animal[bf]
    print('Your best friend animal is {}\n'.format(best_friend))
    
    #Determine the worst enemy animal
    en = i + 6
    if en >= 12:
        en = en - 12
    enemy = animal[en]
    print('Your worst enemy animal is {}\n'.format(enemy))

chinese_zodiac(1994)
