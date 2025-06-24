from helper import validation


user_input = ""
while user_input != "exit":
    user_input = input("Write how many days and to which unit, no spaces (20,h/m/s):")
    days_and_unit = user_input.split(",")
    dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validation(dictionary)

#     # for element in user_input.split(","):
#     #     validation()
