def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Instructions", "-")

    print('''
Conversion 
- enter 'd' for converting distance
- enter 't' for converting time
- enter 'm' for converting mass
    ''')


def conversion_type():

    while True:
        response = input("What would you like being converted: ").lower()

         # grab response
        if response =="xxx":
            return response

        # check if it's a integer
        elif response in ['t', 'Time']:
            return "time"

        # check for an image
        elif response in ['d', 'length']:
            return "distance"

        # check  for text
        elif response in ["m", 'mass', 'weight']:
            return "mass"

        # if the response is invalid
        else:
            print("Please enter a physical quantity to convert")

def distance():
        distance_dict = {
            "mm": 1000,
            "cm": 100,
            "m": 1,
            "km": .001
        }

        # get amount and units (valid)
        amount = float(input("how much? "))
        from_unit = input("From Unit? ")
        to_unit = input("To Unit? ")

        # Look up value
        multiply_by = distance_dict[to_unit]
        standard = amount * multiply_by

        # divide to get our desired value
        divide_by = distance_dict[from_unit]
        solution = standard / divide_by

        answer = print(f"There are {solution} {to_unit} in {amount} {from_unit}")

        return answer

  # Display instructions if requested
want_instructions = input("Press <enter> to read the instructions  "
                          "or any key to continue")

if want_instructions == "":
    instructions()


while True:
    conversion = conversion_type()

    if conversion == "xxx":
        break

    if conversion == "distance":
        distance_ans = distance()
        print(distance_ans)





