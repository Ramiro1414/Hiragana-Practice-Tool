import random
import tkinter as tk
from hiragana import Hiragana

FONT_SIZE = 18
FONT = 'Arial'

hiragana = Hiragana()

class GUI:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("500x500") # magic numbers, replace
        self.root.title("Hiragana Practice Tool")

        self.root.bind("<Return>", self.validate_answer)

        self.user_score = 0

        # List of tuples to keep a record of the mistakes the user commits (starts as an empty list).
        # Format:
        # (hiragana_character, user input, correct answer)
        self.user_errors = []

        self.practicing = False
        self.hiragana_characters_list = []
        self.hiragana_characters_dictionary = hiragana.get_hiragana_dictionary()
        self.hiragana_character_count = 0

        start_button = tk.Button(self.root, text="Start", font=(FONT, FONT_SIZE), command=self.start_practice)
        start_button.pack()

        self.hiragana_character_label = tk.Label(self.root, text="", font=(FONT, FONT_SIZE))
        self.hiragana_character_label.pack(padx=20, pady=20) # magic numbers, replace

        self.user_input_entry = tk.Entry(self.root)
        self.user_input_entry.pack()

        self.root.mainloop()
    
    def show_hiragana_character(self, hiragana_character):
        self.hiragana_character_label.config(text=hiragana_character)

    def validate_answer(self, _):
        user_answer = self.user_input_entry.get().strip().lower()
        current_hiragana_character = self.hiragana_character_label["text"]
        correct_answer = self.hiragana_characters_dictionary.get(current_hiragana_character)

        next_character = self.next_hiragana_character() # modify because last character is not counting, cause if sets "practicing" to false, and the line 53 don't evaluate to true

        if self.practicing:
            if (user_answer == correct_answer):
                self.user_score += 1
                self.show_hiragana_character(next_character)
                self.user_input_entry.delete(0, 'end')
            else:
                self.user_errors.append((current_hiragana_character, user_answer, correct_answer))
                self.show_hiragana_character(next_character)
                self.user_input_entry.delete(0, 'end')
        

    
    def next_hiragana_character(self) -> str:
        """
        Chooses the next hiragana character randomly
        """
        if self.hiragana_character_count != 46:
            self.hiragana_character_count += 1
            return self.hiragana_characters_list.pop(random.randrange(len(self.hiragana_characters_list)))
        else:
            self.practicing = False
            self.show_practice_result()

    def fill_hiragana_characters_list(self):
        for hiragana_character in self.hiragana_characters_dictionary:
            self.hiragana_characters_list.append(hiragana_character)
    
    def start_practice(self):
        self.practicing = True
        self.fill_hiragana_characters_list()
        character = self.next_hiragana_character()
        self.show_hiragana_character(character)

    
    def show_practice_result(self):
        # gui.show_practice_report # show info about how many characters were guessed and errors.
        print(f"User guessed {self.user_score}/46 characters.")

        # If user commited any mistake, it will be displayed along with the correct answer
        if (len(self.user_errors) != 0):
            print("----- Mistakes -----")
            for error in self.user_errors:
                print(f"Character: {error[0]}, User input: {error[1]}, Correct answer: {error[2]}")