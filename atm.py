from tkinter import *
from tkinter import messagebox

pinname = {}
nameamount = {}

h = Tk()
h.title("Bank Service")
h.geometry("655x655")
h.maxsize(width=650, height=650)
h.minsize(width=600, height=600)


# this is the new window for registration
def Tj():
    top = Toplevel()
    top.maxsize(width=650, height=650)
    top.minsize(width=640, height=600)
    head = Label(top, text="Welcome to REGISTRATION FORM ", bg="green", fg="white", font=("", 26)).pack()

    def submit():
        if en.get() == "" or en2.get() == "":
            messagebox.showwarning("warning", "Blank Invalid")
        else:
            v = en.get()
            g = int(v)  # print(g)
            v2 = en2.get()
            g2 = str(v2)  # print(g2)
            pinname[g] = g2
            print(pinname)
            if pinname == "":
                messagebox.showwarning("warning", "Not filled properly")
            else:
                ko = messagebox.showwarning("info", "congratulation you register")
                if ko == True:
                    print("hello")
                else:
                    top.destroy()

    # enter input pin
    en = Entry(top, bd=2)
    en.place(x=160, y=150)
    pin = Label(top, text="Enter your PIN:-")
    pin.place(x=20, y=150)
    en2 = Entry(top, bd=2)
    en2.place(x=160, y=200)
    pin = Label(top, text="Enter your Name:-")
    pin.place(x=6, y=200)
    su = Button(top, text="SUBMIT", fg="green", command=submit)
    su.place(x=9, y=240)


# this is the header
te = Frame(h)
te.pack(side=TOP)
Label(te, text="Welcome to the Service ATM", fg="white", font=("arial", 33), bg="blue").pack()
# this is the end of the header

# this is the entery means input
en = Frame(h)
en.pack()
war = StringVar()
en = Entry(en, bg="white", fg="black", bd=6, width=20, textvariable=war).pack()
# this is the end of the entry
bt = Button(text="Register your self", bd=5, command=Tj)
bt.place(x=20, y=110)


# cash deposite function
def depo():
    top2 = Toplevel()
    top2.maxsize(width=650, height=650)
    top2.minsize(width=640, height=600)
    head = Label(top2, text="Welcome to CASH DEPOSITE", bg="orange", fg="white", font=("", 26)).pack()
    # cash deposite

    # this is the button
    ent5 = Entry(top2, bd=2)
    ent5.place(x=160, y=150)

    # cash deposite and submit
    def amou():
        if len(pinname) < 1:
            messagebox.showwarning("warning", "Register your Self")
        else:
            v = ent5.get()
            do = int(v)
            for i in pinname:
                if i == do:
                    k = entvalue.get()
                    fo = int(k)
                    print(fo)
                    textho.config(text="Welcome back Mr/Mrs:=" + pinname.get(i) + "\nthanks for deposite money:-" + k)
                    nameamount[pinname.get(i)] = fo
                    print(nameamount)
                    lp = messagebox.showindo("sucessfully", "Money deposite sucessfully")
                    if lp == True:
                        print("yes")
                    else:
                        top2.destroy()

                else:
                    messagebox.showwarning("warning", "you are not customer")
                    top2.destroy()

    pinvalue = Label(top2, text="Enter the PIN:-")
    pinvalue.place(x=20, y=150)
    # enter input2 name
    entvalue = Entry(top2, bd=2)
    entvalue.place(x=160, y=200)
    pin = Label(top2, text="Enter the Amount:-")
    pin.place(x=6, y=200)
    su = Button(top2, text="SUBMIT", fg="green", command=amou)
    su.place(x=9, y=240)
    # show info
    textho = Label(top2, fg="green")
    textho.place(x=170, y=400)


bt = Button(text="Cash Deposite", bd=5, command=depo)
bt.place(x=450, y=110)


# this the function of cash withdrwal
def cash():
    top3 = Toplevel()
    top3.maxsize(width=650, height=650)
    top3.minsize(width=640, height=600)
    head = Label(top3, text="Welcome to CASH WITHDRAWAL", bg="purple", fg="white", font=("", 26)).pack()
    # cash withdrawal

    # this is the button
    ent6 = Entry(top3, bd=2)
    ent6.place(x=160, y=150)

    # inside the function
    def submitwith():
        if len(nameamount) < 1:
            messagebox.showwarning("warning", "Deposite money")
        else:
            vp = ent6.get()
            dos = int(vp)
            for i in pinname:
                if i == dos:
                    ky = entvalue1.get()
                    so = int(ky)
                    print(so, type(so))

                    textho2.config(text="Welcome back Mr/Mrs:=" + pinname.get(
                        i) + "\nthanks for using bank Service\n withdrawal amount:-" + ky)
                    for i in nameamount:
                        width = nameamount.get(i) - so
                        nameamount[i] = width
                        print(nameamount)
                    lp = messagebox.showinfo("sucessfully", "money Withdrawal sucessfully")
                    if lp == True:
                        print("yes")
                    else:
                        top3.destroy()

    pinvalue1 = Label(top3, text="Enter the PIN:-")
    pinvalue1.place(x=20, y=150)
    # enter input2 name
    entvalue1 = Entry(top3, bd=2)
    entvalue1.place(x=230, y=200)
    pin2 = Label(top3, text="Enter the Withdrawal Amount:-")
    pin2.place(x=9, y=200)
    su1 = Button(top3, text="SUBMIT", fg="green", command=submitwith)
    su1.place(x=9, y=240)
    # show info
    textho2 = Label(top3, fg="green")
    textho2.place(x=170, y=400)


bt = Button(text="Cash Withdrawal", bd=5, command=cash)
bt.place(x=20, y=160)


# this is the balance check command
def checkb():
    top4 = Toplevel()
    top4.maxsize(width=650, height=650)
    top4.minsize(width=640, height=600)
    head2 = Label(top4, text="Welcome to Balance Check Service", bg="pink", fg="white", font=("", 26)).pack()
    # cash withdrawal

    # this is the button
    ent7 = Entry(top4, bd=2)
    ent7.place(x=160, y=150)

    # inside the function
    def click():
        if len(nameamount) < 1:
            messagebox.showwarning("warning", "Deposite money")
        else:
            vpo = ent7.get()
            dosh = int(vpo)
            for i in pinname:
                if i == dosh:
                    for k in nameamount:
                        h = nameamount.get(k)
                        ho = str(h)
                        print(type(ho), ho)

                    textho3.config(text="Welcome back Mr/Mrs:=" + pinname.get(
                        i) + "\nthanks for using bank Service\n Cash amount:-" + ho + "Rupees")

    pinvalue2 = Label(top4, text="Enter the PIN:-")
    pinvalue2.place(x=20, y=150)
    # enter input2 name
    # entvalue2 = Entry(top4, bd=2)
    # entvalue2.place(x=230, y=200)
    # pin3=Label(top4, text="Enter the Withdrawal Amount:-")
    # pin3.place(x=9,y=200)
    su1 = Button(top4, text="SUBMIT", fg="green", command=click)
    su1.place(x=9, y=240)
    # show info
    textho5 = Label(top4, fg="green")
    textho5.place(x=170, y=400)
    # show info
    textho3 = Label(top4, fg="green")
    textho3.place(x=170, y=400)


bt = Button(text="Cash Balance", bd=5, command=checkb)
bt.place(x=450, y=160)


# this is the function
def ex():
    y = messagebox.askyesno("exit", "Do you want to exit ?")
    if y == True:
        h.destroy()
    else:
        print("no")


exit = Button(text="EXIT", bd=1, fg="red", command=ex)
exit.place(x=20, y=500)
# this is the buttom part
bu = Frame(h)
bu.pack(side=BOTTOM)
Label(bu, text="Made by Trilok nath jha.....").pack()
h.mainloop()

