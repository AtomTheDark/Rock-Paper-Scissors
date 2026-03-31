import time
import random
#val: The random choice of the program
#string: The user preferred one

wins_against = {
    "Rock":"Scissors",
    "Scissors":"Paper",
    "Paper":"Rock",
}

# Calculations hehe
def calc():
    possible_out_comes = ["Rock", "Paper", "Scissors"]
    return random.choice(possible_out_comes)


# Finding The Winner
def win_finder(string, val):
    if string == val:
        print("Draw")
    elif wins_against[string] == val:
        print("You win!")
    else:
        print("You lose!")


# noinspection DuplicatedCode
def rock(val):
    for i in range(3,0,-1):
        print(f"{i}{"."*i}" , end="\n" , flush=True)
        time.sleep(1)
    print(f"Rock - {val}")
    win_finder("Rock", val)


# noinspection DuplicatedCode
def paper(val):
    for i in range(3,0,-1):
        print(f"{i}{"."*i}" , end="\n" , flush=True)
        time.sleep(1)
    print(f"Paper - {val}")
    win_finder("Paper", val)


# noinspection DuplicatedCode
def scissors(val):
    for i in range(3,0,-1):
        print(f"{i}{"."*i}" , end="\n" , flush=True)
        time.sleep(1)
    print(f"Scissors - {val}")
    win_finder("Scissors", val)

#Main
def main():
    buffer = ""
    print("Welcome to Rock Paper Scissors!")
    print("Please enter a number between 1 and 3")
    for i in range(1,3+1,1):
        if i == 1:
            buffer = "Rock"
        elif i == 2:
            buffer = "Paper"
        elif i == 3:
            buffer = "Scissors"
        print(f"{i}.{buffer}")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Please enter a number between 1 and 3")
    if choice == 1:
        rock(calc())
    elif choice == 2:
        paper(calc())
    elif choice == 3:
        scissors(calc())

main()