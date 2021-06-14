from dateutil.relativedelta import relativedelta

from person import *
from tkinter import *
from useful_functions import *

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")


#   FUNCTION CLEARS ALL THE ENTRIES CONTENTS
def clear_entries():
    #   CALL THE clear_entry() FUNCTION TO CLEAR THE ENTRIES
    clear_entry(username_entry)
    clear_entry(address_entry)


#   FUNCTION WILL CHECK AGE AND DETERMINE IF THE USER CAN CONTINUE INSIDE OR NOT.
def check_age():
    #   IMPORT THE rsaidnumber MODULE
    import rsaidnumber
    #   IMPORT THE date FROM THE datetime MODULE
    from datetime import date
    #   GET TODAYS DATE
    today = date.today()
    #   GET THE USERS id_number
    id_number = id_entry.get()

    #   TEST IF id_number IS VALID
    if test_id_number(id_number):
        id_number = rsaidnumber.parse(id_number)
        date_of_birth = id_number.date_of_birth
        difference = relativedelta(today, date_of_birth.date())
        age = difference.years

        if age >= 18:
            messagebox.showinfo("Age Verification", "Lets Play")
            window.destroy()
            import lotto_input
        else:
            messagebox.showerror("Age Verification", "You are too young to play. Please try again in " + 18 - age + " years”")
    else:
        print("id not valid")


def exit_app():
    exit_program(window)


def validate_entries():
    name = username_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    id_number = id_entry.get()

    #   TEST IF ALL THE INPUTS ARENT EMPTY
    if test_empty(name) and test_empty(email) and test_empty(address) and test_empty(id_number):
        if test_type(name) and test_id_number(id_number):
            player_id = id_number[::-1]
            print(player_id)
            person = Person(name, email, address, player_id, id_number)
            print(person)
        else:
            messagebox.showerror("Type Error", "Please check the name and id number entries")
    else:
        messagebox.showerror("Empty Entries", "Entries cannot be empty")


def login():
    check_age()


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
