#   FUNCTION WILL WRITE TO A FILE
import json
from tkinter import messagebox


def write_to_file(object_param):
    #   TAKE THE object_param AND PARSE IT TO A JSON STRING
    json_object = json.dumps(object_param)

    try:
        # OPEN THE database.txt FILE WITH WRITE PRIVILEGES AND THE + MEANS THAT IT WILL CREATE THE FILE IF IT
        # DOESN'T EXIST
        with open("./database/database.txt", "w+") as text_file:
            text_file.write(json_object)
    except TypeError:
        messagebox.showerror("Type Error", TypeError)


#   FUNCTION WILL READ THE DATABASE FILE AND RETURN CONTENTS AS A DICTIONARY
def read_database_file():
    try:
        #   OPEN THE database FILE WITH READ PRIVILEGES
        with open("./database/database.txt", "r", encoding='utf-8-sig', errors='ignore') as text_file:
            dict_object = json.load(text_file, strict=False)
            return dict_object
    #     CATCH THE EXCEPTION IF THE FILE ISN'T FOUND
    except FileNotFoundError:
        messagebox.showerror("File Error", "Wrong file or file path")

