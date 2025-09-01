txt = input("Enter Message ")
key = input("Enter Key ")

def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if ord(char) == 32:
            result += " "
            continue
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

print("Encrypted Text : " + encrypt(txt, int(key)))