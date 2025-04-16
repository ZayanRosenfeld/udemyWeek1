import random
print("Welcome to the rock, paper, scissors game");

random_num = random.randint(1, 3);
print("Your choice now!");
print("1 - Rock");
print("2 - Paper");
print("3 - Scissors");
chosen_num = int(input("Type your choice: "));

choices = {1 : "Rock", 2 : "Paper", 3 : "Scissors"}
print(f"You chose: {choices[chosen_num]}")
print(f"Computer chose: {choices[random_num]}")

if random_num == chosen_num:
    print("It's a draw!")
elif (chosen_num == 1 and random_num == 3) or (chosen_num == 2 and random_num == 1) or (chosen_num == 3 and random_num == 2):
    print("You win!")
else:
    print("Computer Wins") #Since any other way of things going - means a loss for me, i dont even need to define anything.