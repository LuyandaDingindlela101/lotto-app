from tkinter import *
from database import *
from smtplib import SMTP
from useful_functions import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")


def validate_entries():
    database_contents = read_database_file()

    try:
        acc_holder = acc_holder_entry.get()
        acc_number = int(acc_number_entry.get())
        bank = banks_options.get()

        if not_empty(acc_holder) and not_empty(acc_number) and not_empty(bank):
            if type(acc_number) == int and len(str(acc_number)) == 10:
                if bank in ["Capitec", "Nedbank", "First National Bank", "Standard Bank"]:
                    bank_details = {
                        "account holder": acc_holder,
                        "account number": acc_number,
                        "bank name": bank
                    }

                    database_contents["banking details"] = bank_details
                    write_to_file(database_contents)
                    play_sound("validation_success")
                else:
                    messagebox.showerror("Bank Error", "Please check bank input")
            else:
                messagebox.showerror("Account number Error", "Please check account number input")
        else:
            messagebox.showerror("Validation", "Inputs cant be empty")

    except ValueError:
        messagebox.showerror("Value Error", "Please check your inputs")


def send_email():
    validate_entries()

    database_contents = read_database_file()
    database_contents = json.dumps(database_contents)

    try:
        sender_email = "luyandadingindlela@gmail.com"
        receiver_email = "lcproject101@gmail.com"
        password = "LKKHZ5@h0m3"
        server = SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, 'This is a test email.')
        print("the message has been successfully sent")

    except Exception as err:
        print("Something went wrong..", err)
    finally:
        server.close()
        play_sound("page_transition")
        window.destroy()


def clear_entries():
    clear_entry(acc_holder_entry)
    clear_entry(acc_number_entry)
    clear_entry(banks_options)


def exit():
    exit_program()


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

banks_label = Label(window, text="Please choose your bank", fg="blue")
banks_label.place(x=10, y=100)
banks_options = Combobox(window, value=["Capitec", "Nedbank", "First National Bank", "Standard Bank"])
banks_options.place(x=300, y=100)

email_btn = Button(window, text="Email Details", command=send_email, fg="blue").place(x=10, y=200)
clear_btn = Button(window, text="Clear entries", command=clear_entries, fg="blue").place(x=200, y=200)
exit_btn = Button(window, text="Exit programme", command=exit_program, fg="blue").place(x=400, y=200)

window.mainloop()
