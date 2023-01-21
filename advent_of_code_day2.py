import re

A = "Rock"
B = "Paper"
C = "Scissor"
X = "Rock"
Y = "Paper"
Z = "Scissor"

rock_points = 1
paper_points = 2
scissor_points = 3
draw = 3
won = 6

my_points = 0
my_2_points = 0

with open("ay.txt") as file:
    opponentInput = [i for i in file.read().splitlines()]


outcomes = {
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6,
}

for i in opponentInput:
    my_points += outcomes[i]

print(my_points)

X = "lose"
Y = "draw"
Z = "win"

desired_outcomes = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7,
}

for i in opponentInput:
    my_2_points += desired_outcomes[i]

