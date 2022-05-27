from tkinter import *
from tkinter import ttk
import website_response
import website_crawl
import bulk_scan
import store_scans


def open_window():
    #Create an instance of Tkinter frame
    win = Tk()
    #Set the geometry of Tkinter frame
    win.wm_title("Website Validator")
    win.overrideredirect(False)
    win.geometry("300x350")
    win.eval('tk::PlaceWindow . center')
    big_frame = ttk.Frame(win)
    big_frame.pack(fill="both", expand=False)

    # make a frame for the title bar
    options_bar = Frame(win, bg='white', relief='solid', bd=False)
    # put a close button on the title bar
    close_button_external_links = Button(options_bar, width="14", text='External Links', bd=0.5, command=website_crawl.check_external_links)
    close_button_bulk_scan = Button(options_bar, width="14", text='Bulk Scan', bd=0.5, command=bulk_scan.scan_from_file)
    close_button_store_output= Button(options_bar,width="14", text='Store Output', bd=0.5, command=store_scans.store_scans_in_file)
    close_button_external_links.pack(side=RIGHT)
    close_button_bulk_scan.pack(side=LEFT)
    close_button_store_output.pack(side=LEFT)
    options_bar.pack(expand=0, fill=X, side=TOP)
    win.maxsize(width="300", height="300")
    # This will initiate the theme of the tkinter window.
    # The theme being used is azure downloaded from (https://github.com/rdbende/Azure-ttk-theme)
    win.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    win.tk.call("set_theme", "dark")
    #Initialize a Label to display the User Input
    label = Label(win, text="Please enter your website", height=2, font=("Arial 12"))
    label2 = Label(win, text="", font=("Courier 12"))
    #Create an Entry widget to accept User Input
    entry = Entry(win, width= 42, bg="#FFFFFF", fg="#000000")
    entry.focus_set()
    #Create a Button to validate Entry Widget
    button1 = ttk.Button(win, text= "Search",width= 40, command=lambda: [website_response.display_text(entry, label, win, label2)])
    button2 = ttk.Button(win, text="Exit", width=40, command=lambda: [website_response.close_window(win)])

    # This will allow you to manage the order of the widgets
    label.pack(fill="both")
    entry.pack()
    button1.pack(pady=5)
    button2.pack(pady=5)
    label2.pack()
    win.mainloop()

open_window()