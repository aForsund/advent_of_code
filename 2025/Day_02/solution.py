
def solve_part_one(input_data):

    print("Advent of Code 2025 - Day 2: part one - Add up all of the invalid IDs...")

    # We're required to accumulate the sum of all the invalid IDs from all the ranges
    invalid_id_sum = 0

    # Split input by comma to get each range
    ranges = input_data.strip().split(',')

    # Iterate through each range and add up invalid IDs
    for r in ranges:
        if '-' in r:
            first, second = r.split('-')

            # If the second number is equal or less than the first, skip this range
            if int(second) <= int(first):
                continue

            for id in range(int(first), int(second) + 1):
                if is_invalid_id(id):
                    invalid_id_sum += id


    return invalid_id_sum


# Used in part one when we're only required to check if the sequence is repeated twice
def is_invalid_id(id):
    # Check if the provided id made only of some sequence of digits repeated twice
    id_str = str(id)
    length = len(id_str)
    if length % 2 == 0:
        half = length // 2
        if id_str[:half] == id_str[half:]:
            return True

    return False

def solve_part_two(input_data):
    print("Advent of Code 2025 - Day 2: part two - Add up all of the invalid IDs with stricter rules...")

    # We're required to accumulate the sum of all the invalid IDs from all the ranges
    invalid_id_sum = 0

    # Split input by comma to get each range
    ranges = input_data.strip().split(',')

    # Iterate through each range and add up invalid IDs
    for r in ranges:
        if '-' in r:
            first, second = r.split('-')

            # If the second number is equal or less than the first, skip this range
            if int(second) <= int(first):
                continue

            for id in range(int(first), int(second) + 1):
                if is_invalid_id_strict(id):
                    invalid_id_sum += id


    return invalid_id_sum

# Used in part two when we're required to check if the sequence is repeated X times
def is_invalid_id_strict(id):
    # Check if the provided id made only of some sequence of digits repeated X times (X >= 2)
    id_str = str(id)
    length = len(id_str)

    for sub_length in range(1, length // 2 + 1):
        if length % sub_length == 0:
            times = length // sub_length
            sub_sequence = id_str[:sub_length]
            if all(id_str[i*sub_length:(i+1)*sub_length] == sub_sequence for i in range(times)):
                if times >= 2:
                    return True

    return False