import tkinter as tk
from tkinter import ttk

#variables
total = 0

order = []

coffeePrice = {
    'Espresso': 2.5,
    'Americano': 3.0,
    'Latte': 2.5,
    'Cappuchino': 3.0,
    'Macchiato': 2.5,
    'Mocha': 3.5,
    'Flat White': 2.5,
}

sizePrice = {
    'Medium' : 0,
    'Large' : 1.0,
    'XL' : 1.5
}

locationPrice = {
    "In" : 0,
    "Out" : 1
}



#functions
def addTotal(amount=0):
    global total
    total += amount
    totalVar.set(total)

def addOrder(coffee,price,place):
    global order
    order.append([checkCoffee.get(), checkSize.get(), checkPlace.get()])
    print(order)

def clearOrder():
    global order
    order = []
    print(order)



# window
window = tk.Tk()
window.title("Cafe Order System")
window.geometry("600x300")

#Dynamic var for labels in tk
totalVar = tk.IntVar()
checkCoffee = tk.StringVar(value=0)
checkSize = tk.StringVar(value=0)
checkPlace = tk.StringVar(value=0)

# titlescreen
titleLabel = ttk.Label(master=window, text="Coffee", font='Calibri 30 bold')
titleLabel.pack()

#Options
coffeeFrame = ttk.Frame(master=window)
for item in coffeePrice:
    button = ttk.Checkbutton(master=coffeeFrame , text=item, onvalue=item , offvalue=0, variable=checkCoffee)
    button.pack(side=tk.TOP, expand=True)


sizeFrame = ttk.Frame(master=window) 
for item in sizePrice:
    button = ttk.Checkbutton(master=sizeFrame , text=item, onvalue=item , offvalue=0, variable=checkSize)
    button.pack(side=tk.TOP, expand=True)

placeFrame = ttk.Frame(master=window) 
for item in locationPrice:
    button = ttk.Checkbutton(master=placeFrame , text=item, onvalue=item , offvalue=0, variable=checkPlace)
    button.pack(side=tk.TOP, expand=True)

currentTotal = ttk.Label(master=coffeeFrame, text=f'TOTAL : {total}' , font='Calibri 30 bold', textvariable=totalVar)
currentTotal.pack()

coffeeFrame.pack(side='left',expand=True)
sizeFrame.pack(side='left', expand=True)
placeFrame.pack(side='left', expand=True)

#Add to order
button = ttk.Button(master=window, text="ADD", command=lambda : addOrder(checkCoffee, checkPlace, checkSize))
button.pack(side='bottom',expand=False)

button = ttk.Button(master=window, text="CLEAR", command=lambda : clearOrder())
button.pack(side='bottom',expand=False)


# mainloop
window.mainloop()

