#Import the required Libraries
from tkinter import *
from tkinter import ttk
import urllib.request


# This section is for managing the tkinter window.
def open_window():
    #Create an instance of Tkinter frame
    win = Tk()

    #Set the geometry of Tkinter frame
    win.geometry("300x250")
    win.maxsize(width="300", height="250")
    win.eval('tk::PlaceWindow . center')
    big_frame = ttk.Frame(win)
    big_frame.pack(fill="both", expand=False)

    # This will initiate the theme of the tkinter window.
    # The theme being used is azure downloaded from (https://github.com/rdbende/Azure-ttk-theme)
    win.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    win.tk.call("set_theme", "dark")

    #Initialize a Label to display the User Input
    label = Label(win, text="Please enter your website", font=("Arial 12"))
    label2 = Label(win, text="", font=("Courier 12"))


    #Create an Entry widget to accept User Input
    entry = Entry(win, width= 42, bg="#FFFFFF", fg="#000000")
    entry.focus_set()


    #Create a Button to validate Entry Widget
    button1 = ttk.Button(win, text= "Search",width= 40, command=lambda: [display_text(entry, label, win, label2)])
    button2 = ttk.Button(win, text="Exit", width=40, command=lambda: [close_window(win)])



    # This will allow you to manage the order of the widgets
    label.pack()
    entry.pack()
    button1.pack(pady=5)
    button2.pack(pady=5)
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
        if captured_string == '':
            captured_string = "Information cannot be empty"
            label.configure(text=captured_string)
    #If the user input is not empty, then we will process the information.
    if captured_string != '':
        position = 0
        for i in accepted_url_starts:
            validate_accepted_url_position = accepted_url_starts[position]
            valid_response_start_response = captured_string.startswith(validate_accepted_url_position)
            position = position + 1
            if valid_response_start_response == True:
                label.configure(text=captured_string)
                label2.configure(text=captured_string, fg="#228B22")
                break
        #we need to reset the position to 0 so the rest of the code can use the same variable.
        position = 0
        #here we need to iterate over each position within the list using the position as the indicator.
        for i in accepted_url_ends_with:
            validate_accepted_url_end_position = accepted_url_ends_with[position]
            valid_response_end_response = captured_string.endswith(validate_accepted_url_end_position)
            position = position + 1
            if valid_response_end_response == True:
                break
        #If all of the conditions are true then we will craft a valid string and submit it.
        if valid_response_start_response == True and  valid_response_end_response == True:
            #assigning all conditions to be true to process this condition.
            all_conditions_have_been_met = True
            if all_conditions_have_been_met:
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
            label2.configure(text="sorry, all conditions \nneed to be met.\nmake sure your website\n query starts with www. \n and ends a valid\n extention", fg="#FF8C00")

def close_window(win):
    win.destroy()
def website_query(response, label2, crafter_website_checks):
    position = 0

    for i in crafter_website_checks:
        try:
             website_check = urllib.request.urlopen(crafter_website_checks[position]).getcode()
        except:
            label2.configure(text="This site does not exist,\n or it is not live", fg="#FF8C00")
            continue
        if website_check == 200:
            response = crafter_website_checks[position]
            valid_response_label_response = response + "\nIs live"
            label2.configure(text=valid_response_label_response, fg="#228B22")
            break
        if website_check != 200:
            break
        position = position + 1


open_window()
