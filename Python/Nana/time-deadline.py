import datetime

user_input = input("Enter your goal and a deadline separated by comma: ")
input_list = user_input.split(", ")

goal = input_list[0]
deadline = datetime.datetime.strptime(input_list[1], "%d.%m.%Y")

time_to_deadline = deadline - datetime.datetime.today()

print(f"It's {time_to_deadline.days} to your deadline")
