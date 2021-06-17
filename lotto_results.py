from tkinter import *
from useful_functions import *

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")

y_axis = 50


#   CREATE A LABEL AND DISPLAY THE NEW LOTTO SET TO THE USER
def display_user_sets():
    global y_axis

    database_contents = read_database_file()
    #   GET THE LAST ITEM IN THE database_contents
    last_item = database_contents[len(database_contents) - 1]
    print(last_item)
    # returns first occurrence of Substring
    result = last_item.find('user sets: ')
    print("Substring 'user sets: ' found at index:", result)
    print(list(last_item[158: len(last_item)]))
    print(last_item[158: len(last_item)].replace("'", ""))
    # set_label = Label(window, text="", fg="blue").place(x=10, y=y_axis)
    # y_axis = y_axis + 50


def play_again():
    pass


def claim_prize():
    pass


def exit_program():
    pass


heading_label = Label(window, text="Your lucky numbers were: ", fg="blue")
heading_label.place(x=10, y=10)

user_numbers_label = Label(window, text="", fg="blue")
user_numbers_label.place(x=10, y=50)

lotto_label = Label(window, text="The winning numbers are: ", fg="blue")
lotto_label.place(x=10, y=100)

lotto_numbers_label = Label(window, text="", fg="blue")
lotto_numbers_label.place(x=10, y=150)

add_btn = Button(window, text="Add new entry", command=play_again, fg="blue").place(x=10, y=200)
claim_btn = Button(window, text="Claim Prize", command=claim_prize, fg="blue").place(x=200, y=200)
exit_btn = Button(window, text="Exit programme", command=exit_program, fg="blue").place(x=400, y=200)


display_user_sets()

window.mainloop()
