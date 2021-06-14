from tkinter import messagebox, END


def test_type(test_entry):
    try:
        if test_entry != str(test_entry):
            raise TypeError()
        else:
            return True
    except TypeError:
        print("Entry cannot contain integers ")
        return False


def test_empty(test_entry):
    try:
        if test_entry == "":
            raise ValueError()
        else:
            return True
    except ValueError:
        print('Cannot convert empty string')
        return False


def test_email(test_entry):
    email = test_entry.strip().lower()
    if not "@" in email:
        print("Invalid email")
        return False
    elif not email[-4:] in ".com.org.edu.gov.net":
        print("Invalid email")
        return False
    else:
        return True


def test_id_number(id_number):
    import rsaidnumber
    try:
        id_number = rsaidnumber.parse(id_number)
        return id_number.valid
    except ValueError:
        return False


#   FUNCTION CLEARS ALL THE ENTRIES CONTENTS
def clear_entry(test_entry):
    test_entry.delete(0, END)

#   THIS FUNCTION WILL CLOSE THE PROGRAM ON CLICK OF THE exit_btn
def exit_program(window):
    message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit', icon='warning')
    if message_box == 'yes':
        window.destroy()
    else:
        #   ELSE, JUST GO BACK TO THE APPLICATION SCREEN
        pass
