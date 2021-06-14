from tkinter import *

window = Tk()
window.title("Ithuba National Lottery")
window.geometry("550x500")


def play_again():
    pass


def claim_prize():
    pass


def exit_program():
    pass


heading_label = Label(window, text="Your lucky numbers were: ", fg="blue")
heading_label.place(x=10, y=10)

user_numbers_label = Label(window, text="2, 4, 6, 7, 22, 45", fg="blue")
user_numbers_label.place(x=10, y=50)

lotto_label = Label(window, text="The winning numbers are: ", fg="blue")
lotto_label.place(x=10, y=100)

lotto_numbers_label = Label(window, text="2, 4, 6, 7, 22, 45", fg="blue")
lotto_numbers_label.place(x=10, y=150)

add_btn = Button(window, text="Add new entry", command=play_again, fg="blue").place(x=10, y=200)
claim_btn = Button(window, text="Claim Prize", command=claim_prize, fg="blue").place(x=200, y=200)
exit_btn = Button(window, text="Exit programme", command=exit_program, fg="blue").place(x=400, y=200)

window.mainloop()
