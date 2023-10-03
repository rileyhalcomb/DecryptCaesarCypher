
caesar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u','v', 'w', 'x', 'y', 'z']

def decryt(text):
    cipher = ""
    for letter in text:
        if letter == " ":
            cipher += " "
            continue

        letter = letter.lower()
        index = caesar.index(letter) - 4
        cipher += caesar[index]
    return cipher

def encrypt(text):
    cipher = ""
    for letter in text:
        if letter == " ":
            cipher += " "
            continue

        letter = letter.lower()
        index = caesar.index(letter) + 4

        if index < 26:
            cipher += caesar[index]
        else:
            index = index - 26
            cipher += caesar[index]
    return cipher

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    str = input("Please enter a string to encrypt: ")
    print(encrypt(str))
    decryt(encrypt(str))
    print(decryt(encrypt(str)))