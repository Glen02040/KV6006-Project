#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:00:12 2020
@author: justi, glen, kieran
"""

import csv
from tkinter import *
from tkinter import messagebox as msb
from tempfile import NamedTemporaryFile
import shutil
from tkinter.ttk import *
import requests


root = Tk()
root.geometry("300x250")
product = StringVar()
amount = StringVar()
#-----------------------------------------------------------------------------------------------

def show():
    global Productlabel, amountlabel, index
    if listbox1.curselection():
        index = listbox1.curselection()[0]
    else:
        index = -1

    if(index==-1):
        print("error")
        msb.showerror(title="Error", message="Please select a product from the list")
    else:
        Productlabel = Label(root, text="Quantity in the store")
        Productlabel.grid(row=7, column=0)
        amountlabel = Label(root, text = Data[index][2])
        amountlabel.grid(row=7, column=1)


def showProducer():
    global Productlabel1, amountlabel1, index
    if listbox1.curselection():
        index = listbox1.curselection()[0]
    else:
        index = -1

    if(index==-1):
        print("error")
        msb.showerror(title="Error", message="Please select a product from the list")
    else:
        File1 = open('Producer.csv')
        Reader1 = csv.reader(File1)
        Data1 = list(Reader1)
        del(Data1[0])

        list_of_products1 = []
        for x in list(range(0,len(Data1))):
            list_of_products1.append(Data1[x][1])

        Productlabel1 = Label(root, text="Quantity in the producer")
        Productlabel1.grid(row=8, column=0)
        amountlabel1 = Label(root, text = Data1[index][2])
        amountlabel1.grid(row=8, column=1)

    return None


def placeOrder():
    global Orderlabel, OrderEntry, index, btn2, button3
    if listbox1.curselection():
        index = listbox1.curselection()[0]
    else:
        index = -1

    if(index==-1):
        print("error")
        msb.showerror(title="Error", message="Please select a product from the list")
    else:
        Orderlabel = Label(root, text="Quantity to order")
        Orderlabel.grid(row=10, column=0)

        OrderEntry = Entry(root, textvariable = amount, width = 10)
        OrderEntry.grid(row=10, column=1)

        btn2 = Button(root, text="Confirm", command=order)
        btn2.grid(row=10, column=2)

        button3 = Button(root, text="Exit", command=exit)
        button3.grid(row=10, column=3)

        listbox1.config(state="disabled")
        button1.config(state="disabled")



def order():
    global prod_loc
    TheAmount = amount.get()
    if(TheAmount==""):
        print("error")
        msb.showerror(title="error", message="Please provide the amount of product to order")
    else:
        prod_loc = Data[index][3]
        #os.system('python DistanceCalc.py')

        api_file = open("google-api-key.txt", "r")
        api_key = api_file.read()
        api_file.close()

        # home address input
        store = "Newcastle, Uk"
        print(store)

        # work address input
        producer = prod_loc
        print(producer)

        # base url
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

        # get response
        call = url + "origins=" + store + "&destinations=" + producer + "&key=" + api_key
        print(call)
        r = requests.get(call)

        # return time as text and as seconds
        time = r.json()["rows"][0]["elements"][0]["duration"]["text"]

        seconds = r.json()['rows'][0]['elements'][0]['duration']['value']

        # print the message and the delivery time
        msb.showinfo(title="Success", message="Order was placed! \n\n The delivery time:" + time)


        listbox1.config(state="normal")
        button1.config(state="normal")




def cancel():
        listbox1.config(state="normal")
        button1.config(state="normal")
        Productlabel.grid_remove()
        Productlabel1.grid_remove()
        Orderlabel.destroy()
        OrderEntry.destroy()
        amountlabel1.destroy()
        amountlabel.destroy()
        btn2.destroy()
        button3.destroy()
        index = None

def exit():
    root.destroy()

#-----------------------------------------------------------------------------------------------
File = open('Store.csv')
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0])

list_of_products = []
for x in list(range(0,len(Data))):
    list_of_products.append(Data[x][1])

lblProduct = Label(root, text="List of all products").grid(row=0, column = 0)

var = StringVar(value = list_of_products)
listbox1 = Listbox(root, listvariable = var)
listbox1.grid(row=2 , column=0, rowspan=3)


btn1 = Button(root, text="Check storage", command=show)
btn1.grid(row=2, column=1)

btn1 = Button(root, text="Check producer", command=showProducer)
btn1.grid(row=3, column=1)

button1 = Button(root, text="Order", command=placeOrder)
button1.grid(row=4, column=1)

button3 = Button(root, text="Exit", command=exit)
button3.grid(row=5, column=1)


root.mainloop()
