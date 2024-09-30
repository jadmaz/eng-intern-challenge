
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

english_letters_to_braille = {v: k for k, v in braille_letters_to_english.items()}

english_numbers_to_braille = {v: k for k, v in braille_numbers_to_english.items()}

def braille_to_english(braille_string):
    braille_list = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    print(braille_list)
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
        else:
            if braille in braille_letters_to_english:
                letter = braille_letters_to_english[braille]
                if capitalize_next:
                    english_list.append(letter.upper())
                    capitalize_next = False
                else:
                    english_list.append(letter)
    return "".join(english_list)


