

## Assignment 4: Phonebook (dictionary)

user = {"name": "Hanad" , "phone no": "89237322" , "country": "somalia"}
print(user.get("name"))
print(user.get("location"))

for name in user:
    print(name)

for key, value in user.items():
    print(key, ":", value)