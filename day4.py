registration_number = input("Enter registration number: ")

total_inputs = int(input("Enter no of inputs: "))
data = []

for index in range(total_inputs):
    user_input = input("Enter input: ")

    if user_input.isdigit():
        data.append(int(user_input))
    else:
        data.append(user_input)

numbers = []
strings = []

num_count = 0
str_count = 0

for element in data:

    if type(element) == int:
        numbers.append(element)
        num_count = num_count + 1

    elif type(element) == str:
        if element != "":
            strings.append(element)
            str_count = str_count + 1

last_digit = int(registration_number[-1])

if last_digit % 2 == 0:

    reversed_numbers = []
    for i in range(len(numbers)-1, -1, -1):
        reversed_numbers.append(numbers[i])
    numbers = reversed_numbers

else:

    reversed_strings = []
    for i in range(len(strings)-1, -1, -1):
        reversed_strings.append(strings[i])
    strings = reversed_strings

print("Numbers list :", numbers)
print("Strings list :", strings)
print("Total numbers :", num_count)
print("Total strings :", str_count)
