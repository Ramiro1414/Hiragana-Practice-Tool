import tkinter as tk
from controller import Controller

def main():
   root = tk.Tk()
   root.title("Hiragana practice tool")
   root.geometry("480x360")

   app = Controller(root)
   root.mainloop()

if __name__ == "__main__":
   main()