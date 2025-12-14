# Solution for Day 3 of Advent of Code 2025
from dataclasses import dataclass

def solve_part_one(input_data):
    print("Advent of Code 2025 - Day 3: Part One - Find the maximum joltage with two batteries...")

    sum_joltage = 0
    
    for line in input_data.strip().splitlines():
        
        sequence = line.strip()

        first_joltage = find_max_joltage(sequence, 0, 1)
        second_joltage = find_max_joltage(sequence, first_joltage.index + 1, 0)
        
        combined_joltage = int(f"{first_joltage.joltage}{second_joltage.joltage}")
        sum_joltage += combined_joltage

    return sum_joltage


def find_max_joltage(sequence, start_index, end_offset):
    max_joltage = 0
    max_index = 0

    for i in range(start_index, len(sequence) - end_offset):
        current_joltage = int(sequence[i])
        if current_joltage > max_joltage:
            max_joltage = current_joltage
            max_index = i
            
    return BatteryJoltage(max_index, max_joltage)


@dataclass
class BatteryJoltage:
    index: int
    joltage: int


def solve_part_two(input_data):
    print("Advent of Code 2025 - Day 3: Part Two - Find the maximum joltage with X batteries...")
    
    sum_joltage = 0
    num_batteries = 12

    for line in input_data.strip().splitlines():

        sequence = line.strip()
        
        current_index = 0
        batteries = []

        for _ in range(num_batteries):
            battery = find_max_joltage(sequence, current_index, num_batteries - len(batteries) - 1)
            batteries.append(battery)
            current_index = battery.index + 1

        combined_joltage = "".join(str(battery.joltage) for battery in batteries)
        sum_joltage += int(combined_joltage)

    return sum_joltage
