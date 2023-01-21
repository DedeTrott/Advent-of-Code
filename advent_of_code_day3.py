# Import ascii_letters
from string import ascii_letters

# Getting the Data
with open("Files/day3.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

totalSum = 0
for rucksack in data:
    # find half
    half = len(rucksack)//2
    left = set(rucksack[:half])
    right = set(rucksack[half:])

    for priority, char in enumerate(ascii_letters):
        if char in left and char in right:
            totalSum += priority + 1

print("The answer to Part one is: ", totalSum)

j = 3
totalSum = 0
for i in range(0, len(data), 3):
    rucksacks = data[i:j]
    j += 3

    for priority, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            totalSum += priority + 1

print("The Answer to Part two: ", totalSum)