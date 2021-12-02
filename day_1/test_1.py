array_of_ints = []

with open('data.txt') as my_file:
    array_of_ints = map(int, my_file.read().split("\n"))

previous_number = None
increased_number_count = 0

for current_number in array_of_ints:
    if previous_number and (current_number > previous_number):
        increased_number_count += 1

    previous_number = current_number

print(increased_number_count)