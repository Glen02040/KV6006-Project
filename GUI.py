#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:00:12 2020

@author: justi
"""

import csv
from tkinter import *
from tkinter import messagebox as msb
from tempfile import NamedTemporaryFile
import shutil
from tkinter.ttk import *
import os 

root = Tk()
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
    
        button3 = Button(root, text="Cancel", command=cancel)
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
# =============================================================================
#         filename = '/Users/justi/Desktop/IoT/Assignment_2/Store.csv'
#         tempfile = NamedTemporaryFile(delete=False)
# 
#         fields = ['id', 'product_name', 'quantity']
# 
#         with open(filename, 'r') as csvfile, tempfile:
#             reader = csv.DictReader(csvfile)
#             writer = csv.DictWriter(tempfile, fieldnames=fields)
#             for row in reader:
#                 if row['product_name'] == str(Data[index][1]):
#                     print('updating the amount of ', row['product_name'])
#                     row['quantity'] = TheAmount
#                 row = {'id':row['id'],'product_name': row['product_name'], 'quantity': row['quantity']}
#                 writer.writerow(dict(row))
#          shutil.move(tempfile, filename)
# =============================================================================
        prod_loc = Data[index][3]
        print(prod_loc)
        os.system('python DistanceCalc.py')
        
        msb.showinfo(title="Success", message="Order was placed! \n")
        
        listbox1.config(state="normal")
        button1.config(state="normal")
        
        
    

def cancel():
        listbox1.config(state="normal")
        button1.config(state="normal") 
        Productlabel.destroy()
        Productlabel1.destroy()
        Orderlabel.destroy()
        OrderEntry.destroy()
        amountlabel1.destroy()
        amountlabel.destroy()
        btn2.destroy()
        button3.destroy()
        index = None
        
  

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


root.mainloop()
