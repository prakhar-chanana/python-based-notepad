from tkinter import *
from tkinter import scrolledtext as skt
from tkinter import messagebox as msb

c = ''
d = ''
a = r''
xx = r''


def opn(*event):
    global a
    a = r'{}'.format(path.get())
    try:
        if a != '':
            file = open(a)
            rd()
            t1.delete('1.0', END)
            inst()
            convrtD()
        else:
            msb.showwarning('Warning', 'File Path Empty!')
            return
    except FileNotFoundError:
        msb.showwarning("File Not Found!", "File Fot Found!")
    except Exception as e:
        print("Error : ", e)
    else:
        try:
            pass
        finally:
            file.close()


def rd():
    global c
    f = open(a)
    cc = f.read()
    c = cc
    f.close()


def inst():
    global c
    for x in c:
        t1.insert(END, x)


def convrtD():
    global d
    d = t1.get('1.0', END)
    ef = list(d)
    del ef[-1]
    ex = ''
    for p in ef:
        ex += p
    d = ex


def crtTT():
    def crtNew():
        convrtD()
        xx = r'{}'.format(nnn.get())
        try:
            file = open(xx)
            msb.showwarning('Warning', 'File Already Exists')
        except FileNotFoundError:
            file = open(xx, 'w')
            file.write(d)
            file.close()
            msb.showinfo('New File Created', 'New File Created: {}'.format(nnn.get()))
            path.set(xx)
            t1.delete('1.0', END)
            opn()
            tt.destroy()
        except Exception as e:
            print("Error : ", e)
        else:
            try:
                pass
            finally:
                file.close()

    global a, xx, d
    tt = Toplevel()
    tt.title('Save As')
    nnn = StringVar()
    nnn.set('')
    lo = Label(tt, text='Enter New File Name: ', font=('arial', 10))
    lo.grid(row=0)
    le = Entry(tt, textvariable=nnn, font=('arial', 10), width='30')
    le.grid(row=0, column=1)
    lo1 = Label(tt, text='  ', font=('arial', 10))
    lo1.grid(row=1, columnspan=2)
    lb = Button(tt, text='Save As', font=('arial', 10), command=crtNew)
    lb.grid(row=2, columnspan=2)
    tt.mainloop()


def clr():
    global c, d
    t1.delete('1.0', END)
    path.set('')
    c = ''
    d = ''


def save():
    global c, d, xx
    convrtD()
    if path.get() != '':
        f = open(path.get(), 'w')
        f.write(d)
        f.close()
        msb.showinfo('Save', 'File Saved Successfully!!')
    elif path.get() == '':
        crtTT()


r = Tk()
r.geometry('900x556')
r.maxsize(900, 556)
r.title('Text Editor')

pw1 = PanedWindow(orient=HORIZONTAL)
pw1.pack(fill=X)

pw2 = PanedWindow(orient=HORIZONTAL)
pw2.pack()

pw3 = PanedWindow(orient=HORIZONTAL)
pw3.pack(fill=X)

path = StringVar()
path.set('')

l5 = Label(pw1, text='Enter File Path:', font=('arial', 10), width='20')
pw1.add(l5)
e1 = Entry(pw1, textvariable=path, font=('arial', 12), width='60', bd=5)
e1.bind('<Return>', opn)
pw1.add(e1)
l1 = Label(pw1, text='   ', font=('arial black', 20), width='2')
pw1.add(l1)
b1 = Button(pw1, text='Open', font=('arial', 10), width='15', command=opn)
pw1.add(b1)
l4 = Label(pw1, text=' ', font=('arial black', 20))
pw1.add(l4)

t1 = skt.ScrolledText(pw2, wrap=WORD, height=20, font=('arial', 15))
t1.pack(fill=BOTH)
pw2.add(t1)

l6 = Label(pw3, text='         ', font=('arial black', 20), width='9')
pw3.add(l6)
b2 = Button(pw3, text='Clear/New', font=('arial', 10), width='20', command=clr)
pw3.add(b2)
l2 = Label(pw3, text='                     ', font=('arial black', 20))
pw3.add(l2)
b3 = Button(pw3, text='Save/Save As', font=('arial', 10), width='20', command=save)
pw3.add(b3)
l3 = Label(pw3, text='                    ', font=('arial black', 20))
pw3.add(l3)

pw1.mainloop()
pw2.mainloop()
pw3.mainloop()
r.mainloop()
