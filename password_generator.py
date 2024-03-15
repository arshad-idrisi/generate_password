from tkinter import *
import random
import string


def exit():
    root.destroy()


def gene():
    # ent1.configure(state=NORMAL)
    # ent2.configure(state=NORMAL)
    # ent3.configure(state=NORMAL)
    # ent4.configure(state=NORMAL)

    if ent1.get()=="":
        message5.config(text="Empty Fname")
    elif ent2.get()=="":
        message5.config(text="Empty Lname")
    elif ent3.get()=="":
        message5.config(text="Empty Email")
    elif ent1.get()==ent3.get()=="":
        message5.config("")
    elif ent1.get()==ent2=="":
        message5.config("")
    elif ent2.get()==ent3.get()=="":
        message5.config("")
    else:
        ent1.get()!=""+ent2.get()!=""+ent3.get()!=""
        ent4.config(text="")
        length=8
        btn = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        ent4.delete(0, END)
        ent4.insert(END, btn)

    # ent1.configure(state=DISABLED)
    # ent2.configure(state=DISABLED)
    # ent3.configure(state=DISABLED)
    # ent4.configure(state=DISABLED)

root = Tk()
root.geometry("500x500")
root.minsize(500, 500)
root.maxsize(500, 500)
root.title("Password Generator!!")

lbl = Label(root, text="Password Generator.", bg="yellow", fg="red", bd="4", font="arial 19 bold", relief="raised")
lbl.pack(pady=5)

lbl1 = Label(root, text="Fname :", fg="blue", font="comicsansms, 10 bold")
lbl2 = Label(root, text="Lname :", fg="blue", font="comicsansms, 10 bold")
lbl3 = Label(root, text="Email_Id :", fg="blue", font="comicsansms, 10 bold")
message5 = Label(root, text="", font="aial 12 bold", fg="red")
bottom = Label(root, text="✨✨...Star Code with Arshad...👑👑", bg="aqua", fg="red", font="comicsansms, 15 bold", bd="4", relief="raised")
bottom.pack(side=BOTTOM)


btn = Button(root, text="Gen-Pass", bg="lightgreen",font="arial 12 bold", command=gene)
btn2 = Button(root, text="Exit", bg="lightgreen",font="arial 12 bold", command=exit)
btn.place(x=150, y=290)
btn2.place(x=280, y=290)

ent1 = Entry(root, font="comicsansms, 10 bold", fg="green")
ent2 = Entry(root, font="comicsansms, 10 bold", fg="green")
ent3 = Entry(root, font="comicsansms, 10 bold", fg="green")
ent4 = Entry(root, font="comicsansms, 10 bold", fg="red")


lbl1.place(x=70, y=80)
ent1.place(x=130, y=80)

lbl2.place(x=70, y=120)
ent2.place(x=130, y=120)

lbl3.place(x=70, y=160)
ent3.place(x=140, y=160)

ent4.place(x=150, y=250)

message5.place(x=170, y=350)

root.mainloop()

