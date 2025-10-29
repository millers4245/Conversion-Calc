def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Instructions", "-")

    print('''
Conversion 
enter 'd' for converting distance
enter 't' for converting time
enter 'm' for converting mass''')


def conversion_type():

    while True:
        response = input("What would you like being converted: ").lower()

        # exit code
        if response == "xxx":
            return response

        # check if it's time
        elif response in ['t', 'time']:
            return "time"

        # check if it's distance
        elif response in ['d', 'distance', 'length']:
            return "distance"

        # check if it's mass
        elif response in ["m", 'mass', 'weight']:
            return "mass"

        # if the response is invalid
        else:
            print("Please enter a valid physical quantity to convert")


def distance():
    distance_dict = {
        "mm": 1000,
        "cm": 100,
        "m": 1,
        "km": 0.001
    }

    # get amount and units
    amount = float(input("How much? "))
    from_unit = input("From Unit? ").lower()
    to_unit = input("To Unit? ").lower()

    # Look up value
    multiply_by = distance_dict[to_unit]
    standard = amount * multiply_by

    # divide to get value
    divide_by = distance_dict[from_unit]
    solution = standard / divide_by

    answer = f"There are {solution} {to_unit} in {amount} {from_unit}"
    print(answer)

    return answer


def mass():
    mass_dict = {
        "mg": 1000000,
        "g": 1000,
        "kg": 1,
        "t": 0.001
    }

    # get amount and units (valid)
    amount = float(input("How much? "))
    from_unit = input("From Unit? ").lower()
    to_unit = input("To Unit? ").lower()

    # Look up value for unit
    multiply_by = mass_dict[to_unit]
    standard = amount * multiply_by

    # Divide to get unit
    divide_by = mass_dict[from_unit]
    solution = standard / divide_by

    answer = f"There are {solution} {to_unit} in {amount} {from_unit}"
    print(answer)

    return answer


# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions  "
                          "or any key to continue: ")

if want_instructions == "":
    instructions()


while True:
    conversion = conversion_type()

    if conversion == "xxx":
        break

    if conversion == "distance":
        distance_ans = distance()
        print(distance_ans)

    elif conversion == "mass":
        mass_ans = mass()
        print(mass_ans)