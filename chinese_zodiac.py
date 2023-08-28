from zodiac import chinese_zodiac
from images_results import animal_images
from energetic_element import fixed_energetic_element
from element import calculate_element

name = input('What is your name? ')
year = int(input('What year were you born? '))

# Call the function
sign, best_animal, guardian_animals1, guardian_animals2, worst_animal, worse_animal = chinese_zodiac(year)
calculate_element(year)
animal_images(name, sign, best_animal, guardian_animals1, guardian_animals2, worst_animal, worse_animal)
