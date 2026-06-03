import random

print("🎲 Advanced Dice Game - Player vs Computer")

player_score = 0
computer_score = 0

rounds = int(input("Enter number of rounds: "))

for i in range(1, rounds + 1):
    input(f"\nPress Enter to roll dice for Round {i}...")

    player = random.randint(1, 6)
    computer = random.randint(1, 6)

    print(f"Round {i}:")
    print("Player rolled:", player)
    print("Computer rolled:", computer)

    if player > computer:
        print("Player wins this round!")
        player_score += 1
    elif player < computer:
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("This round is a draw!")

print("\n🎯 Final Score:")
print("Player:", player_score)
print("Computer:", computer_score)

if player_score > computer_score:
    print("🏆 Player is the overall winner!")
elif player_score < computer_score:
    print("🏆 Computer is the overall winner!")
else:
    print("🤝 The game is a draw!")