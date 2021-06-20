from tkinter import *
from database import *
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
    Button(window, text="Exit programme", command=exit, fg="blue").place(x=400, y=(y_axis + 50))


#   GENERATE AND DISPLAY THE WINNING NUMBERS AND UPDATE THE database FILE
def display_winning_sets():
    #   GENERATE THE WINNING lotto_numbers
    lotto_numbers = get_lotto_numbers()
    lotto_numbers.sort()
    #   SAVE THE lotto_numbers TO THE database FILE
    #   FIRST GET THE database_contents
    database_contents = read_database_file()
    #   UPDATE THE database_sets AND ADD THE winning sets
    database_contents["winning set"] = lotto_numbers
    #   UPDATE THE database FILE
    write_to_file(database_contents)

    #   ADD THE lotto_numbers_label TO THE window
    lotto_numbers_label = Label(window, text=lotto_numbers, fg="blue")
    lotto_numbers_label.place(x=250, y=50)

    #   CALL THE determine_winnings() FUNCTION TO INFORM THE USER HOW MUCH THEY WON
    determine_winnings()


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
    match_list = []
    #   GET THE CONTENTS OF THE database FILE
    database_contents = read_database_file()

    #   GET BOTH LOTTO SETS
    user_sets = database_contents["user sets"]
    winning_set = database_contents["winning set"]

    #     NOW, WE LOOP THROUGH THE user_sets TO CHECK HOW MANY MATCHES THERE ARE
    for user_set in user_sets:
        #   CONVERT EACH DIGIT IN THE user_set TO AN INTEGER
        for i in range(0, len(user_set)):
            user_set[i] = int(user_set[i])

        #   CONVERT THE user_set LIST TO A PYTHON SET
        user_set = set(user_set)
        winning_set = set(winning_set)
        #   GET THE AMOUNT OF INTERSECTING DIGITS
        matching_numbers = len(winning_set.intersection(user_set))

        #   CHECK IF matching_numbers IS MORE THAN 0
        if matching_numbers > 0:
            #   GET THE MATCHING NUMBERS AND ADD THEM TO THE match_list
            for item in list(winning_set.intersection(user_set)):
                match_list.append(item)

    #   SAVE THE MATCHING NUMBERS
    database_contents["matching numbers"] = match_list
    #   UPDATE THE database FILE
    write_to_file(database_contents)
    #   CALL THE determine_prize FUNCTION
    determine_prize(len(match_list))


# FUNCTION WILL DETERMINE THE USERS PRIZE BASED ON THE AMOUNT OF INTERSECTIONS PER SET
def determine_prize(intersections):
    # ACCESS THE GLOBAL winnigs VARIABLE
    global winnings

    #   CREATE A DICTIONARY TO STORE THE prizes AND THE AMOUNT OF INTERSECTIONS NEEDED
    prizes = {
        0: 0,
        1: 0,
        2: 20.00,
        3: 100.50,
        4: 2384.00,
        5: 8584.00,
        6: 1000000.00
    }

    prize = prizes[intersections]
    #   CONVERT AND ADD EACH PRIZE TO THE winnings LIST
    winnings.append(int(prize))


#   FUNCTION WILL SAVE THE TOTAL WINNINGS AND ALLOW USERS TO MOVE TO THE NEXT SCREEN OR RESTART
def claim_prize():
    #   ACCESS THE GLOBAL winnings VARIABLE
    global winnings

    #   total_winnings IS ALL THE winnings ADDED TOGETHER
    total_winnings = sum(winnings)
    #   SHOW THE USER THEIR total_winnings
    if total_winnings == 0:
        messagebox.showinfo("Status", "Unfortunately, you didn't win. Your prize is : R" + str(total_winnings))
    else:
        messagebox.showinfo("Status", "Congrats, your prize is : R" + str(total_winnings))
        play_sound("Clapping")

    #   GET THE CONTENTS OF THE database FILE
    database_contents = read_database_file()
    #   SAVE THE TOTAL WINNINGS
    database_contents["total winnings"] = total_winnings
    #   UPDATE THE database FILE
    write_to_file(database_contents)

    #   IF THE USER WON MORE THAN 0, THEN ASK IF THEY WANT TO CONVERT THEIR CURENCY?
    if total_winnings > 0:
        convert = messagebox.askquestion("Convert Currency?", "Would you like to convert your winnings?")
        #   IF YES, THEN IMPORT THE currency_converter SCREEN
        if convert == "yes":
            play_sound("page_transition")
            #   IMPORT THE CURRENCY CONVERTER SCREEN
            window.destroy()
            import currency_converter
        #   IF NOT, THEN DESTROY THIS window AND IMPORT THE banking_input SCREEN
        else:
            play_sound("page_transition")
            window.destroy()
            import banking_input
    #   IF THE total_winnings IS EQUAL TO OR LESS THAN 0, THEN ASK THE USER IF THE WANT TO RESTART THE GAME
    else:
        replay = messagebox.askquestion("Replay?", "Unfortunately, you didn't win. Would you like to play again?")
        if replay == "yes":
            #   RESET THE database FILE, SO THE USER CAN RESTART
            with open("./database/database.txt", "w+") as text_file:
                pass
            #   IMPORT THE user_auth SCREEN
            play_sound("page_transition")
            window.destroy()
            import user_auth
        else:
            play_sound("page_transition")
            window.destroy()


def exit():
    exit_program(window)


heading_label = Label(window, text="Your lucky numbers were: ", fg="blue")
heading_label.place(x=10, y=10)

user_numbers_label = Label(window, text="", fg="blue")
user_numbers_label.place(x=10, y=50)

lotto_label = Label(window, text="The winning numbers are: ", fg="blue")
lotto_label.place(x=250, y=10)

display_user_sets()
display_winning_sets()

window.mainloop()
