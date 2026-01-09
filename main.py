import random

hiragana_characters_dictionary = {
    "ん" : "n", "わ" : "wa", "ら" : "ra", "や" : "ya", "ま" : "ma", "は" : "ha", "な" : "na", "た" : "ta", "さ" : "sa", "か" : "ka", "あ" : "a",
    "り" : "ri", "み" : "mi", "ひ" : "hi", "に" : "ni", "ち" : "chi", "し" : "shi", "き" : "ki", "い" : "i",
    "る" : "ru", "ゆ" : "yu", "む" : "mu", "ふ" : "fu", "ぬ" : "nu", "つ" : "tsu", "す" : "su", "く" : "ku", "う" : "u",
    "れ" : "re", "め" : "me", "へ" : "he", "ね" : "ne", "て" : "te", "せ" : "se", "け" : "ke", "え" : "e",
    "を" : "wo", "ろ" : "ro", "よ" : "yo", "も" : "mo", "ほ" : "ho", "の" : "no", "と" : "to", "そ" : "so", "こ" : "ko", "お" : "o"										
}

# Original list of hiragana characters
hiragana_characters_list = []

for hiragana_character in hiragana_characters_dictionary:
    hiragana_characters_list.append(hiragana_character)

# List used for practicing (is a copy, since I don't want a reference of the original list, but a copy of it)
current_hiragana_character_list = hiragana_characters_list.copy()

# List of tuples to keep a record of the mistakes the user commits (starts as an empty list).
# Format:
# (hiragana_character, user input, correct answer)
user_errors = []

# Number of correct answers
score = 0

while (len(current_hiragana_character_list) != 0):

    current_hiragana_character = current_hiragana_character_list.pop(random.randrange(len(current_hiragana_character_list)))

    answer = input(f"{current_hiragana_character}: ").strip().lower()

    if (answer == hiragana_characters_dictionary.get(current_hiragana_character)):
        score += 1
    else:
        user_errors.append((current_hiragana_character, answer, hiragana_characters_dictionary.get(current_hiragana_character)))

print(f"User guessed {score}/46 characters.")

# If user commited any mistake, it will be displayed along with the correct answer
if (len(user_errors) != 0):
    print("----- Mistakes -----")
    for error in user_errors:
        print(f"Character: {error[0]}, User input: {error[1]}, Correct answer: {error[2]}")
