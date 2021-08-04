#Importing the libraries
import random as r
from tkinter import *
import pandas as pd

#Creating the different Window and setting up its background image
window=Tk()
window.geometry("500x260")
bgimg=PhotoImage(file="Path Of the Image")
bgimg=bgimg.subsample(2,2)
bglab=Label(window,image=bgimg)
bglab.place(x=0,y=0)

#Defining the variables
df=pd.read_csv("Path Of the Dataset")
a=["Milk","Eggs","Tea","Biscuit","Coffee","Jam", "Bread", "Cereal", "Rusk", "Maggie", "Ketchup", "Cocoa Powder", "Flour", "Vanilla Essence", "Whipped Cream", "Sugar", "Mayonnaise", "Oats", "Butter", "Yogurt", "Beverages", "Candy", "Dairy Milk", "Hair Oil", "Toothpaste", "Shampoo", "Bathing Soap", "Talcum Powder", "Deodorant", "Facewash", "Hand Sanitizer", "Vegetables", "Snacks", "Spices", "Cooking Oil", "Fruits"]

b=df.values.tolist()
#b=[]
d,max=0,0

guiout=StringVar()
guiout.set("")

def getitems():
    c=[0 for q in range(36)]
    initem=entry.get()
    if initem not in a:
        guiout.set("Item not available at the moment.")
        return 0
    out="We recommend:\n"
    for i in range(len(b)):
        if initem in b[i]:
            for k in b[i]:
                if k!=initem:
                    indexu=a.index(k)
                    c[indexu]+=1
    e=[]
    for q in range(len(c)):
        e.append(c[q])
    c.sort()
    templist=[]
    for i in range(len(c)-1,len(c)-4,-1):
                for j in range(len(e)):
                    if c[i]==e[j]:
                        if a[j] not in templist and len(templist)<4:
                            out+=a[j]+"\n"
                            templist.append(a[j])
                            break
    guiout.set(out)

Label(window, text="Enter the product: ").grid(row=0,column=0)
entry=Entry(window)
entry.grid(row=0,column=1)
Button(window, width = 5, height= 2, text="Search",command=getitems).grid(row=1,column=1)
Label(window,textvariable=guiout).grid(row=2,column=1)
window.mainloop()