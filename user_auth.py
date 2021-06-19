from dateutil.relativedelta import relativedelta

from person import *
from tkinter import *
from useful_functions import *

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")


def login():
    if validate_entries():
        check_age()


#   FUNCTION WILL VALIDATE ALL ENTRIES
def validate_entries():
    #   GET ALL ENTRIES
    name = username_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    id_number = id_entry.get()

    #   TEST IF ALL THE INPUTS ARENT EMPTY
    if test_empty(name) and test_empty(email) and test_empty(address) and test_empty(id_number):
        #   MAKE SURE THE name ENTRY IS ONLY STRING AND MAKE THE id_number IS VALID
        if test_type(name):
            if test_id_number(id_number):
                #   GENERATE A player_id BY REVERSING THE id_number
                player_id = id_number[::-1]
                #   CREATE A Person DICTIONARY WITH THE USERS DETAILS
                person = {
                    "name": name,
                    "email": email,
                    "address": address,
                    "id number": id_number,
                    "player id": player_id
                }
                #   SAVE ALL THE DATA TO A TEXT FILE
                write_to_file(person)
                return True
            #   IF THE id_number IS INVALID, DISPLAY ERROR TO USER
            else:
                messagebox.showerror("Id Invalid", "Invalid ID number. Try again")
        #   IF THE name ENTRY HAS ANYTHING THAT ISN'T STRING
        else:
            messagebox.showerror("Type Error", "Please check the name and id number entries")
            return False
    #   IF ENTRIES ARE EMPTY, DISPLAY ERROR TO USER
    else:
        messagebox.showerror("Validation", "Please check your inputs")
        return False


#   FUNCTION WILL CHECK AGE AND DETERMINE IF THE USER CAN CONTINUE INSIDE OR NOT.
def check_age():
    #   IMPORT THE rsaidnumber MODULE
    import rsaidnumber
    #   IMPORT THE date FROM THE datetime MODULE
    from datetime import date
    #   GET TODAY'S DATE
    today = date.today()
    #   GET THE USERS id_number
    id_number = id_entry.get()

    #   TEST IF id_number IS VALID
    if test_id_number(id_number):
        id_number = rsaidnumber.parse(id_number)
        date_of_birth = id_number.date_of_birth
        difference = relativedelta(today, date_of_birth.date())
        age = int(difference.years)

        if age >= 18:
            messagebox.showinfo("Age Verification", "Lets Play")
            window.destroy()
            import lotto_input
        else:
            messagebox.showerror("Age Verification",
                                 "You are too young to play. Please try again in " + 18 - age + " years”")
    else:
        print("id not valid")


#   FUNCTION CLEARS ALL THE ENTRIES CONTENTS
def clear_entries():
    #   CALL THE clear_entry() FUNCTION TO CLEAR THE ENTRIES
    clear_entry(id_entry)
    clear_entry(email_entry)
    clear_entry(address_entry)
    clear_entry(username_entry)


#   FUNCTION WILL EXIT THE PROGRAM
def exit_app():
    #   CALL THE exit_program() TO EXIT THE PROGRAM AND PASS IN THE CURRENT window
    exit_program(window)


username_label = Label(window, text="Please enter your name", fg="blue")
username_label.place(x=10, y=10)
username_entry = Entry(window)
username_entry.place(x=200, y=10)

email_label = Label(window, text="Please enter your email", fg="blue")
email_label.place(x=10, y=50)
email_entry = Entry(window)
email_entry.place(x=200, y=50)

address_label = Label(window, text="Please enter your address", fg="blue")
address_label.place(x=10, y=100)
address_entry = Entry(window)
address_entry.place(x=200, y=100)

id_label = Label(window, text="Please enter your id number", fg="blue")
id_label.place(x=10, y=150)
id_entry = Entry(window)
id_entry.place(x=200, y=150)

verify_btn = Button(window, text="Validate entries", command=login, fg="blue").place(x=10, y=200)
clear_btn = Button(window, text="Clear entries", command=clear_entries, fg="blue").place(x=200, y=200)
exit_btn = Button(window, text="Exit programme", command=exit_app, fg="blue").place(x=400, y=200)

window.mainloop()
