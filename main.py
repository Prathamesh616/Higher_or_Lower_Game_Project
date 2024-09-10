from operator import index

from art import logo
from art import vs
from game_data import data
import random
data_replica = data
game_over = True
user_score = 0

while game_over:
    if len(data_replica) == 1:
        break
    print(logo)
    if user_score == 0:
        random1 = random.choice(data_replica)
    name1 = random1["name"]
    fc1 = random1["follower_count"]
    description1 = random1["description"]
    country1 = random1["country"]
    print(f"Compare A: {name1}, a {description1}, from {country1}.")
    print(vs)
    data_replica.remove(random1)
    random2 = random.choice(data_replica)
    name2 = random2["name"]
    fc2 = random2["follower_count"]
    description2 = random2["description"]
    country2 = random2["country"]
    print(f"Against B: {name2}, a {description2}, from {country2}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == "a" and fc1 > fc2:
        user_score += 1
        print("----------------------------------------------------------------------------------------")
        print(f"You're right! Current Score: {user_score}.")
        print("----------------------------------------------------------------------------------------")
    elif choice == "b" and fc1 < fc2:
        user_score += 1
        print("----------------------------------------------------------------------------------------")
        print(f"You're right! Current Score: {user_score}.")
        print("----------------------------------------------------------------------------------------")
    else:
        print(f"Oh no. You lost! Final Score: {user_score}")
        game_over = False
    random1 = random2
if len(data_replica) == 1:
    print("It seems you have reached the end of our data.")




