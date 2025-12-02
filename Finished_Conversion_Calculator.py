# Functions

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Instructions", "-")
    print('''
Conversion:
  enter 'd' for converting distance
  enter 't' for converting time
  enter 'm' for converting mass


Valid Distance Units:
  mm (millimetre)
  cm (centimetre)
  m  (metre)
  km (kilometre)

Valid Mass Units:
  mg (milligrams)
  g  (grams)
  kg (kilograms)
  t  (tonnes)

Valid Time Units:
  s   (seconds)
  min (minutes)
  h   (hours)
  day (days)
''')


#Number Checker

def number_checker(question):
    while True:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print("Please enter a valid number.")

#Conversion type

def conversion_type():
    while True:
        response = input("What would you like to convert? (d/t/m): ").lower()

        if response == "xxx":
            return response
        elif response == "d":
            return "distance"
        elif response == "t":
            return "time"
        elif response == "m":
            return "mass"
        else:
            print("Please enter 'd', 't', 'm', or 'xxx' to exit.")

# Distance

def distance():
    distance_dict = {
        "mm": 1000,
        "cm": 100,
        "m": 1,
        "km": 0.001
    }

    amount = number_checker("How much? ")
    from_unit = input("From Unit? ").lower()
    to_unit = input("To Unit? ").lower()

    # Convert
    multiply_by = distance_dict[to_unit]
    standard = amount * multiply_by

    divide_by = distance_dict[from_unit]
    solution = standard / divide_by

    answer = f"There are {solution} {to_unit} in {amount} {from_unit}"
    return answer     

# Mass

def mass():
    mass_dict = {
        "mg": 1000000,
        "g": 1000,
        "kg": 1,
        "t": 0.001
    }

    amount = number_checker("How much? ")
    from_unit = input("From Unit? ").lower()
    to_unit = input("To Unit? ").lower()

    multiply_by = mass_dict[to_unit]
    standard = amount * multiply_by

    divide_by = mass_dict[from_unit]
    solution = standard / divide_by

    answer = f"There are {solution} {to_unit} in {amount} {from_unit}"
    return answer

#Time

def time():
    time_dict = {
        "s": 3600,
        "min": 60,
        "h": 1,
        "day": 1/24
    }

    amount = number_checker("How much? ")
    from_unit = input("From Unit? ").lower()
    to_unit = input("To Unit? ").lower()

    multiply_by = time_dict[to_unit]
    standard = amount * multiply_by

    divide_by = time_dict[from_unit]
    solution = standard / divide_by

    answer = f"There are {solution} {to_unit} in {amount} {from_unit}"
    return answer

# Main Rountine

statement_generator("The Ultimate Conversion Calculator", "*")

want_instructions = input("Press <enter> for instructions or any key to continue: ")
if want_instructions == "":
    instructions()

while True:
    conversion = conversion_type()

    if conversion == "xxx":
        break

    if conversion == "distance":
        print(distance())

    elif conversion == "mass":
        print(mass())

    elif conversion == "time":
        print(time())


