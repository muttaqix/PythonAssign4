phonebook = {
    'John': ('209 Trafalgar Road', '905-666-7777'),
    'Rosie': ('1439 Trafalgar Road', '487-423-7721'),
}

with open("SpeedDial1.txt", "w") as file:
    for contact in phonebook.values():
        phone_number = contact[1]
        file.write(phone_number + "\n")

