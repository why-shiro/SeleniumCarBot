import tkinter

from chrome import SearchAgent
from tkinter import *

gui = Tk()
gui.title("Autopark-Nord GmbH Bot Control")
gui.geometry("1000x550")
gui.resizable(False, False)


def show():
    label.config(text=clicked.get())


#
# Start of Kraftstoffart grid
#

label = tkinter.Label(gui, text="Kraftstoffart", font=('Helvetica', 10, 'bold'))
label.place(x=10, y=10)

c1 = tkinter.Checkbutton(gui, text="Diesel", onvalue=1, offvalue=0)
c1.place(x=10, y=30)

c2 = tkinter.Checkbutton(gui, text="Benzin", onvalue=1, offvalue=0)
c2.place(x=10, y=50)

c3 = tkinter.Checkbutton(gui, text="Hybrid (Benzin/Elektro)", onvalue=1, offvalue=0)
c3.place(x=10, y=70)

c4 = tkinter.Checkbutton(gui, text="Hybrid (Diesel/Elektro)", onvalue=1, offvalue=0)
c4.place(x=10, y=90)

c5 = tkinter.Checkbutton(gui, text="Elektro", onvalue=1, offvalue=0)
c5.place(x=10, y=110)

c6 = tkinter.Checkbutton(gui, text="Autogas (LPG)", onvalue=1, offvalue=0)
c6.place(x=10, y=130)

c7 = tkinter.Checkbutton(gui, text="Erdgas (CNG)", onvalue=1, offvalue=0)
c7.place(x=10, y=150)

c8 = tkinter.Checkbutton(gui, text="Wasserstoff", onvalue=1, offvalue=0)
c8.place(x=10, y=170)

#
# Start of Getriebe grid
#

label2 = tkinter.Label(gui, text="Getriebe", font=('Helvetica', 10, 'bold'))
label2.place(x=10, y=200)

g1 = tkinter.Checkbutton(gui, text="Automatik", onvalue=1, offvalue=0)
g1.place(x=10, y=220)

g1 = tkinter.Checkbutton(gui, text="Halbautomatik", onvalue=1, offvalue=0)
g1.place(x=10, y=240)

g1 = tkinter.Checkbutton(gui, text="Schaltgetriebe", onvalue=1, offvalue=0)
g1.place(x=10, y=260)

options = [
    "Beliebig",
    "Abarth",
    "AC",
    "Acura",
    "Aiways",
    "Alfa Romeo",
    "ALPINA",
    "Artega",
    "Asia Motors",
    "Aston Martin",
    "Audi",
    "Austin",
    "Austin Healey",
    "BAIC",
    "Bentley",
    "BMW",
    "Borgward",
    "Brilliance",
    "Bugatti",
    "Buick",
    "Cadillac",
    "Casalini",
    "Caterham",
    "Chatenet",
    "Chevrolet",
    "Chrysler",
    "Citroën",
    "Cobra",
    "Cupra",
    "Dacia",
    "Daewoo",
    "Daihatsu",
    "DeTomaso",
    "DFSK",
    "Dodge",
    "Donkervoort",
    "DS Automobiles",
    "e.GO",
    "Elaris",
    "Ferrari",
    "Fiat",
    "Fisker",
    "Ford",
    "GAC Gonow",
    "Gemballa",
    "Genesis",
    "GMC",
    "Grecav",
    "Hamann",
    "Holden",
    "Honda",
    "Hummer",
    "Hyundai",
    "Infiniti",
    "Iveco",
    "Jaguar",
    "Jeep",
    "Kia",
    "Koenigsegg",
    "KTM",
    "Lada",
    "Lamborghini",
    "Land Rover",
    "Landwind",
    "LEVC",
    "Lexus",
    "Ligier",
    "Lincoln",
    "Lotus",
    "Lynk & Co",
    "Mahindra",
    "Maserati",
    "Maybach",
    "Mazda",
    "McLaren",
    "Mercedes-Benz",
    "MG",
    "Microcar",
    "MINI",
    "Mitsubishi",
    "Morgan",
    "Nissan",
    "NSU",
    "Oldsmobile",
    "Opel",
    "Pagani",
    "Peugeot",
    "Piaggio",
    "Plymouth",
    "Polestar",
    "Pontiac",
    "Porsche",
    "Proton",
    "Renault",
    "Rolls-Royce",
    "Rover",
    "Ruf",
    "Saab",
    "Santana",
    "Seat",
    "Skoda",
    "Smart",
    "speedART",
    "Spyker",
    "Ssangyong",
    "Subaru",
    "Suzuki",
    "Talbot",
    "Tata",
    "TECHART",
    "Tesla",
    "Toyota",
    "Trabant",
    "Triumph",
    "TVR",
    "Volkswagen",
    "Volvo",
    "Wartburg",
    "Westfield",
    "Wiesmann",
    "Andere"

]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Monday")

drop = OptionMenu(gui, clicked, *options)
drop.pack()

# Create button, it will change label text
button = Button(gui, text="click Me", command=show)
button.pack()

# Create Label
label = Label(gui, text=" ")
label.pack()

gui.mainloop()

"""sa = SearchAgent("https://suchen.mobile.de/fahrzeuge/search.html?dam=0&isSearchRequest=true&ms=%3B9%3B%3B%3B&ref=srp&refId=a8c7b255-3940-40e5-2663-235341e768fe&s=Car&sb=rel&st=FSBO&vc=Car")

sa.sendMails()"""
