try:
    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()
    if name == "" or feedback == "":
        raise ValueError("Name and feedback cannot be empty.")
    print("\nThank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)
except ValueError as e:
    print("\nError:", e)
finally:
    print("\nThank you for visiting our restaurant.")