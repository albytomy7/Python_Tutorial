text = input("Enter text: ")
shift = int(input("Enter shift value: "))

result = ""

for char in text:
    if char.isalpha():
        result += chr((ord(char) - 65 + shift) % 26 + 65)
    else:
        result += char

print("Encrypted:", result)
