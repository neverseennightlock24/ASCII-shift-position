# Instructions for the user
print("This program will shift each character in your sentence either upwards or downwards in the ASCII alphabet.")
print("The shift will be based on the number you provide.")
print("Letters, numbers, and symbols will all be shifted.")
print("Note: This shift will wrap around within the alphabet or character set if necessary.")

# Ask the user if they want to view the entire ASCII alphabet
while True:
    view_ascii = input("Do you want to view the entire ASCII alphabet? (yes/no): ").strip().lower()
    if view_ascii in ["yes", "no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")

# If the user wants to view the ASCII alphabet, display it
if view_ascii == "yes":
    print("\nASCII Alphabet:")
    for i in range(32, 128):  # Printable ASCII characters range from 32 to 127
        print(f"{i}: {chr(i)}", end="  ")
        if (i - 31) % 10 == 0:  # Print 10 characters per line for readability
            print()
    print("\n")

# Ask the user if they want to shift up or down
while True:
    direction = input("Do you want to shift the characters up or down? (up/down): ").strip().lower()
    if direction in ["up", "down"]:
        break
    else:
        print("Please enter 'up' or 'down'.")

# Input from the user
theirSen = input("Type a sentence: ")
theirShift = int(input(f"Type the amount you want to shift your sentence {direction}: "))

# Shifting the sentence
for char in theirSen:
    if char.isprintable() and not char.isspace():  # Shift only printable, non-space characters
        if direction == "up":
            shifted = (ord(char) + theirShift) % 128  # Shift up within the ASCII range (0-127)
        else:  # direction == "down"
            shifted = (ord(char) - theirShift) % 128  # Shift down within the ASCII range (0-127)
        print(chr(shifted), end="")
    else:
        print(char, end="")  # Print spaces and non-printable characters as is

print("\nYour sentence has been shifted according to the ASCII alphabet.")
