from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")


def claim():
    pass


def clear_entries():
    pass


def exit_program():
    pass


chosen_bank = StringVar()
bank_options = ("Capitec", "Nedbank", "First National Bank", "Standard Bank")

acc_holder_label = Label(window, text="Please enter your account holder name", fg="blue")
acc_holder_label.place(x=10, y=10)
acc_holder_entry = Entry(window)
acc_holder_entry.place(x=300, y=10)

acc_number_label = Label(window, text="Please enter your account number", fg="blue")
acc_number_label.place(x=10, y=50)
acc_number_entry = Entry(window)
acc_number_entry.place(x=300, y=50)

banks_label = Label(window, text="Please enter your address", fg="blue")
banks_label.place(x=10, y=100)
banks_options = Combobox(window, value=["Capitec", "Nedbank", "First National Bank", "Standard Bank"])
banks_options.place(x=300, y=100)

claim_btn = Button(window, text="Validate entries", command=claim, fg="blue").place(x=10, y=200)
clear_btn = Button(window, text="Clear entries", command=clear_entries, fg="blue").place(x=200, y=200)
exit_btn = Button(window, text="Exit programme", command=exit_program, fg="blue").place(x=400, y=200)

window.mainloop()
