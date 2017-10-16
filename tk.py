import sqlite3
from tkinter import *
from sqliteQuerys import countToday
janela = Tk()




data = 0

lb = Label(janela, text=data)
janela.mainloop()
while True:
    lb["text"] = countToday()
    lb.pack()



 

   



