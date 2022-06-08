import urllib.request
from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

from website_scanner import website_response


def show_external_links(win, entry, button1, button2, label, label2):
    global list
    edited_list = []
    for i in list:
        if i not in edited_list:
            edited_list.append(i)
    entry.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    label.pack_forget()
    label2.pack_forget()
    v = Scrollbar(win, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    text = Text(win, width=60, height=12, yscrollcommand=v.set)
    position = 0
    for i in edited_list:
        if edited_list[position] == None:
            edited_list.remove(edited_list[position])
        text.insert(END, edited_list[position] + "\n")
        text.configure(font=("Times New Roman", 12), fg="#f2f4f7")
        position = position + 1
    v.config(command=text.yview)
    text.pack()
    button_process = ttk.Button(win, width=67, text='Process', command=lambda: [(valid_links(win, edited_list, text), button_process.forget(),button_exit.forget(),button_store.forget())])
    button_exit = ttk.Button(win,width=32, text='Exit', command=win.destroy)
    button_store = ttk.Button(win,width=32, text='Store', command=lambda: [])
    button_process.pack()
    button_exit.pack(side=LEFT)
    button_store.pack(side=RIGHT)

def check_external_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
    handle_external_links(links)

def handle_external_links(links):
    global list
    ammended_list = []
    position = 0
    for i in links:
        ammended_list.append(links[position])
        position = position + 1
    list = ammended_list
    return list

def valid_links(win, list, text):
    global keep_list
    text.delete("1.0","end")
    live_list = []
    keep_list = []
    not_valid_links = []
    position = 0
    print(list)
    for i in list:
        if list[position].startswith("http"):
            keep_list.append(list[position])
        else:
            not_valid_links.append(list[position])
        position = position + 1
    position = 0

    # Take the list from show_external_links and scans them for 200 code. If there is a 200 code then it will show up in green
    for i in keep_list:
        try:
            web_requests = requests.get(keep_list[position])
            if web_requests.status_code >= 200:
                live_list.append(keep_list[position] + "\n")
                text.insert(INSERT, live_list[position])
                # print(web_requests)
        except:
            pass
        position = position + 1
    print(not_valid_links)
    text.configure(font=("Times New Roman", 12), fg="#228B22", height=13)
    text.pack()
    scan_live_sites = ttk.Button(win, width=67, text='Scan Live Sites', command=lambda: [()])
    scan_live_sites.pack(expand=True, fill=Y)
    
