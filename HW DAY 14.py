import random
import math
names_input = input("Enter customer names (comma-separated): ")
names_list = [name.strip() for name in names_input.split(",")]
unique_names = list(set(names_list))
random.shuffle(unique_names)
total_participants = len(unique_names)
print("\nTotal unique participants:", total_participants)
sqrt_value = round(math.sqrt(total_participants))
print("Rounded square root of participants:", sqrt_value)
if total_participants >= 2:
    winners = random.sample(unique_names, 2)
    reversed_winners = [winner[::-1] for winner in winners]
    print("\n Lucky Draw Winners (Reversed Names):")
    print("Winner 1:", reversed_winners[0])
    print("Winner 2:", reversed_winners[1])
elif total_participants == 1:
    print("\nOnly one participant. Not enough for a lucky draw.")
else:
    print("\nNo participants entered.")