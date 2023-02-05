import numpy as np
from PIL import Image
from varname import nameof


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

    # Determine the best friend animal
    if i <= 6:
        bf = 1-i
    elif i > 6:
        bf = 13-i
    bff = animal[bf]
    print('Your best friend animal is {}\n'.format(bff))

    # Determine the worse enemy animal
    en = i + 6
    if en >= 12:
        en = en - 12
    worse = animal[en]
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

    # Get the images of the animals
    label = [sign, guardian_animal1, guardian_animal2, bff, worse, worst]
    name_label = ['sign', 'guardian_animal1',
                  'guardian_animal2', 'bff', 'worse', 'worst']
    img_size = "C:/Users/willi/OneDrive/Documentos/DataScience/portfolio/Chinese_Zodiac/Rat.jpg"
    img_size = Image.open(img_size)
    group_images = Image.new('RGB', (2*img_size.width, 3*img_size.height))

    for j in range(0, len(label)):
        img_dir = "C:/Users/willi/OneDrive/Documentos/DataScience/portfolio/Chinese_Zodiac/" + \
            label[j] + ".jpg"
        img = Image.open(img_dir)
        img.save('C:/Users/willi/OneDrive/Documentos/DataScience/portfolio/Chinese_Zodiac/' +
                 name + '_' + name_label[j] + '.jpg', 'JPEG')
        if j == 0:
            group_images.paste(img, (0, 0))
        elif j == 1:
            group_images.paste(img, (img.width, 0))
        elif j == 2:
            group_images.paste(img, (img.width, img.height))
        elif j == 3:
            group_images.paste(img, (0, img.height))
        elif j == 4:
            group_images.paste(img, (0, 2*img.height))
        elif j == 5:
            group_images.paste(img, (img.width, 2*img.height))
    group_images.show()

# Merge the images together


"""     group_images.paste(img_sign, (0, 0)) #dog
    group_images.paste(img_bff, (img_g1.width, 0)) #rabbit
    group_images.paste(img_g1, (img_g1.width, img_g1.height)) #tiger
    group_images.paste(img_g2, (0, img_g1.height)) #horse
    group_images.paste(img_en, (0, 2*img_g1.height)) #dragon
    group_images.paste(img_wst, (img_g1.width, 2*img_g1.height))
    group_images.save('C:/Users/willi/OneDrive/Documentos/DataScience/portfolio/Chinese_Zodiac/' + name + '_results.jpg', 'JPEG')  """


chinese_zodiac('Karina', 1995)
