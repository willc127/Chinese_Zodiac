from guardian_animals import guardian
from best_animals import best
from worst_animals import worst
from worse_animals import worse


def chinese_zodiac(year):
    # Define the zodiac animals
    animal = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
              'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']

    # Calculate the index of the animal sign through the difference between the year and reference (1924: Rat)
    i = (year - 1924) % 12

    # Determine the sign
    sign = animal[i]
    print(f'\nYour zodiac animal is {sign.lower()}')

    # Determine the guardian animals
    guardian_animals = guardian(sign)
    print(
        f"The guardian animals are {guardian_animals[0].lower()} and {guardian_animals[1].lower()}.")

    # Determine the index of the best friend animal
    best_animal = best(sign)
    print(f"The best friend animal is {best_animal.lower()}.")

    # Determine the worse enemy animal
    worse_animal = worse(sign)
    print(f"The worse enemy animal is {worse_animal.lower()}.")

    # Determine the worst enemy animal
    worst_animal = worst(sign)
    print(f"The worst enemy animal is {worst_animal.lower()}.")

    return sign, best_animal, guardian_animals[0], guardian_animals[1], worst_animal, worse_animal
