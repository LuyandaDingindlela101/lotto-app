#   Luyanda Dingindlela | Class 1
from email.mime.multipart import MIMEMultipart
from tkinter import *
from database import *
from smtplib import SMTP
from useful_functions import *
from tkinter.ttk import Combobox
from email.mime.multipart import MIMEMultipart
from classes.bank_details import BankingDetails

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")


#   FUNCTION WILL CHECK IF ALL THE ENTRIES ARE VALID OR NOT
def validate_entries():
    #   GET ALL THE CONTENTS OF THE database FILE
    database_contents = read_database_file()

    try:
        #   GET THE VALUES OF THE ENTRIES
        acc_holder = acc_holder_entry.get()
        acc_number = int(acc_number_entry.get())
        bank = banks_options.get()

        #   CHECK IF THE ENTRIES ARENT EMPTY
        if not_empty(acc_holder) and not_empty(acc_number) and not_empty(bank):
            #   CHECK IF THE LENGTH OF THE acc_number IS LONGER THAN 10 AND THAT acc_number IS AN INTEGER
            if type(acc_number) == int and len(str(acc_number)) == 10:
                #   MAKE SURE THAT THE USER ONLY CHOSE OPTIONS THAT ARE IN THE COMBOBOX
                if bank in ["Capitec", "Nedbank", "First National Bank", "Standard Bank"]:
                    #   CREATE AN INSTANCE OF THE BankingDEtails CLASS AND ASSIGN THE VALUES
                    bank_details = BankingDetails(acc_holder, acc_number, bank)
                    #   CALL THE make_dict() FUNCTION SO WE CAN SAVE THE UPDATED database_contents TO THE database FILE
                    database_contents["banking details"] = bank_details.make_dict()
                    #   SAVE THE UPDATED database_contents
                    write_to_file(database_contents)
                    play_sound("validation_success")
                    return True
                #   IF THE USER ENTERS SOMETHING THAT ISN'T IN THE COMBOBOX, DISPLAY THE ERROR
                else:
                    messagebox.showerror("Bank Error", "Please check bank input")
                    return False
            #   IF THE acc_number IS NOT VALID, DISPLAY THE ERROR TO THE USER
            else:
                messagebox.showerror("Account number Error", "Please check account number input")
                return False
        #   IF THE INPUTS ARE EMPTY, DISPLAY THE ERROR TO THE USER
        else:
            messagebox.showerror("Validation", "Inputs cant be empty")
            return False
    #   HANDLE THE ValueError ERROR
    except ValueError:
        messagebox.showerror("Value Error", "Please check your inputs")
        return False


#   FUNCTION SENDS EMAIL IF VALIDATION PASSES
def send_email():
    #   CHECK IF THE VALIDATION PASSED OR NOT
    if validate_entries():
        #    GET THE CONTENTS OF THE database FILE
        database_contents = read_database_file()

        try:
            sender_email = "luyandadingindlelaemail@gmail.com"
            receiver_email = database_contents["email"]
            password = "Ld0740285889"
            message = "Congratulations, you won. \n" + "Mr " + database_contents["name"] + ". Your player id is: " + \
                      str(database_contents["player id"]) + ", you won: R" + str(database_contents["total winnings"]) + \
                      ". Your prize will be delivered at: " + database_contents["address"] + \
                      ". Please have your id ready so we can confirm if " + str(database_contents["id number"]) + \
                      " is your id. \n" + "Your lucky numbers were: " + str(database_contents["user sets"]) + \
                      " and the winning numbers were: " + str(database_contents["winning set"]) + \
                      ". Please also confirm if the account holders name: " + \
                      database_contents["banking details"]["account holder"] + \
                      ", account number: " + str(database_contents["banking details"]["account number"]) + \
                      " and bank name: " + database_contents["banking details"]["bank name"] + "are correct."

            email_options = MIMEMultipart("alternative")
            email_options["Subject"] = "Ithuba National Lottery"

            server = SMTP('smtp.gmail.com', 587)
            server.starttls()

            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            messagebox.showinfo("Email success", "Please check your emails")

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


#   FUNCTION WILL EXIT PROGRAM
def exit():
    exit_program(window)


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
