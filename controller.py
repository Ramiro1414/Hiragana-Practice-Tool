from model import Model
from view import View

class Controller:
    def __init__(self, root):
      self.root = root
      self.model = Model()
      self.view = View(root, self)
      self.view.update_hiragana_character_label(self.model.get_character_from_list()) # shows the first hiragana character

    def validate_answer(self, user_input):
        """
        Function that validates user's input, chooses another character and shows it in the label
        """
        self.model.decrease_number_of_characters()

        if (self.model.get_number_of_characters() != 0):
            self.model.answer_is_correct(user_input)
            self.view.update_hiragana_character_label(self.model.get_character_from_list())
        else:
            self.model.answer_is_correct(user_input)
            self.view.show_end_of_practice(self.model.get_number_of_correct_answers())

        return