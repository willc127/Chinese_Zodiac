#This script calculates the Chinese Zodiac sign, guardian animals, best friend, worse enemy, and worst animal for a given name and year.
# The calculation is based on a reference year of 1924 (the year of the Rat). The script uses the "numpy" library to perform the calculation. 
# The result is displayed in the console and saved in an image format in a folder named after the input name.  
# The script uses the "Pillow" library to merge and save the images. 
# The images are merged into one image with the sign and best friend animal in the first row, the guardian animals in the second row,
# and the worst and worse enemy animals in the third row.

import numpy as np
from PIL import Image
import os

def chinese_zodiac(name, year):
    # Define the zodiac animals
    animal = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
              'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']

    # Calculate the difference between the year and reference (1924: Rat)
    diff = year - 1924

    # Calculate the index of the animal sign
    a = np.floor(diff/12)
    i = int(diff-12*a)
    sign = animal[i]
    print('Your zodiac animal is {}\n'.format(sign))

    # Determine the index of the two guardian animals
    g1 = i+4
    if g1 >= 12:
        g1 = g1 - 12

    g2 = g1+4
    if g2 >= 12:
        g2 = g2 - 12

    guardian_animal1 = animal[g1]
    guardian_animal2 = animal[g2]
    print('Your guardian animals are {} and {}\n'.format(
        guardian_animal1, guardian_animal2))

    # Determine the index of the best friend animal
    if i <= 6:
        bf = 1-i
    elif i > 6:
        bf = 13-i
    best = animal[bf]
    print('Your best friend animal is {}\n'.format(best))

    # Determine the worse enemy animal
    wrs = i + 6
    if wrs >= 12:
        wrs = wrs - 12
    worse = animal[wrs]
    print('Your worse animal is {}\n'.format(worse))

    # Determine the worst animal
    if i <= 3:
        wst = 7 - i
    elif i >= 4 and i <= 9:
        wst = 19-i
    elif i >= 10 and i <= 11:
        wst = 31 - i

    if wst >= 12:
        wst = wst - 12
    worst = animal[wst]

    print('Your worst animal is {}\n'.format(worst))

    # Create a new folder to store the results
    results_PATH = 'C:/Users/willi/OneDrive/Documentos/DataScience/portfolio/Chinese_Zodiac/' + name + '_results/'
    os.makedirs(results_PATH, exist_ok=True)
    
    #Define the labels of each image
    label = [sign, best,
                  guardian_animal1, guardian_animal2, worst, worse]
    name_label = ['sign', 'best',
                  'guardian_animal1', 'guardian_animal2', 'worst', 'worse']
    
    #Define the size of the group images
    img_size = "C:/Users/willi/OneDrive/Documentos/DataScience/portfolio/Chinese_Zodiac/Animals/Rat.jpg"
    img_size = Image.open(img_size)
    group_images = Image.new('RGB', (2*img_size.width, 3*img_size.height))

    #Define the position of the group images
    for j in range(0, len(label)):
        img_dir = "C:/Users/willi/OneDrive/Documentos/DataScience/portfolio/Chinese_Zodiac/Animals/" + \
            label[j] + ".jpg" #Define the path of the image
        img = Image.open(img_dir) #Open the image
        img.save(results_PATH + name + '_' + name_label[j] + '.jpg', 'JPEG') #Save the image
        
        # Merge the images together
        if j < 2:
            group_images.paste(img, (img.width*j, 0)) # Add the image to the group image (first row)
        elif j < 4:
            group_images.paste(img, (img.width*(j-2), img.height)) # Add the image to the group image (second row)
        elif j < 6:
            group_images.paste(img, (img.width*(j-4), 2*img.height)) # Add the image to the group image (third row)
            
    group_images.save(results_PATH + name + '_results.jpg', 'JPEG') #Save the group image

#Call the function
chinese_zodiac('Karina', 1995) 


