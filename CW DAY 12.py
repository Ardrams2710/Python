
import re
try:
    title=input("Enter the book title: ")
    if not re.fullmatch(r"[A-Za-z ]+", title):
        raise ValueError("Invalid book title! Use only alphabets and spaces.")
    year = input("Enter the publication year: ")
    if not re.fullmatch(r"(19|20)\d{2}", year):
        raise ValueError("Invalid publication year! Must be a 4-digit year starting with 19 or 20.")
    print("\nBook details accepted successfully.")
    print("Title:", title)
    print("Publication Year:", year)
except ValueError as e:
    print("\nError:", e)
finally:
    print("\nProgram execution completed. Thank you for using the Mini Library System.")


