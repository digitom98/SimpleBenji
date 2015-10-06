from tkinter import *


# Window configuration :

myWindows = Tk()
myWindows.configure(background='black')
myWindows.wm_title("Benji : Assistant Personnel")
myFrame = Frame(myWindows, bg="black")
myFrame.pack()
myWindows.geometry('{}x{}'.format(600, 400))


##############################################################


# text analysis :
def submitTxt(event):
    print(textbox.get())

    if "salut" in textbox.get() or "bonjour" in textbox.get() or "hey" in textbox.get():
        answer.configure(text="Bonjour !")
        print("Bonjour !")
    else:
        print("Desole, je n'ai pas compris...")

    textbox.delete(0, END)


###################################################################


# TextBox / Label Config :
answer = Label(myFrame, text="Que puis-je pour vous ?", fg='DeepSkyBlue', bg='black', font="Calibri 14", justify=CENTER,
               wraplength=500)
answer.pack(side=BOTTOM)
textbox = Entry(myWindows, width=18, font="Calibri 14", bg="DeepSkyBlue3", fg="gray14")
textbox.pack(side=BOTTOM, fill=X, ipady=10)
textbox.focus_force()

textbox.bind("<Return>", submitTxt)

#######################################################################


myWindows.mainloop()  # Don't close the Window !
