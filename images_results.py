def animal_images(name, sign, best_animal,guardian_animals1, guardian_animals2, worst_animal, worse_animal):

    from PIL import Image
    import os

    # Create a new folder to store the results
    results_PATH = 'C:/Users/willi/OneDrive/Documentos/DataScience/portfolio/Chinese_Zodiac/' + name + '_results/'
    os.makedirs(results_PATH, exist_ok=True)

    # Define the labels of each image
    label = [sign, best_animal,
                guardian_animals1, guardian_animals2, worst_animal, worse_animal]
    name_label = ['sign', 'best','guardian_animal1', 'guardian_animal2', 'worst', 'worse']

    # Define the size of the group images
    img_size = "C:/Users/willi/OneDrive/Documentos/DataScience/portfolio/Chinese_Zodiac/Animals/Rat.jpg"
    img_size = Image.open(img_size)
    group_images = Image.new('RGB', (2*img_size.width, 3*img_size.height))

    # Define the position of the group images
    for j in range(0, len(label)):
        img_dir = "C:/Users/willi/OneDrive/Documentos/DataScience/portfolio/Chinese_Zodiac/Animals/" + label[j] + ".jpg"  # Define the path of the image
        img = Image.open(img_dir)  # Open the image
        img.save(results_PATH + name + '_' + name_label[j] + '.jpg', 'JPEG')  # Save the image

        # Merge the images together
        if j < 2:
            # Add the image to the group image (first row)
            group_images.paste(img, (img.width*j, 0))
        elif j < 4:
            # Add the image to the group image (second row)
            group_images.paste(img, (img.width*(j-2), img.height))
        elif j < 6:
            # Add the image to the group image (third row)
            group_images.paste(img, (img.width*(j-4), 2*img.height))

    group_images.save(results_PATH + name + '_results.jpg','JPEG')  # Save the group image
