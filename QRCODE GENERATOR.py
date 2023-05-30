import qrcode
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

QRCODE_GENERATOR = tk.Tk()
QRCODE_GENERATOR.title("QRCODE GENERATOR")
QRCODE_GENERATOR.minsize(500,400)
QRCODE_GENERATOR.maxsize(500,400)

def MAKE_QR_CODE():
    data =  QRCODE_GET_AREA.get("1.0","end-1c")
    QRCODE_SYMBOL = qrcode.make(data)
    data2 = filedialog.asksaveasfilename()
    if data2 is None:
        return data2

    if data2 == "":
        return 0
    
    QRCODE_SYMBOL.save(str(data2)+".png")
    msg = Tk()
    msg.withdraw()
    messagebox.showinfo("İMFORMATİON","YOUR QR CODE SAVED SUCCESFULLY\n"+str(data2))

QRCODE_İNFO_AREA = tk.Label(QRCODE_GENERATOR,text = "PLEASE ENTER THE DESIRED DATA AND CLICK THE BUTTON.",fg = "salmon",bg = "black",font = "Arial 13")
QRCODE_İNFO_AREA.place(width = 500,height = 50,x = 0,y = 0)

QRCODE_GET_AREA = tk.Text(QRCODE_GENERATOR,fg = "black",bg = "white",font = "Arial 20")
QRCODE_GET_AREA.place(width = 500,height = 250,x = 0,y = 50)

QRCODE_TRANSLATE_BUTTON = tk.Button(QRCODE_GENERATOR,text = "MAKE QR CODE",fg = "lime",bg = "black",activebackground = "black",activeforeground = "lime",font = "Arial 35",command = MAKE_QR_CODE)
QRCODE_TRANSLATE_BUTTON.place(width = 500,height = 100,x = 0,y = 300)

QRCODE_GENERATOR.mainloop()
