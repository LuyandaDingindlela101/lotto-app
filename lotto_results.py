from tkinter import *
from useful_functions import *

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")

y_axis = 50
winnings = []


#   CREATE A LABEL AND DISPLAY THE NEW LOTTO SET TO THE USER
def display_user_sets():
    global y_axis

    database_contents = read_database_file()
    database_sets = database_contents["user sets"]

    for set in database_sets:
        Label(window, text=set, fg="blue").place(x=10, y=y_axis)
        y_axis = y_axis + 50

    Button(window, text="Claim Prize", command=claim_prize, fg="blue").place(x=10, y=(y_axis + 50))
    Button(window, text="Exit programme", command=exit_program, fg="blue").place(x=400, y=(y_axis + 50))


#   GENERATE AND DISPLAY THE WINNING NUMBERS AND UPDATE THE database FILE
def display_winning_sets():
    #   GENERATE THE WINNING lotto_numbers
    lotto_numbers = get_lotto_numbers()

    #   SAVE THE lotto_numbers TO THE database FILE
    #   FIRST GET THE database_contents
    database_contents = read_database_file()
    #   UPDATE THE database_sets AND ADD THE winning sets
    database_contents["winning set"] = lotto_numbers
    #   UPDATE THE database FILE
    print(database_contents)
    # write_to_file(database_contents)

    lotto_numbers_label = Label(window, text=lotto_numbers, fg="blue")
    lotto_numbers_label.place(x=250, y=50)


#   FUNCTION GETS AND RETURNS RANDOM LOTTO NUMBERS
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


#   FUNCTION WILL CHECK THE USERS SETS AGAINST THE WINNING SETS AND DETERMINE HOW MUCH THEY WON
def determine_winnings():
    #   GET THE CONTENTS OF THE database FILE
    database_contents = read_database_file()

    user_sets = database_contents["user sets"]
    winning_set = database_contents["winning set"]

#     NOW, WE LOOP THROUGH THE user_sets TO CHECK HOW MANY MATCHES THERE ARE
    for user_set in user_sets:
        print(user_set)
        for i in range(0, len(user_set)):
            user_set[i] = int(user_set[i])

        user_set = set(user_set)
        winning_set = set(winning_set)

        intersections = len(winning_set.intersection(user_set))

        determine_prize(intersections)


def determine_prize(intersections):
    global winnings

    prizes = {
        0: 0,
        1: 0,
        2: 20.00,
        3: 100.50,
        4: 2384.00,
        5: 8584.00,
        6: 1000000.00
    }

    your_prize = prizes[intersections]
    winnings.append(int(your_prize))


def claim_prize():
    total_winnings = sum(winnings)
    messagebox.showinfo("Wins", "Congrats, your prize is : R" + str(total_winnings))

    database_contents = read_database_file()
    database_contents["total winnings"] = total_winnings
    write_to_file(database_contents)

    if total_winnings > 0:
        convert = messagebox.askquestion("Convert Currency?", "Would you like to convert your winnings?")

        if convert == "yes":
            pass
#             IMPORT THE CURRENCY CONVERTER SCREEN
        else:
            window.destroy()
            import banking_input


def exit_program():
    pass


heading_label = Label(window, text="Your lucky numbers were: ", fg="blue")
heading_label.place(x=10, y=10)

user_numbers_label = Label(window, text="", fg="blue")
user_numbers_label.place(x=10, y=50)

lotto_label = Label(window, text="The winning numbers are: ", fg="blue")
lotto_label.place(x=250, y=10)

display_user_sets()
display_winning_sets()
determine_winnings()

window.mainloop()
