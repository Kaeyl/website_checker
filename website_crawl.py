from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import pprint

def show_external_links(win, entry, button1, button2, label, label2):
    global list
    entry.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    label.pack_forget()
    label2.pack_forget()
    v = Scrollbar(win, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    text = Text(win, width=60, height=12, yscrollcommand=v.set)
    position = 0
    for i in list:
        print(list[position])
        if list[position] == None:
            list.remove(list[position])
        text.insert(END, list[position] + "\n")
        text.configure(font=("Times New Roman", 12))
        position = position + 1
    v.config(command=text.yview)
    text.pack()
    button_undefined = ttk.Button(win, text="Exit", width=65).pack()

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
        pprint.pprint(ammended_list[position])
        position = position + 1
    list = ammended_list
    return list

