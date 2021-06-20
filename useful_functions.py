from tkinter import messagebox, END


#   FUNCTION WILL DETERMINE IF PARAMETER CONTAINS INTEGERS
def contains_numbers(test_entry):
    #   IMPORT THE REGULAR EXPRESSION MODULE
    import re

    try:
        #   search FOR A DIGIT(INTEGER) IN THE test_entry
        if re.search('\d', test_entry):
            #   IF A DID=GIT IS FOUND, RAISE TypeError
            raise TypeError()
        #   IF NO DIGIT IS FOUND, RETURN False
        else:
            return False

    except TypeError:
        messagebox.showerror("Type Error", "Entry cannot contain integers")
        return True


def not_empty(test_entry):
    try:
        if test_entry == "":
            raise ValueError()
        else:
            return True
    except ValueError:
        messagebox.showerror("Value Error", "Cannot convert empty string")
        return False


def is_email(test_entry):
    email = test_entry.strip().lower()
    if "@" not in email:
        print("Invalid email")
        return False
    elif not email[-4:] in ".com.org.edu.gov.net":
        print("Invalid email")
        return False
    else:
        return True


def id_valid(id_number):
    import rsaidnumber
    try:
        id_number = rsaidnumber.parse(id_number)
        return id_number.valid
    except ValueError:
        return False


def generate_lotto_number():
    import random
    return random.randint(1, 49)


#   FUNCTION CLEARS ALL THE ENTRIES CONTENTS
def clear_entry(test_entry):
    test_entry.delete(0, END)


#   THIS FUNCTION WILL CLOSE THE PROGRAM ON CLICK OF THE exit_btn
def exit_program(window):
    message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit', icon='warning')
    if message_box == 'yes':
        play_sound("page_transition")
        window.destroy()
    else:
        #   ELSE, JUST GO BACK TO THE APPLICATION SCREEN
        pass


def play_sound(sound):
    from playsound import playsound
    playsound("./audio/" + sound + ".mp3")
