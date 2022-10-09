"""Main Address Book application 

Creater: Gagan gupta,  october 2022

Bridge functions to connect gui and database. 
"""


"""from cProfile import label
from cgitb import text
from email.headerregistry import Address
from socket import AddressInfo"""
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from tkinter.tix import ROW, Tree
"""from tkinter import font
from turtle import width"""

# colors
co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456F0"

window = Tk()
window.title("")
window.geometry('600x700')
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)


# GUIframes

frame_up = Frame(window, width=600, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=600, height=400, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=600, height=300, bg=co2)
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1, sticky=NW)

# function


def show():
    global tree

    listheader = ['Name', 'Address', 'Pincode', 'Mobile', 'Birth', ]

    demo_list= [['Gagan Gupta', 'Amarpur Umaria MP', '484661', '7000513498', '12/06/2000' ]]

    tree = ttk.Treeview(frame_table, selectmode="extended",
                        columns=listheader, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # tree head

    tree.heading(0, text='Name', anchor=NW)
    tree.heading(1, text='Address', anchor=NW)
    tree.heading(2, text='Pincode', anchor=NW)
    tree.heading(3, text='Mobile', anchor=NW)
    tree.heading(4, text='Birth', anchor=NW)

    # tree column

    tree.column(0, width=120, anchor=NW)
    tree.column(1, width=200, anchor=NW)
    tree.column(2, width=80, anchor=NW)
    tree.column(3, width=100, anchor=NW)
    tree.column(4, width=80, anchor=NW)

    for item in demo_list:
        tree.insert('', 'end', values=item)

show()


# frameup widgets

app_name = Label(frame_up, text="ADDRESS BOOK", height=1,
                 font=('verdana 20 bold'), bg=co2, fg=co0)
app_name.place(x=170, y=5)

# framedown widgets

l_name = Label(frame_down, text=" First Name:* ", width=25,
               height=1, font=('Ivy 12 '), bg=co0, anchor=NW)
l_name.place(x=10, y=10)
e_name = Entry(frame_down, width=20, justify='left',
               highlightthickness=1, relief="solid")
e_name.place(x=120, y=10)

l_name = Label(frame_down, text=" Last Name:* ", width=25,
               height=1, font=('Ivy 12 '), bg=co0, anchor=NW)
l_name.place(x=10, y=40)
e_name = Entry(frame_down, width=20, justify='left',
               highlightthickness=1, relief="solid")
e_name.place(x=120, y=40)

l_address = Label(frame_down, text=" Address1:* ",  height=1,
                  font=('Ivy 12 '), bg=co0, anchor=NW)
l_address.place(x=10, y=70)
e_address = Entry(frame_down, width=30, justify='left',  relief="solid",)
e_address.place(x=120, y=70)

l_address = Label(frame_down, text=" Address2:* ",  height=1,
                  font=('Ivy 12 '), bg=co0, anchor=NW)
l_address.place(x=10, y=100)
e_address = Entry(frame_down, width=30, justify='left',  relief="solid")
e_address.place(x=120, y=100)

l_city = Label(frame_down, text=" District:* ", width=25,
               height=1, font=('Ivy 12 '), bg=co0, anchor=NW)
l_city.place(x=10, y=130)
e_city = Entry(frame_down, width=25, justify='left',  relief="solid")
e_city.place(x=120, y=130)


l_pincode = Label(frame_down, text=" Pincode:* ",  height=1,
                  font=('Ivy 12 '), bg=co0, anchor=NW)
l_pincode.place(x=10, y=160)
e_pincode = Entry(frame_down, width=10, justify='left',  relief="solid")
e_pincode.place(x=120, y=160)

l_state = Label(frame_down, text=" State:* ", width=25,
                height=1, font=('Ivy 12 '), bg=co0, anchor=NW)
l_state.place(x=10, y=190)
e_state = Entry(frame_down, width=25, justify='left',  relief="solid")
e_state.place(x=120, y=190)

l_country = Label(frame_down, text=" Country:* ", width=25,
                  height=1, font=('Ivy 12 '), bg=co0, anchor=NW)
l_country.place(x=10, y=220)
e_country = Entry(frame_down, width=25, justify='left',  relief="solid")
e_country.place(x=120, y=220)

l_mobile = Label(frame_down, text=" Mobile:* ",  height=1,
                 font=('Ivy 12 '), bg=co0, anchor=NW)
l_mobile.place(x=10, y=250)
e_mobile = Entry(frame_down, width=20, justify='left',  relief="solid")
e_mobile.place(x=120, y=250)

l_gmail = Label(frame_down, text=" Email:* ",  height=1,
                font=('Ivy 12 '), bg=co0, anchor=NW)
l_gmail.place(x=10, y=280)
e_gmail = Entry(frame_down, width=25, justify='left',  relief="solid")
e_gmail.place(x=120, y=280)

l_dob = Label(frame_down, text=" Birth:* ", width=25,
              height=1, font=('Ivy 12 '), bg=co0, anchor=NW)
l_dob.place(x=10, y=310)
e_dob = Entry(frame_down, width=15, justify='left',  relief="solid")
e_dob.place(x=120, y=310)

l_note = Label(frame_down, text=" NOTES:* ",  height=1,
               font=('Ivy 12 '), bg=co0, anchor=NW)
l_note.place(x=10, y=340)
e_note = Entry(frame_down,  width=50,  justify='left',   relief="solid")
e_note.place(x=120, y=340)

# button creating

b_save = Button(frame_down, text="Save", height=1, width=10,
                bg=co1, fg=co0, font=('lvy 10 bold'))
b_save.place(x=120, y=370)

b_search = Button(frame_down, text="Search", height=1,
                  width=8, bg=co1, fg=co0, font=('lvy 10 bold'))
b_search.place(x=350, y=10)

e_search = Entry(frame_down, width=20, justify='left',
                 font=('lvy 11'), relief="solid")
e_search.place(x=430, y=10)

b_add = Button(frame_down, text="Add", height=1, width=8,
               bg=co1, fg=co0, font=('lvy 10 bold'))
b_add.place(x=350, y=50)

b_edit = Button(frame_down, text="Update", height=1, width=8,
                bg=co1, fg=co0, font=('lvy 10 bold'))
b_edit.place(x=350, y=90)

b_view = Button(frame_down, text="View", height=1, width=8,
                bg=co1, fg=co0, font=('lvy 10 bold'))
b_view.place(x=350, y=130)

b_delete = Button(frame_down, text="Remove", height=1,
                  width=8, bg=co1, fg=co0, font=('lvy 10 bold'))
b_delete.place(x=350, y=170)

window.mainloop()
