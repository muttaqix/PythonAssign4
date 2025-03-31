import json

phonebook = {
    'John': ('209 Trafalgar Road', '905-666-7777'),
    'Rosie': ('1439 Trafalgar Road', '487-423-7721'),
}
phonebookJson = {}

for name in phonebook:
    address, phone = phonebook[name]  
    phonebookJson[name] = [address, phone]  

with open("Speeddial2.json", "w") as file:
    json.dump(phonebookJson, file, indent=4)

with open("Speeddial2.json", "r") as file:
    phonebook = json.load(file)

for name, info in phonebook.items():
    address = info[0]  
    phone = info[1]    
    print(f"Name: {name}\nAddress: {address}\nPhone: {phone}\n")


