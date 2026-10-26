# This file stores contacts and saves them to a text file.
# A class is a blueprint for creating objects.
# An object is one real instance of the class.
# We use Path(__file__) so the saved file lives next to this script.

from pathlib import Path


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"


alice = Contact("Alice", "555-0101")
print(alice)

storage_file = Path(__file__).with_name("contact_book.txt")
with storage_file.open("a", encoding="utf-8") as file:
    file.write(f"{alice.name},{alice.phone}\n")

print(f"Saved contact to {storage_file.name}")
