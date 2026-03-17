# Four roommates take turns doing four different chores.
# Each day everyone does a different chore, and tomorrow they move to the next
# one in a fixed order.  We'll ask for today's chore for each person and then
# report what they will do tomorrow.

chores = ["cleaning", "washing", "cooking", "filling the water"]
print("Chore numbers: 1=cleaning  2=washing  3=cooking  4=filling water")

# collect today's chore for each of the four roommates
today_done = []
for person in range(1, 5):
    while True:
        try:
            choice = int(input(f"Roommate {person}, what did you do today? "))
            if 1 <= choice <= 4:
                today_done.append(choice - 1)  # store zero-based index
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("That's not a valid number, try again.")

print("\nSummary:")
for person, idx in enumerate(today_done, start=1):
    tomorrow_idx = (idx + 1) % len(chores)
    print(f"Roommate {person} did {chores[idx]} today and will do {chores[tomorrow_idx]} tomorrow.")

# you could easily extend this to keep a history or run for multiple days.
