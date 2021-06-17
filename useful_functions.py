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
    if "@" not in email:
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


#   FUNCTION WILL WRITE TO A FILE
def write_to_file(to_write):
    try:
        # OPEN THE database.txt FILE WITH APPEND PRIVILEGES AND THE + MEANS THAT IT WILL CREATE THE FILE IF IT
        # DOESN'T EXIST
        with open("./database/database.txt", "a+") as file_to_save:
            file_to_save.write(to_write)
    except TypeError:
        messagebox.showerror("Type Error", TypeError)


#   FUNCTION WILL READ THE DATABASE FILE AND RETURN CONTENTS AS A LIST
def read_database_file():
    #   EMPTY LIST WILL HOLD FILE CONTENTS
    line_list = []

    try:
        #   OPEN THE database.txt FILE
        with open("./database/database.txt", "r") as file_to_read:
            #   LOOP THROUGH THE file_to_read
            for line in file_to_read:
                #   APPEND EACH line TO THE line_list
                line_list.append(line)

            #   RETURN THE line_list
            return line_list
    #     CATCH THE EXCEPTION IF THE FILE ISN'T FOUND
    except FileNotFoundError:
        messagebox.showerror("File Error", "Wrong file or file path")


def generate_lotto_number():
    import random
    return random.randint(1, 49)


