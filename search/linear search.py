string = "sambhav"
tar = input("Enter the character: ")
found = False
for char in string:
    if char == tar:
        found = True
        break
if found:
    print("Found")
else:
    print("Not found")
