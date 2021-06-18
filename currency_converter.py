import requests
from tkinter import *
from useful_functions import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")


def clear_entries():
    clear_entry(base_currency)
    clear_entry(new_currency)


def exit():
    exit_program(window)


def proceed():
    pass


def get_currency():
    url = "https://v6.exchangerate-api.com/v6/58a779d694f48375cb4bb0a0/latest/USD"
    responce = requests.get(url)
    responce.json()
    print(responce)


banks_label = Label(window, text="Please choose base curency", fg="blue")
banks_label.place(x=10, y=10)
base_currency = Combobox(window)
base_currency.place(x=10, y=50)

banks_label = Label(window, text="Please choose currency to convert to", fg="blue")
banks_label.place(x=250, y=10)
new_currency = Combobox(window)
new_currency.place(x=250, y=50)

add_btn = Button(window, text="Proceed", command=proceed, fg="blue").place(x=10, y=100)
clear_btn = Button(window, text="Clear entries", command=clear_entries, fg="blue").place(x=200, y=100)
exit_btn = Button(window, text="Exit programme", command=exit, fg="blue").place(x=400, y=100)

get_currency()

window.mainloop()