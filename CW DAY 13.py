item = input("Enter the name of the new item: ")
try:
    with open("items.txt", "a") as file:
        file.write(item + "\n")
    print("\nCurrent list of items:")
    with open("items.txt", "r") as file:
        for line in file:
            print("- " + line.strip())
except Exception as e:
    print("An error occurred:", e)