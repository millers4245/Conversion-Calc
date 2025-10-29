def mass():
    mass_dict = {
        "mg": 10,
        "g": 100,
        "kg": 1000
    }

    # get amount and units (valid)
    amount = float(input("how much? "))
    from_unit = input("From Unit? ")
    to_unit = input("To Unit? ")

    # Look up value
    multiply_by = mass_dict[to_unit]
    standard = amount * multiply_by

    divide_by = mass_dict[from_unit]
    solution = standard / divide_by




