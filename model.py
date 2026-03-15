import random

TOTAL_HIRAGANA_CHARACTERS = 46

class Model:
    
    def __init__(self):

        self.characters_dictionary = {
        "ん" : "n", "わ" : "wa", "ら" : "ra", "や" : "ya", "ま" : "ma", "は" : "ha", "な" : "na", "た" : "ta", "さ" : "sa", "か" : "ka", "あ" : "a",
        "り" : "ri", "み" : "mi", "ひ" : "hi", "に" : "ni", "ち" : "chi", "し" : "shi", "き" : "ki", "い" : "i",
        "る" : "ru", "ゆ" : "yu", "む" : "mu", "ふ" : "fu", "ぬ" : "nu", "つ" : "tsu", "す" : "su", "く" : "ku", "う" : "u",
        "れ" : "re", "め" : "me", "へ" : "he", "ね" : "ne", "て" : "te", "せ" : "se", "け" : "ke", "え" : "e",
        "を" : "wo", "ろ" : "ro", "よ" : "yo", "も" : "mo", "ほ" : "ho", "の" : "no", "と" : "to", "そ" : "so", "こ" : "ko", "お" : "o"										
        }
        
        self.correct_answers = 0
        self.characters_list = self.create_hiragana_characters_list()
        self.number_of_characters = len(self.characters_list)
        self.current_character = ""

    def answer_is_correct(self, user_answer):
        if (user_answer == self.characters_dictionary[self.current_character]):
            self.correct_answers += 1
            return

        return
    
    def get_number_of_correct_answers(self):
        return self.correct_answers
    
    def get_number_of_characters(self):
        return self.number_of_characters
    
    def decrease_number_of_characters(self):
        self.number_of_characters -= 1
    
    def create_hiragana_characters_list(self):
        list = []
        for character in self.characters_dictionary.keys():
            list.append(character)

        return list
    
    def get_character_from_list(self):
        new_character = random.choice(self.characters_list)
        self.characters_list.remove(new_character)
        self.current_character = new_character
        return new_character
    