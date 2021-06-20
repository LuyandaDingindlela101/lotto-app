#   Luyanda Dingindlela | Class 1
from tkinter import *
from database import *
from useful_functions import *

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")

y_axis = 250
user_sets = []


#   GET THE VALUES FROM THE SPIN BOXES AND RETURN THEM AS A LIST
def get_values():
    global user_sets

    try:
        number_one = int(number_one_spinbox.get())
        number_two = int(number_two_spinbox.get())
        number_three = int(number_three_spinbox.get())
        number_four = int(number_four_spinbox.get())
        number_five = int(number_five_spinbox.get())
        number_six = int(number_six_spinbox.get())

        #   FIRST, CHECK IF ALL THE SPIN BOXES ARENT EMPTY
        if not_empty(number_one) and not_empty(number_two) and not_empty(number_three) and not_empty(number_four) and not_empty(number_five) and not_empty(number_six):

            #   GET THE VALUES OF THE SPIN BOXES AND ADD THEM TO THE lotto_set
            lotto_set = [
                number_one,
                number_two,
                number_three,
                number_four,
                number_five,
                number_six
            ]

            #   WE GOTTA CHECK IF THE GIVEN NUMBERS ARE BETWEEN 1 - 49
            for number in lotto_set:
                #       IF THE number IS BETWEEN 1 - 49
                if not 1 <= number <= 49:
                    raise ValueError

            play_sound("validation_success")
            #   UPDATE THE user_sets LIST SO WE CAN SAVE IT TO THE DATABASE LATER
            user_sets.append(lotto_set)
            return lotto_set

    except ValueError:
        messagebox.showerror("Input Error", "One or more of your inputs are not between 1 - 49")


#   GETS THE VALUES AND DISPLAYS THEM TO THE USER
def play_new_set():
    #   GET THE VALUES OF THE LOTTO SETS AND DISPLAY TO THE USER
    display_user_sets(get_values())
    #   CLEAR THE LAST PLAYED VALUES
    clear_entries()


#   CLEAR THE VALUES OF THE SPIN BOXES
def clear_entries():
    clear_entry(number_one_spinbox)
    clear_entry(number_two_spinbox)
    clear_entry(number_three_spinbox)
    clear_entry(number_four_spinbox)
    clear_entry(number_five_spinbox)
    clear_entry(number_six_spinbox)


#   EXIT THE PROGRAM
def exit():
    exit_program(window)


#   FUNCTION WILL ADD TO database FILE AND IMPORT THE NEXT SCREEN
def play_lotto():
    #   GET ACCESS TO THE global user_sets
    global user_sets
    #   SORT THS user_sets IN ASCENDING ORDER
    for user_set in user_sets:
        user_set.sort()

    #   GET ALL THE DATA FROM THE database FILE
    database_dict = read_database_file()
    #   UPDATE THE database_dict AND ADD THE user_sets
    database_dict["user sets"] = user_sets
    #   UPDATE THE database FILE
    write_to_file(database_dict)
    #   DESTROY THE CURRENT window AND IMPORT THE NEXT window
    play_sound("page_transition")
    window.destroy()
    import lotto_results


#   CREATE A LABEL AND DISPLAY THE NEW LOTTO SET TO THE USER
def display_user_sets(lotto_set):
    global y_axis

    set_label = Label(window, text=lotto_set, fg="blue").place(x=10, y=y_axis)
    y_axis = y_axis + 50


instructions_label = Label(window, text="Choose your lucky numbers", fg="blue")
instructions_label.place(x=10, y=10)

number_one_spinbox = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_one_spinbox.place(x=10, y=50)

number_two_spinbox = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_two_spinbox.place(x=80, y=50)

number_three_spinbox = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_three_spinbox.place(x=180, y=50)

number_four_spinbox = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_four_spinbox.place(x=280, y=50)

number_five_spinbox = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_five_spinbox.place(x=380, y=50)

number_six_spinbox = Spinbox(window, from_=0, to=49, width=5, fg="blue")
number_six_spinbox.place(x=480, y=50)

add_btn = Button(window, text="Add new entry", command=play_new_set, fg="blue").place(x=10, y=100)
clear_btn = Button(window, text="Clear entries", command=clear_entries, fg="blue").place(x=200, y=100)
exit_btn = Button(window, text="Exit programme", command=exit, fg="blue").place(x=400, y=100)

play_btn = Button(window, text="Play Lotto", command=play_lotto, fg="blue", width=62).place(x=10, y=150)

heading_label = Label(window, text="Your lotto sets: ", fg="blue")
heading_label.place(x=10, y=200)

window.mainloop()
