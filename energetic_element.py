def fixed_energetic_element(sign):
    fixed_energetic_elements = {
        'Rat': 'Water',
        'Ox': 'Earth',
        'Tiger': 'Wood',
        'Rabbit': 'Wood',
        'Dragon': 'Earth',
        'Snake': 'Fire',
        'Horse': 'Fire',
        'Goat': 'Earth',
        'Monkey': 'Metal',
        'Rooster': 'Metal',
        'Dog': 'Earth',
        'Pig': 'Water'
    }
    
    print(f'Your fixed energetic element is {fixed_energetic_elements[sign].lower()}\n')
    return fixed_energetic_elements.get(sign)
