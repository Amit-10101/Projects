from logo_art import logo
from lists import alphabet, cap_alpha, special_char

# Logo
print(logo)


# Main Program Function
def caesar_cipher():
    # Inputs
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    def caesar(caesar_direction, plain_text, shift_amount):
        cipher_text = ""

        if (caesar_direction == "encode") or (caesar_direction == "decode"):
            for letter in plain_text:
                # Special Characters
                if (letter in special_char):
                    new_letter = letter
                else:
                    # Position
                    if (letter in cap_alpha):
                        position = cap_alpha.index(letter)
                    else:
                        position = alphabet.index(letter)

                    # Encoding Postions
                    if (caesar_direction == "encode"):
                        new_position = position + shift_amount
                        if (new_position > 25):
                            while (new_position > 25):
                                new_position -= 26
                    # Decoding Postions
                    elif (caesar_direction == "decode"):
                        new_position = position - shift_amount
                        if (new_position < 0):
                            while (new_position < 0):
                                new_position += 26

                    # Encrypted or Decrypted Letters
                    if (letter in cap_alpha):
                        new_letter = cap_alpha[new_position]
                    else:
                        new_letter = alphabet[new_position]
                cipher_text += new_letter
            # Encrypted or Decrypted Text
            print(f"The {caesar_direction}d text is '{cipher_text}'")

        else:
            print("Invalid Function ❌")

    caesar(direction, text, shift)


run_of_program = True
while (run_of_program):
    caesar_cipher()
    # Continuation
    continue_of_program = input(
        "\nDo you want to continue? 'Y' or 'N' ").lower()
    print()
    if (continue_of_program == "n"):
        run_of_program = False
        print("Goodbye!!!")
    elif (continue_of_program != "y"):
        print("Invalid Input ❌\n")