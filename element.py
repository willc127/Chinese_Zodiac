def calculate_element(year):
    remainder = year % 10
    if remainder in [0, 1]:
        element = "Metal"
    elif remainder in [2, 3]:
        element = "Water"
    elif remainder in [4, 5]:
        element = "Wood"
    elif remainder in [6, 7]:
        element = "Fire"
    else:
        element = "Earth"

    print(f'Your element is {element.lower()}\n')
    return element
