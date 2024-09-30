import sys

braille_letters_to_english = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",
}

braille_numbers_to_english = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

braille_special_symbols = {
    ".....O": "capital",
    ".O...O": "decimal",
    ".O.OOO": "number",
}

english_letters_to_braille = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    " ": "......"
}


def braille_to_english(braille_string):
    braille_list = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    english_list = []
    capitalize_next = False
    in_number_mode = False

    for braille in braille_list:
        if braille in braille_special_symbols:
            if braille_special_symbols[braille] == 'capital':
                capitalize_next = True
            elif braille_special_symbols[braille] == 'decimal':
                english_list.append(",")
                in_number_mode = True
            elif braille_special_symbols[braille] == 'number':
                in_number_mode = True
            continue


        if in_number_mode:
            if braille in braille_numbers_to_english:
                english_list.append(braille_numbers_to_english[braille])
            else:
                in_number_mode = False
                english_list.append(braille_letters_to_english[braille])
        else:
            if braille in braille_letters_to_english:
                letter = braille_letters_to_english[braille]
                if capitalize_next:
                    english_list.append(letter.upper())
                    capitalize_next = False
                else:
                    english_list.append(letter)
    return "".join(english_list)

def english_to_braille(english_string):
    braille_string = ""
    for i, char in enumerate(english_string):
        if char.isdigit():
            if (i == 0) or (not english_string[i - 1].isdigit()):
                braille_string += ".O.OOO"
                braille_string += english_letters_to_braille[char]
            else:
                braille_string += english_letters_to_braille[char]    
        
        elif char.isalpha():
            if char.isupper():
                braille_string += ".....O"
                braille_string += english_letters_to_braille[char.lower()]
            else:
                braille_string += english_letters_to_braille[char]
        elif char == " ":
            braille_string += english_letters_to_braille[char]
    return braille_string

def main():


    input_string = " ".join(sys.argv[1:]).strip()

    if all(char in "O. " for char in input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()
