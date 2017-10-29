import Tkinter
import random
from collections import namedtuple

Button = namedtuple("Button", "color alt_color x y")
BUTTONS_DATA = [Button("yellow", "yellow3", 30, 50),
                Button("blue", "medium blue", 125, 50),
                Button("red", "red3", 30, 145),
                Button("green", "dark green", 125, 145)]


class SimonGame:
    def __init__(self, buttons_data=BUTTONS_DATA):
        self.base = Tkinter.Tk()
        self.frame = Tkinter.Frame(self.base, bg="black", width="238", height="250")

        self.score = 0
        self.score_label = self.place_label(30, 15, "Score:")
        self.score_val = self.place_label(70, 15, self.score)

        self.best = 0
        self.best_label = self.place_label(155, 15, "Best:")
        self.best_val = self.place_label(188, 15, self.best)

        self.start = Tkinter.Button(self.base, bd="0", text="start", command=self.show_sequence)
        self.start.place(x=90, y=12)

        self.sequence = []
        self.user_sequence = []

        self.buttons_data = buttons_data
        self.buttons = [self.create_button(*button) for button in self.buttons_data]

        self.frame.pack()
        self.base.resizable(False, False)
        self.base.mainloop()

    def place_label(self, x, y, text, fg="white", bg="black"):
        label = Tkinter.Label(self.base, bg=bg, fg=fg, text=text)
        label.place(x=x, y=y)
        return label

    def click_factory(self, button, color, alt_color):
        def click():
            button.configure(activebackground=alt_color)
            button.after(500, lambda: button.configure(activebackground=color))
            self.user_sequence.append(color)
            self.check_sequence()
        return click

    def create_button(self, color, alt_color, x, y):
        button = Tkinter.Button(self.base, bd="0", highlightthickness="0",
                           width="7", height="5", activebackground=color,
                           bg=alt_color)
        button['command'] = self.click_factory(button, color, alt_color)
        button.place(x=x, y=y)
        return button

    def show_sequence(self):
        self.reset_gui()
        for _ in range(self.score + 1):
            i = random.randrange(len(self.buttons))
            button = self.buttons[i]
            button_data = self.buttons_data[i]
            button.configure(bg=button_data.color)
            button.after(750, lambda: button.configure(bg=button_data.alt_color))
            self.sequence.append(button_data.color)
        print self.sequence

    def check_sequence(self):
        if self.sequence == self.user_sequence:
            self.score += 1
            self.best = max(self.best, self.score)
            self.reset_gui()
        elif not self.sequence[:len(self.user_sequence)] == self.user_sequence:
            self.score = 0
            self.reset_gui()

    def reset_gui(self):
        self.sequence = []
        self.user_sequence = []
        for button, data in zip(self.buttons, self.buttons_data):
            button.configure(bg=data.alt_color, activebackground=data.color)
        self.best_val.configure(text=self.best)
        self.score_val.configure(text=self.score)

if __name__ == "__main__":
    game = SimonGame()
