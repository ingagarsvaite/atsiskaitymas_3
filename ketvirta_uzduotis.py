# Ketvirta užduotis - Tkinter
#
# Sukurti programą su TKinter. Programa turi turėti:
# Laukelį, į kurį įvedama temperatūrą
# Mygtuką, kurį paspaudus į laukelį įrašyta temperatūrą būtų konvertuojama iš farenheito į celsijų.
# Konvertuota temperatūra turi būti atvaizduota programoje kaip tekstas.
# Mygtuką, kurį paspaudus į laukelį įrašyta temperatūrą būtų konvertuojama iš celsijaus į farenhaitą.
# Konvertuota temperatūra turi būti atvaizduota programoje kaip tekstas.
# Tekstą, kuris atvaizduos temperatūros konvertavimo rezultatą

from tkinter import *
def c_i_f():
    ivesta = laukas.get()
    rezultatas = float(ivesta) * 1.8 + 32
    isspausdinam["text"] = f"{rezultatas} F"

def f_i_c():
    ivesta = laukas.get()
    rezultatas = (float(ivesta) - 32) * 5 / 9
    isspausdinam["text"] = f"{round(rezultatas, 2)} C"

langas = Tk()
langas.title("Mano langas")
langas.geometry("320x120")
uzrasas = Label(langas, text="Įveskite temperatūrą C arba F")
laukas = Entry(langas)

mygtukas1 = Button(langas, text="Celsius -> Fahrenheit", command = c_i_f)
mygtukas2 = Button(langas, text="Fahrenheit -> Celsius", command = f_i_c)
isspausdinam = Label(langas, text = "")
uzrasas.pack()
laukas.pack()
mygtukas1.pack()
mygtukas2.pack()
isspausdinam.pack()

mainloop()

