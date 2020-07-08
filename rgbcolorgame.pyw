"""
Usage:
    1) The correct RGB is displayed above the buttons as text
    2) Click the color that you think corresponds to the correct RGB
    3) If the answer you choose is wrong, the box turns black
    3) If the answer is correct, all the boxes turn into the correct color
    - A window pop's up to ask you to play again or quit.
    4) You can set the difficulty to easy (3 boxes) or normal (6 boxes)

Python version:
    3x

App version:
    0.0.8


Author:
    King Phyte

Email:
    kofiasante1400@gmail.com
"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import randint, choice
from time import sleep


class RGBColorGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RGB Color Game")
        self.root.resizable(0, 0)
        self.root.configure(
            borderwidth=1, relief=tk.SUNKEN, background="black")
        self.default_frame = ttk.Frame(self.root, width=700, height=700)
        self.default_frame.pack()
        self.new_game()
        self.root.mainloop()

    def new_game(self, boxes=6):
        """
        Starts a new game
        """
        def is_correct(button_index, button):
            """
            Checks if the clicked button is the correct answer
            """
            sleep(0.2)  # To give a sense of animation

            if boxes == 6:
                buttons = [button_1, button_2, button_3,
                           button_4, button_5, button_6]

            elif boxes == 3:
                buttons = [button_1, button_2, button_3]

            # If answer is correct, turn all boxes to that color, else make it black
            if button_index == index_of_chosen_color:
                rgb_display.configure(text="Correct!")

                for but in buttons:
                    but.configure(style="B%d.TLabel" % index_of_chosen_color)

                retry = messagebox.askyesno(
                    title="RGB Color Game", message="You won! Play again?")

                if retry == True:
                    self.new_game(boxes=boxes)
                else:
                    self.root.destroy()
            else:
                button.configure(style="Default.TLabel")

        rgb_display = ttk.Label(
            self.default_frame, text="RGB()", font=("Arial", 20, "italic"))
        rgb_display.grid(row=1, columnspan=3, rowspan=2)

        difficulty_label = ttk.Frame(
            self.default_frame, relief=tk.SUNKEN, borderwidth=1, width=435)
        difficulty_label.grid(row=3, columnspan=4)

        easy_mode = ttk.Button(difficulty_label, text="Easy",
                               command=lambda: self.new_game(boxes=3))
        easy_mode.grid(row=1, column=0)

        normal_mode = ttk.Button(
            difficulty_label, text="Normal", command=lambda: self.new_game(boxes=6))
        normal_mode.grid(row=1, column=1)

        colors = []

        style = ttk.Style()

        # Generate random colors, assign them to styles and
        # randomly assign them to the buttons
        for i in range(boxes):
            color = self.rgb_generator()
            style.configure("B%d.TLabel" % i, background=color[-1])
            colors.append(color)

        # Select one color randomly, find its index and put its RGB in the label
        chosen_color = choice(colors)
        index_of_chosen_color = colors.index(chosen_color)

        style.configure("Default.TLabel", background="black")

        if boxes == 6:

            self.root.geometry("435x355")

            button_1 = ttk.Button(self.default_frame,
                                  command=lambda: is_correct(0, button_1))
            button_1.grid(row=4, column=0, ipadx=70, ipady=70)

            button_2 = ttk.Button(self.default_frame,
                                  command=lambda: is_correct(1, button_2))
            button_2.grid(row=4, column=1, ipadx=70, ipady=70)

            button_3 = ttk.Button(self.default_frame,
                                  command=lambda: is_correct(2, button_3))
            button_3.grid(row=4, column=2, ipadx=70, ipady=70)

            button_4 = ttk.Button(self.default_frame,
                                  command=lambda: is_correct(3, button_4))
            button_4.grid(row=5, column=0, ipadx=70, ipady=70)

            button_5 = ttk.Button(self.default_frame,
                                  command=lambda: is_correct(4, button_5))
            button_5.grid(row=5, column=1, ipadx=70, ipady=70)

            button_6 = ttk.Button(self.default_frame,
                                  command=lambda: is_correct(5, button_6))
            button_6.grid(row=5, column=2, ipadx=70, ipady=70)

            buttons = [button_1, button_2, button_3,
                       button_4, button_5, button_6]

            rgb_display.configure(text="RGB(%d, %d, %d)" %
                                  (chosen_color[0], chosen_color[1], chosen_color[2]))

        elif boxes == 3:

            self.root.geometry("435x200")

            button_1 = ttk.Button(self.default_frame,
                                  command=lambda: is_correct(0, button_1))
            button_1.grid(row=4, column=0, ipadx=70, ipady=70)

            button_2 = ttk.Button(self.default_frame,
                                  command=lambda: is_correct(1, button_2))
            button_2.grid(row=4, column=1, ipadx=70, ipady=70)

            button_3 = ttk.Button(self.default_frame,
                                  command=lambda: is_correct(2, button_3))
            button_3.grid(row=4, column=2, ipadx=70, ipady=70)

            buttons = [button_1, button_2, button_3]

            rgb_display.configure(text="RGB(%d, %d, %d)" %
                                  (chosen_color[0], chosen_color[1], chosen_color[2]))

        # Style a button with its saved index and remove both the button and
        # color from the list to prevent another button using the same color
        buttons[index_of_chosen_color].configure(
            style="B%d.TLabel" % index_of_chosen_color)
        buttons.remove(buttons[index_of_chosen_color])
        colors.pop(index_of_chosen_color)

        k = 0  # To index the list of colors and buttons (the wrong ones)

        for i in range(boxes):
            if i != index_of_chosen_color:
                buttons[k].configure(style="B%d.TLabel" % i)
                buttons.pop(k)

    def rgb_generator(self):
        """
        Generates and returns a tuple of RGB and a hexacimal value
        """
        def rgb_to_hex_converter(rbg):
            """Translates an rgb tuple of int to hexadecimal color"""
            return "#%02x%02x%02x" % rbg

        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        hexa = rgb_to_hex_converter((r, g, b))
        return (r, g, b, hexa)


def main():
    RGBColorGame()


if __name__ == "__main__":
    main()
