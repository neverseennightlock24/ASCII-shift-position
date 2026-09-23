# Explain what the program does
def print_instructions():
    print("This program will shift each character in your sentence either upwards or downwards in the ASCII alphabet.")
    print("The shift will be based on the number you provide.")
    print("Letters, numbers, and symbols will all be shifted, while spaces stay where they are.")
    print("Note: Shifting past either end of the ASCII alphabet (0-127) wraps around to the other end.")


# Keep asking until the user gives one of the two allowed answers
def ask_choice(prompt, options):
    while True:
        answer = input(prompt).strip().lower()
        if answer in options:
            return answer
        print(f"Please enter '{options[0]}' or '{options[1]}'.")


# Keep asking until the user gives a whole number
def ask_integer(prompt):
    while True:
        answer = input(prompt).strip()
        try:
            return int(answer)
        except ValueError:
            print("Please enter a whole number.")


# Display the printable ASCII characters (32-126), 10 per line
def print_ascii_table():
    print("\nASCII Alphabet:")
    for code in range(32, 127):
        print(f"{code}: {chr(code)}", end="  ")
        if (code - 31) % 10 == 0:
            print()
    print("\n")


# Shift every printable ASCII character except spaces; anything else is kept as is
def shift_sentence(sentence, shift_amount):
    shifted_chars = []
    for char in sentence:
        if char.isascii() and char.isprintable() and not char.isspace():
            shifted_code = (ord(char) + shift_amount) % 128
            shifted_chars.append(chr(shifted_code))
        else:
            shifted_chars.append(char)
    return "".join(shifted_chars)


print_instructions()

if ask_choice("Do you want to view the entire ASCII alphabet? (yes/no): ", ["yes", "no"]) == "yes":
    print_ascii_table()

direction = ask_choice("Do you want to shift the characters up or down? (up/down): ", ["up", "down"])

theirSentence = input("Type a sentence: ")
theirShift = ask_integer(f"Type the amount you want to shift your sentence {direction}: ")

# Shifting down is the same as shifting up by a negative amount
signed_shift = theirShift if direction == "up" else -theirShift

print(shift_sentence(theirSentence, signed_shift))
print("Your sentence has been shifted according to the ASCII alphabet.")
