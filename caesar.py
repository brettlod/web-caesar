import webapp2


def alphabet_position(letter):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    character = letter.lower()
    index = alphabet.index(character)
    return index

def rotate_character(char, rot):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ordinal_value = int(ord(char))
    if ordinal_value < 65 or ordinal_value > 122:
        new_character = char
        return new_character
    character_index = int(alphabet_position(char))
    new_index=character_index + int(rot)
    if new_index > 25:
        new_index = new_index % 26
    new_character = alphabet[new_index]
    if ordinal_value > 64 and ordinal_value < 91:
            new_character = new_character.upper()
    return new_character


def encrypt(tex, rot):
    encrypted = ''
    rot=rot
    for char in tex:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            newChar = rotate_character(char, rot)
            encrypted = encrypted + newChar

    return encrypted
