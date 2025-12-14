# The dial has a min value of 0 and a max value of 99
min_value = 0
max_value = 99

def solve_part_one(input_data):

    print("Advent of Code 2025 - Day 1: Part One - Checking how many times the dial lands on 0...")

    # The dial starts at position 50
    position = 50    
    
    # The number of times the dial lands on 0
    count = 0

    # Process each line of input
    for line in input_data.strip().splitlines():
        direction, value = line[0], int(line[1:])
        # Make sure the dial is not turned more than a full rotation
        if value > 100:
            value = value % 100
        # Turn the dial and check if it lands on 0
        position = turn_dial(position, direction, value)
        if position == 0:
            count += 1

    return count

def solve_part_two(input_data):

    print("Advent of Code 2025 - Day 1: Part Two - Checking how many times the dial is at 0...")

    # The dial starts at position 50
    position = 50

    # The number of times the dial is at 0 during turns
    count = 0

    # Process each line of input
    for line in input_data.strip().splitlines():
        direction, value = line[0], int(line[1:])
        # Make sure the dial is not turned more than a full rotation
        if value > 100:
            # Add the counts the dial would have landed on 0 in full rotations
            full_rotations = value // 100
            count += full_rotations
            value = value % 100
        
        new_position = turn_dial(position, direction, value)
        # Check if the dial is or crosses 0 during the turn
        if direction == 'R':
            if position < new_position:
                if position < 0 <= new_position:
                    count += 1
            else:
                if position < 0 or new_position >= 0:
                    count += 1
        elif direction == 'L':
            if position > new_position:
                if new_position <= 0 < position:
                    count += 1
            else:
                if position > 0 or new_position <= 0:
                    count += 1
        
        position = new_position

    return count

def turn_dial(current_position, direction, value):
    if direction == 'R':
        new_position = current_position + value
        if new_position > max_value:
            new_position = new_position - 100
    elif direction == 'L':
        new_position = current_position - value
        if new_position < min_value:
            new_position = new_position + 100
    return new_position

