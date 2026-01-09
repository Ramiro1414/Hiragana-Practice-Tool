import random

hiragana_characters = [
    ("ん", "n"),
    ("わ", "wa"),
    ("ら", "ra"),
    ("や", "ya"),
    ("ま", "ma"),
    ("は", "ha"),
    ("な", "na"),
    ("た", "ta"),
    ("さ", "sa"),
    ("か", "ka"),
    ("あ", "a"),
    ("り", "ri"),
    ("み", "mi"),
    ("ひ", "hi"),
    ("に", "ni"),
    ("ち", "chi"),
    ("し", "shi"),
    ("き", "ki"),
    ("い", "i"),
    ("る", "ru"),
    ("ゆ", "yu"),
    ("む", "mu"),
    ("ふ", "fu"),
    ("ぬ", "nu"),
    ("つ", "tsu"),
    ("す", "su"),
    ("く", "ku"),
    ("う", "u"),
    ("れ", "re"),
    ("め", "me"),
    ("へ", "he"),
    ("ね", "ne"),
    ("て", "te"),
    ("せ", "se"),
    ("け", "ke"),
    ("え", "e"),
    ("を", "wo"),
    ("ろ", "ro"),
    ("よ", "yo"),
    ("も", "mo"),
    ("ほ", "ho"),
    ("の", "no"),
    ("と", "to"),
    ("そ", "so"),
    ("こ", "ko"),
    ("お", "o")										
]

score = 0

while (len(hiragana_characters) != 0):

    current_hiragana_character = hiragana_characters.pop(random.randrange(len(hiragana_characters)))

    answer = input(f"{current_hiragana_character[0]}: ")

    if (answer == current_hiragana_character[1]):
        score += 1

print(f"User guessed {score}/46 characters.")
