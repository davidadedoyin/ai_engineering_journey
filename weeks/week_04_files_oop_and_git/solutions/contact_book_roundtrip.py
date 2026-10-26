# Reference solution.
# Look only after you have tried.

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

contacts = [
    Contact("Alice", "555-0101"),
    Contact("Bob", "555-0102"),
]

with open("contact_book.txt", "w", encoding="utf-8") as file:
    for contact in contacts:
        file.write(f"{contact.name},{contact.phone}\n")

with open("contact_book.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
