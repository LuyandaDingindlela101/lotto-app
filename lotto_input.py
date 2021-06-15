from tkinter import *
from useful_functions import *

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")


def get_lotto_numbers():
    #   CREATE AN EMPTY LIST TO HOLD THE Lotto_numbers
    lotto_numbers = []

    #   WHILE THE lotto_numbers HAS 6 OR LESS ITEMS
    while len(lotto_numbers) < 6:
        #   GENERATE A RANDOM NUMBER
        number = generate_lotto_number()

        #   CHECK IF THE number IS IN THE lotto _numbers ALREADY OR NOT
        if number not in lotto_numbers:
            #   IF IT ISN'T, APPEND THE number TO THE Lotto_numbers LIST
            lotto_numbers.append(number)

    #   RETURN THE lotto_numbers
    return lotto_numbers


def get_values():
    lotto_set = []

    lotto_set.append(number_one.get())
    lotto_set.append(number_two.get())
    lotto_set.append(number_three.get())
    lotto_set.append(number_four.get())
    lotto_set.append(number_five.get())
    lotto_set.append(number_six.get())

    display_user_sets(lotto_set)


def play_new_set():
    # SHOW THE PREV SETS AND ADD NEW SETS
    get_values()


def clear_entries():
    clear_entry(number_one)
    clear_entry(number_two)
    clear_entry(number_three)
    clear_entry(number_four)
    clear_entry(number_five)
    clear_entry(number_six)


def exit():
    exit_program(window)


def play_lotto():
    pass


def display_user_sets(set):
    set_label = Label(window, text=set, fg="blue")


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

add_btn = Button(window, text="Add new entry", command=play_new_set, fg="blue").place(x=10, y=100)
clear_btn = Button(window, text="Clear entries", command=clear_entries, fg="blue").place(x=200, y=100)
exit_btn = Button(window, text="Exit programme", command=exit, fg="blue").place(x=400, y=100)

play_btn = Button(window, text="Play Lotto", command=play_lotto, fg="blue", width=62).place(x=10, y=150)

heading_label = Label(window, text="Your lotto sets: ", fg="blue")
heading_label.place(x=10, y=200)

print(get_lotto_numbers())

window.mainloop()
