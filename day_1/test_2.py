FILE = "data.txt"

def get_array_of_ints_from(file):
    array_of_ints = []

    with open(file) as my_file:
        array_of_ints = map(int, my_file.read().split("\n"))

    return array_of_ints

def has_increased_sum(previous_sum, current_sum):
    return (previous_sum and (current_sum > previous_sum))

def get_increased_sum_count_of(array_of_ints):
    previous_sum = None
    increased_sum_count = 0
    array_of_sum_lenght = len(array_of_ints) - 2

    for index in range(array_of_sum_lenght):
        current_sum = sum(array_of_ints[index:index+3])

        if has_increased_sum(previous_sum, current_sum):
            increased_sum_count += 1

        previous_sum = current_sum

    return increased_sum_count

if "__main__":
    array_of_ints = get_array_of_ints_from(FILE)
    increased_sum_count = get_increased_sum_count_of(array_of_ints)
    print(increased_sum_count)