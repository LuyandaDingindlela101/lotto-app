import json
from tkinter import *
from useful_functions import *

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")

y_axis = 250
user_sets = []


#   FUNCTION GETS AND RETURNS RANDOM NUMBERS
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


#   GET THE VALUES FROM THE SPIN BOXES AND RETURN THEM AS A LIST
def get_values():
    global user_sets
    #   FIRST, CHECK IF ALL THE SPIN BOXES ARENT EMPTY
    if test_empty(number_one.get()) and test_empty(number_two.get()) and test_empty(number_three.get()) and test_empty(number_four.get()) and test_empty(number_five.get()) and test_empty(number_six.get()):
        #   GET THE VALUES OF THE SPIN BOXES AND ADD THEM TO THE lotto_set
        lotto_set = [
            number_one.get(),
            number_two.get(),
            number_three.get(),
            number_four.get(),
            number_five.get(),
            number_six.get()
        ]

    #   UPDATE THE user_sets LIST SO WE CAN SAVE IT TO THE DATABASE LATER
    user_sets.append(lotto_set)
    return lotto_set


#   GETS THE VALUES AND DISPLAYS THEM TO THE USER
def play_new_set():
    #   GET THE VALUES OF THE LOTTO SETS AND DISPLAY TO THE USER
    display_user_sets(get_values())


#   CLEAR THE VALUES OF THE SPIN BOXES
def clear_entries():
    clear_entry(number_one)
    clear_entry(number_two)
    clear_entry(number_three)
    clear_entry(number_four)
    clear_entry(number_five)
    clear_entry(number_six)


#   EXIT THE PROGRAM
def exit():
    exit_program(window)


#   FUNCTION WILL ADD TO database FILE AND IMPORT THE NEXT SCREEN
def play_lotto():
    #   GET ACCESS TO THE global user_sets
    global user_sets
    #   UPDATE THE VALUE OF THE user_sets
    user_sets = ", user sets: " + str(user_sets)
    #   WRITE TO THE database FILE
    write_to_file(str(user_sets))
    #   DESTROY THE CURRENT window AND IMPORT THE NEXT window
    window.destroy()
    import  lotto_results


#   CREATE A LABEL AND DISPLAY THE NEW LOTTO SET TO THE USER
def display_user_sets(set):
    global y_axis

    set_label = Label(window, text=set, fg="blue").place(x=10, y=y_axis)
    y_axis = y_axis + 50


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

window.mainloop()
