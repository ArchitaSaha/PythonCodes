import random
from tkinter import *

def rollDiceAnalog():
    n = random.randint(1, 6)
    print(n)
    display(n)

def display(n):
    if n == 1:
        print('+-------+')
        print('|       |')
        print('|   *   |')
        print('|       |')
        print('+-------+')
    elif n == 2:
        print('+-------+')
        print('| *     |')
        print('|       |')
        print('|     * |')
        print('+-------+')
    elif n == 3:
        print('+-------+')
        print('| *     |')
        print('|   *   |')
        print('|     * |')
        print('+-------+')
    elif n == 4:
        print('+-------+')
        print('| *   * |')
        print('|       |')
        print('| *   * |')
        print('+-------+')
    elif n == 5:
        print('+-------+')
        print('| *   * |')
        print('|   *   |')
        print('| *   * |')
        print('+-------+')
    elif n == 6:
        print('+-------+')
        print('| * * * |')
        print('|       |')
        print('| * * * |')
        print('+-------+')

def rollDiceDigital():
     # These values indicate dots on the dices.
     # For eg: \u2680 corresponds to 1 dot,
     # \u2681 corresponds to 2 dots etc.
    dice_dots = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice_dots)}')
    label.pack()

if __name__ == "__main__":
    window = Tk()
    window.configure(bg="black")
    window.geometry("600x550")
    window.title("Rolling The Dices Game")
    window.resizable(0, 0)
    roll_button = Button(window, text="Roll!", width=10, height=2, font=15, bg="white", bd=2, command=rollDiceDigital)
    roll_button.pack(padx=10, pady=15)
    label = Label(window, font=("times", 250), bg="black", fg="white")
    window.mainloop()

    # while True:
    #     choice = input('Press X to exit. Press any other key to roll the dice ... ')
    #     if choice == 'X' or choice == 'x':
    #         break
        
    #     rollDiceAnalog()