def guardian(sign):
    guardian_animals = {
        'Rat': ['Dragon', 'Monkey'],
        'Ox': ['Snake', 'Rooster'],
        'Tiger': ['Horse', 'Dog'],
        'Rabbit': ['Goat', 'Pig'],
        'Dragon': ['Rat', 'Monkey'],
        'Snake': ['Ox', 'Rooster'],
        'Horse': ['Tiger', 'Dog'],
        'Goat': ['Rabbit', 'Pig'],
        'Monkey': ['Rat', 'Dragon'],
        'Rooster': ['Ox', 'Snake'],
        'Dog': ['Tiger', 'Horse'],
        'Pig': ['Rabbit', 'Goat']
    }
    return guardian_animals.get(sign)
