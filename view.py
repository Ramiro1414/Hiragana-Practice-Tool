import tkinter as tk

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.hiragana_character_label = tk.Label(root, text="")
        self.hiragana_character_label.pack()

        self.user_input = tk.Entry(root)
        self.user_input.pack()

        self.next_character_button = tk.Button(root, text="Next", command=self.validate_answer)
        self.next_character_button.pack()
    
    def validate_answer(self):
        self.controller.validate_answer(self.user_input.get())
        self.user_input.delete(0, tk.END)

    def update_hiragana_character_label(self, character):
        self.hiragana_character_label.config(text=character)
    
    def show_end_of_practice(self, number_of_correct_answers):
        print(f"End of practice. You've guessed {number_of_correct_answers}/46")