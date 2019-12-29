name, char = input("Enter comma seperated name and character :").split(",")

print(f"Length of your name is {len(name)}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}")
