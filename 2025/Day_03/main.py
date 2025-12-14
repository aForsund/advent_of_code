# Check if input.txt exists, print a message and abort if not

import os
import sys
import solution

input_path = "input.txt"

if not os.path.exists(input_path):
    print(f"Error: {input_path} not found.")
    sys.exit(1)

print("Reading input.txt...")
with open(input_path, "r") as file:
    data = file.read()

# Check which solution parts are available
has_part_one = hasattr(solution, "solve_part_one")
has_part_two = hasattr(solution, "solve_part_two")

if has_part_one and has_part_two:
    print("Which part do you want to solve?")
    print("1: Part 1")
    print("2: Part 2")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        answer = solution.solve_part_one(data)
        print("Answer (Part 1):", answer)
    elif choice == "2":
        answer = solution.solve_part_two(data)
        print("Answer (Part 2):", answer)
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)
elif has_part_one:
    answer = solution.solve_part_one(data)
    print("Answer (Part 1):", answer)
elif has_part_two:
    answer = solution.solve_part_two(data)
    print("Answer (Part 2):", answer)
else:
    print("No solution function found in solution.py.")
    sys.exit(1)
