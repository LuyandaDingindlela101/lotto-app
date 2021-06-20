#   Luyanda Dingindlela | Class 1
from tkinter import messagebox, END


#   FUNCTION WILL DETERMINE IF PARAMETER CONTAINS INTEGERS OR NOT
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


#   FUNCTION WILL DETERMINE IF PARAMETER IS EMPTY OR NOT
def not_empty(test_entry):
    try:
        #   IF THE test_entry IS EMPTY, RAISE THE ValueError
        if test_entry == "":
            raise ValueError()
        #   IF THE test_entry IS NOT EMPTY, RETURN True
        else:
            return True
    except ValueError:
        messagebox.showerror("Value Error", "Cannot convert empty string")
        return False


#   FUNCTION WILL DETERMINE IF PARAMETER IS A VALID EMAIL OR NOT
def is_email(test_entry):
    #   .strip() FUNCTION REMOVES EMPTY SPACES BEFORE AND AFTER A STRING
    email = test_entry.strip().lower()
    #   CHECK IF THE email CONTAINS AN @ SYMBOL
    if "@" not in email:
        return False
    #   CHECK IF THE LAST CHARACTERS ARE ONE OF THE OPTIONS
    elif not email[-4:] in [".com", ".org", ".edu", ".gov", ".net"]:
        return False

    #   IF EVERYTHING CHECKS OUT, RETURN True
    return True


#   FUNCTION WILL DETERMINE IF PARAMETER IS A VALID ID OR NOT
def id_valid(id_number):
    #   IMPORT THE rsaidnumber MODULE
    import rsaidnumber

    try:
        id_number = rsaidnumber.parse(id_number)
        #   .valid RETURNS TRUE OR FALSE BASED ON id_number
        return id_number.valid
    except ValueError:
        return False


#   FUNCTION WILL GENERATE A RANDOM NUMBER
def generate_random_number():
    #   IMPORT THE random MODULE
    import random
    #   RETURN A RANDOM NUMBER BETWEEN 1 - 49
    return random.randint(1, 49)


#   FUNCTION CLEARS ALL THE ENTRIES CONTENTS
def clear_entry(test_entry):
    test_entry.delete(0, END)


#   THIS FUNCTION WILL CLOSE THE PROGRAM ON CLICK OF THE exit_btn
def exit_program(window):
    exit = messagebox.askquestion('Exit Application', 'Are you sure you want to exit', icon='warning')

    if exit == 'yes':
        play_sound("page_transition")
        window.destroy()
    else:
        #   ELSE, JUST GO BACK TO THE APPLICATION SCREEN
        pass


#   FUNCTION WILL PLAY A SOUND
def play_sound(sound):
    from playsound import playsound
    playsound("./audio/" + sound + ".mp3")
