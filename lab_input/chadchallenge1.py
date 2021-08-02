## input asking for user's name
user_name = input("Enter your username:")

## input asking what day of the week it is
day_of_week = input("Enter the current day of week:")

## Print statement that reads outputs of both inputs
print("Hello," + , user_name + "!", "Happy", day_of_week + "!")

# print, no concatenation
print("Hello, ",name,"! Happy ",day,"!",sep="")
# print with concatenation
print("Hello, " + name + "! Happy " + day + "!")
# print with .format method
print("Hello, {}! Happy {}!".format(name, day))
# Peng's solution!
# f string
print(f"Hello, {name}! Happy {day}!")
