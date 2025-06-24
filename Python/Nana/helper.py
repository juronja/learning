def days_to_units(days, unit):
    if unit == "h":
        return f"{days} days are {days * 24} hours"
    elif unit == "m":
        return f"{days} days are {days * 24 * 60} minutes"
    elif unit == "s":
        return f"{days} days are {days * 24 * 60 * 60} seconds"
    else:
        return "unsupported unit"


def validation(dictionary):
    try:
        days_to_integer = int(dictionary["days"])
        if days_to_integer > 0:
            print(days_to_units(days_to_integer, dictionary["unit"]))
        elif days_to_integer <= 0:
            print("zero or negative number not allowed")
    except ValueError:
        print("Input is not a integer")
