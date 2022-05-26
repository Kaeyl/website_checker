#Import the required Libraries
from tkinter import *
from tkinter import ttk
import urllib.request


def open_window():
    #Create an instance of Tkinter frame
    win = Tk()

    #Set the geometry of Tkinter frame
    win.geometry("300x300")
    user_input = ''
    #Initialize a Label to display the User Input
    label = Label(win, text="Please enter your website", font=("Arial 12"))
    label.pack()

    #Create an Entry widget to accept User Input
    entry = Entry(win, width= 40)
    entry.focus_set()
    entry.pack()
    #Create a Button to validate Entry Widget
    ttk.Button(win, text= "Search",width= 40, command=lambda: [display_text(entry, label, win, label2)]).pack(pady=5)
    ttk.Button(win, text="Exit", width=40, command=lambda: [close_window(win)]).pack(pady=5)

    label2 = Label(win, text="", font=("Courier 12"))
    label2.pack()

    win.mainloop()

def display_text(entry, label, win, label2):
    # here we will validate user input, if valid window will close. else it will require the user to try again
    captured_string = entry.get()
    label.configure(text=captured_string)
    display_text.user_input = captured_string
    accepted_url_starts = ["www.", "http://", "https://"]
    accepted_url_ends_with = [".com", ".net",".au", ".eu",".co",".org", ".io",]
    if captured_string == '':
        print("sorry input was empty")
        if captured_string == '':
            captured_string = "Information cannot be empty"
            label.configure(text=captured_string)

    if captured_string != '':
        position = 0
        for i in accepted_url_starts:
            validate_accepted_url_position = accepted_url_starts[position]
            valid_response_start_response = captured_string.startswith(validate_accepted_url_position)
            position = position + 1
            if valid_response_start_response == True:
                print("we found a Valid start")
                label.configure(text=captured_string)
                label2.configure(text=captured_string)
                break
        position = 0
        for i in accepted_url_ends_with:
            validate_accepted_url_end_position = accepted_url_ends_with[position]
            valid_response_end_response = captured_string.endswith(validate_accepted_url_end_position)
            position = position + 1
            if valid_response_end_response == True:
                print("we found a valid end")
                position = 0
                break
        if valid_response_start_response == True and  valid_response_end_response == True:
            all_conditions_have_been_met = True

            if all_conditions_have_been_met == True:
                crafter_website_checks = [captured_string]
                captured_string_start = captured_string.startswith("www.")
                if captured_string_start == True:
                    position = 1
                    for i in accepted_url_starts:
                        add_crafter_url = accepted_url_starts[position] + captured_string
                        crafter_website_checks.insert(0, add_crafter_url)
                        position = position + 1
                        if position >=3:
                            break
            website_query(captured_string, label2, crafter_website_checks)
        else:
            label2.configure(text="sorry, all conditions \nneed to be met\nmake sure your website\n query starts with www. \n and ends with .com")


def close_window(win):

    win.destroy()


def website_query(response, label2, crafter_website_checks):
    position = 0

    for i in crafter_website_checks:
        website_check = urllib.request.urlopen(crafter_website_checks[position]).getcode()
        print(website_check)

        if website_check == 200:
            response = crafter_website_checks[position]
            print(response)
            print("the value for this is " + response)
            valid_response_label_response = response + "\nIs live"
            label2.configure(text=valid_response_label_response)
            break
        if website_check != 200:
            print("This site is not live or does not exist")
            break
        position = position + 1


open_window()
