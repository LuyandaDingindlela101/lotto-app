import requests
from tkinter import *
from database import *
from useful_functions import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")

exchange_rates = []


#   FUNCTION WILL CLEAR ALL ENTRIES
def clear_entries():
    clear_entry(base_currency)
    clear_entry(new_currency)


#   FUNCTION WILL EXIT PROGRAM
def exit():
    exit_program(window)


#   FUNCTION WILL DETERMINE WHETHER USER PROCEEDS TO NEXT SCREEN OR NOT
def proceed():
    proceed = messagebox.askquestion("Ready To Proceed?", "Are you ready to proceed?")

    if proceed == "yes":
        play_sound("page_transition")
        window.destroy()
        import banking_input
    else:
        pass


def populate_comboboxes():
    global exchange_rates

    #   SEND A GET REQUEST TO THE SUPPLIED URL
    response = requests.get("https://v6.exchangerate-api.com/v6/58a779d694f48375cb4bb0a0/latest/ZAR")
    json_response = response.json()

    for rate in json_response["conversion_rates"]:
        exchange_rates.append(rate)


#   FUNCTION CONVERTS TOTAL WINNINGS AND DISPLAYS THE RESULT TO THE USER
def convert_currency():
    try:
        from_currency = base_currency.get().upper()
        to_currency = new_currency.get().upper()

        if test_empty(from_currency) and test_empty(to_currency):
            play_sound("validation_success")

            database_contents = read_database_file()
            amount = database_contents["total winnings"]
            #   SEND A GET REQUEST TO THE SUPPLIED URL
            response = requests.get(
                "https://v6.exchangerate-api.com/v6/58a779d694f48375cb4bb0a0/latest/" + from_currency)
            json_response = response.json()

            #   RETURN THE CONVERTED AMOUNT
            converted_winnings = float(amount) * float(json_response["conversion_rates"][to_currency])
            #   SAVE THE converted_currency TO THE database FILE
            database_contents["converted winnings"] = converted_winnings
            #   UPDATE THE database FILE
            write_to_file(database_contents)

            #     DISPLAY THE converted_currency TO THE USER
            messagebox.showinfo("Converted Currency", "Your prize is now: " + str(converted_winnings))
        else:
            messagebox.showerror("Validation", "Please check your inputs")
    except KeyError:
        messagebox.showerror("Key Error", "Please check your inputs")


populate_comboboxes()

banks_label = Label(window, text="Please choose base currency", fg="blue")
banks_label.place(x=10, y=10)
base_currency = Combobox(window, values=exchange_rates)
base_currency.place(x=10, y=50)

banks_label = Label(window, text="Please choose currency to convert to", fg="blue")
banks_label.place(x=250, y=10)
new_currency = Combobox(window, values=exchange_rates)
new_currency.place(x=250, y=50)

convert_btn = Button(window, text="Convert", command=convert_currency, fg="blue").place(x=10, y=100)
clear_btn = Button(window, text="Clear entries", command=clear_entries, fg="blue").place(x=200, y=100)
exit_btn = Button(window, text="Exit programme", command=exit, fg="blue").place(x=400, y=100)

proceed_btn = Button(window, text="Proceed", command=proceed, fg="blue", width=62).place(x=10, y=150)

window.mainloop()
