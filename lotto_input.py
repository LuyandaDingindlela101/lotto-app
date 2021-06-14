from tkinter import *

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")


def play_again():
    # SHOW THE PREV SETS AND ADD NEW SETS
    pass


def clear_entries():
    pass


def exit_program():
    pass


def play_lotto():
    pass


instructions_label = Label(window, text="Choose your lucky numbers", fg="blue")
instructions_label.place(x=10, y=10)

number_one = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_one.place(x=10, y=50)

number_two = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_two.place(x=80, y=50)

number_three = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_three.place(x=180, y=50)

number_four = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_four.place(x=280, y=50)

number_five = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_five.place(x=380, y=50)

number_six = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_six.place(x=480, y=50)

add_btn = Button(window, text="Add new entry", command=play_again, fg="blue").place(x=10, y=100)
clear_btn = Button(window, text="Clear entries", command=clear_entries, fg="blue").place(x=200, y=100)
exit_btn = Button(window, text="Exit programme", command=exit_program, fg="blue").place(x=400, y=100)

play_btn = Button(window, text="Play Lotto", command=play_lotto, fg="blue", width=62).place(x=10, y=150)

heading_label = Label(window, text="Your lotto sets: ", fg="blue")
heading_label.place(x=10, y=200)

window.mainloop()
