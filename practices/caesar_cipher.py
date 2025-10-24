# EG 2nd Caesar Cypher
 
# funciton encode message, shift
#     set result to empty string
#     FOR each character IN message
#         IF character is a letter
#             IF character is uppercase
#                 SET new_char TO ( (ASCII(character) - ASCII('A') + shift) MOD 26 ) + ASCII('A')
#             ELSE
#                 SET new_char TO ( (ASCII(character) - ASCII('a') + shift) MOD 26 ) + ASCII('a')
#             ADD new_char TO result
#         ELSE
#             ADD character TO result
#     RETURN result
# END FUNCTION
#
# FUNCTION decode(message, shift)
#     RETURN encode(message, -shift)
# END FUNCTION
#
# MAIN PROGRAM
#     DISPLAY "Choose operation (1 for encode, 2 for decode): "
#     INPUT operation
#     DISPLAY "Enter the message: "
#     INPUT message
#     DISPLAY "Enter the shift value: "
#     INPUT shift
#     IF operation == 1
#         set output to encode(message, shift)
#         DISPLAY "Encoded message: " + output
#     ELSE IF operation == 2
#         set output to decode(message, shift)
#         DISPLAY "Decoded message: " + output
#     ELSE
#         DISPLAY "Invalid choice. Please enter 1 or 2."

# FUNCTION DEFINITIONS

def encode(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        else:
            result += char
    return result


def decode(message, shift):
    return encode(message, -shift)


# MAIN PROGRAM

print("Choose operation (1 for encode, 2 for decode): ")
operation = int(input())

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

if operation == 1:
    output = encode(message, shift)
    print("Encoded message:", output)
elif operation == 2:
    output = decode(message, shift)
    print("Decoded message:", output)
else:
    print("Invalid choice. Please enter 1 or 2.")

