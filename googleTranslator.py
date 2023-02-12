from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text="type", src="English", dest="Marathi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans11 = trans.translate(text=text1, dest= dest1)
    return trans11.text
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_text.get(1.0, END)
    textGet = change(text = masg, src = s, dest = d)
    dest_text.delete(1.0, END)
    dest_text.insert(END, textGet)





root = Tk()
root.title("Google Translator")
root.geometry("500x700")
root.config(bg="Red")

leb_1 = Label(root,text = "Translator", font= ("Time New Roman", 30, "bold"))
leb_1.place(x=100, y= 40, height=50, width = 300)


frame = Frame(root).pack(side=BOTTOM)

leb_1 = Label(root,text = "Source Text", font= ("Time New Roman", 20, "bold"), fg = "Black", bg = "Red")
leb_1.place(x=100, y= 100, height=20, width = 300)

sor_text = Text(frame,font = ("Time New Roman", 20, "bold"), wrap= WORD)
sor_text.place(x=10, y=120, height=150, width = 480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value= list_text)
comb_sor.place(x=10, y=300, height=40, width = 150)
comb_sor.set("English")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)#relief & raised give the 3d veiw
button_change.place(x=170, y=300, height=40, width = 150)

comb_dest = ttk.Combobox(frame, value= list_text)
comb_dest.place(x=330, y=300, height=40, width = 150)
comb_dest.set("English")

leb_1 = Label(root,text = "Destination Text", font= ("Time New Roman", 20, "bold"), fg = "Black", bg = "Red")
leb_1.place(x=100, y= 360, height=20, width = 300)

dest_text = Text(frame,font = ("Time New Roman", 20, "bold"), wrap= WORD)
dest_text.place(x=10, y=400, height=150, width = 480)


root.mainloop()