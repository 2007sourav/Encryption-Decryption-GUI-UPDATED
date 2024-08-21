import tkinter as tk
from tkinter import *
import os
import random as r
from tkinter import messagebox

#####################################################################################################################################

def userwarn():
    messagebox.showwarning("Warning","Make Sure To Start Key With Any Digit Other Than 0")


#####################################################################################################################################

def credits():                      #CREDITS SYSTEM
    messagebox.showinfo('Credits', 'This System Was Made By Sourav, Make Sure To Check Out :-\nGithub - @2007sourav\nTwitter/X - @2007sourav')
    root.destroy()

#####################################################################################################################################

def enbox():                       #UPDATE TEXT BOX
    messagebox.showinfo('Update', 'Text And Key Updated Successfully')

#####################################################################################################################################

def close_encrypt():                       #CLOSES ENCRYPTION BOX AFTER SUBMIT
    enwin.destroy()
    enbox()


#####################################################################################################################################

def decbox():                       #OPERATES DECRYPTION BOX
    dectext=f"Here Is The Decrypted Text Fetched From Data :- {h}"
    messagebox.showinfo("Decrypted Text",dectext)
def emptytext():
    messagebox.showerror("Empty File", "No Encrypted Text Found In Data")
def wrongkey():
    messagebox.showerror("Wrong Key", "Key Error : User Has Denied Access")
#####################################################################################################################################

def check():                       #CHECKS IF DIRECTORY IS PRESENT IN E DRIVE FOR STORING KEY
    if not os.path.isdir("E:\\Encryption-Key"):
        os.mkdir("E:\\Encryption-Key")

#####################################################################################################################################
 
def keypass(k):                       #ENCRYPTS KEY
    check()
    f=open("E:\\Encryption-Key\\key.txt", "w")
    z=''
    for i in str(k):
        ran=r.randint(0,9)
        z=z+i+str(ran)
    f.write(z)
    f.close()    

#####################################################################################################################################
def encrypt():                       #ENCRYPTION 
    f=open("D:\\pythonpro\\endec-updated-GUI\\encryptedfile.txt", "w")
    s=textval.get()
    
    final=''

    key=keyval.get()
    keypass(key)
   
    zigzag = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wd=s.split()
    for i in wd:
        final=final+''.join(r.choices(zigzag, k=3))+i[1:]+i[0]+''.join(r.choices(zigzag, k=3))+' '
    f.write(final)
    close_encrypt()
    f.close()
#####################################################################################################################################
h=None
def decrypt():                       #DECRYPTION 
    f=open("D:\\pythonpro\\endec-updated-GUI\\encryptedfile.txt", "r")
    r=f.read()
    f.close()
    key2=keyval2.get()
    fp=open("E:\\Encryption-Key\\key.txt", "r")
    g=fp.read()
    fp.close()
    nw=""
    if g=='':
        emptytext()
    else:
        nw=g[0::2]
        if key2==int(nw):
            final=''
            word=[]
            wd=r.split()
            for i in wd:
                final=i[3:-3]
                final=final[-1]+final[:-1]
                word.append(final)
            global h
            h=' '.join(word)
            decbox()
        else:
            wrongkey()
    fp.close()

#####################################################################################################################################
def exitsys():                      #EXITS SYSTEM
    credits()

#####################################################################################################################################
textval=None
keyval=None
def textencrypt():                       #ENCRYPTION GUI
    userwarn()
    global enwin
    enwin=tk.Toplevel()
    enwin.geometry("655x333")
    enwin.title("Text Encrypter")
    text1 = Label(enwin, text="Text")
    key1 = Label(enwin, text="Key")
    text1.grid()
    key1.grid(row=1)
    global textval
    global keyval
    textval = StringVar()
    keyval = IntVar()

    textentry = Entry(enwin, textvariable = textval)
    keyentry = Entry(enwin, textvariable = keyval)
    textentry.grid(row=0, column=1)
    keyentry.grid(row=1, column=1)

    Button(enwin,text="Submit",command=encrypt).grid()
    enwin.mainloop()


#####################################################################################################################################
global keyval2
def textdecrypt():                       #DECRYPTION GUI
    global decwin
    decwin=tk.Toplevel()
    decwin.geometry("655x333")
    decwin.title("Text Decrypter")
    key2 = Label(decwin, text="Key")
    key2.grid()


    global keyval2
    keyval2 = IntVar()

    keyentry = Entry(decwin, textvariable = keyval2)
    keyentry.grid(row=0, column=1)

    Button(decwin,text="Submit",command=decrypt).grid()
    decwin.mainloop()



#####################################################################################################################################
#####################################################################################################################################

                                                #GUI BODY

root=tk.Tk()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry(f"{sw}x{sh}+0+0")
root.title("Text Encrypter")
#####################################################################################################################################
f1=Frame(root, bg='#96E6B3', borderwidth=5, relief=SUNKEN)
f1.pack(fill=X)
te=PhotoImage(file="D:\\pythonpro\\endec-updated-GUI\\logo.png")
tcl=Label(f1,image=te,bg="#96E6B3")
tcl.pack()
#####################################################################################################################################
f2=Frame(root, bg='#96E6B3', borderwidth=5, relief=SUNKEN)
f2.pack(side=LEFT,anchor="nw")
en=Button(f2, text='Enrcypt Text', command=textencrypt, bg='#F1FFFA',fg='#464E47',pady=59, padx=40, font=('comicsansms',30,'bold'))
en.pack()
dn=Button(f2, text='Decrypt Text',command=textdecrypt, bg='#F1FFFA',fg='#464E47',pady=50, padx=40, font=('comicsansms',30,'bold'))
dn.pack()
ex=Button(f2, text='Exit Encrypter',command=exitsys , bg='grey',fg='red',pady=50, padx=25, font=('comicsansms',30,'bold'))
ex.pack()
#####################################################################################################################################
fe = Frame(root, borderwidth=6, bg="#C4DEC4", relief=SUNKEN)
fe.pack(side=TOP, fill="x")
eth = Label(fe, text="Encrypter :- :-", font="Helvetica 22 bold underline", fg="black", bg="#C4DEC4")
eth.pack()
et = Label(fe, text="Text Encrypter -:\nIt converts your given text\nto set of text which is not\nunderstandable easily and can only\nbe decrypted through a \nspecific KEY", font="Helvetica 16 bold", fg="#464E47", bg="#C4DEC4")
et.pack()
#####################################################################################################################################
fd = Frame(root, borderwidth=6, bg="#C4DEC4", relief=SUNKEN,pady=0)
fd.pack(side=TOP, fill="x")
edh = Label(fd, text="Decrypter :-", font="Helvetica 22 bold underline", fg="black", bg="#C4DEC4")
edh.pack()
ed = Label(fd, text="Text Decrypter\n It takes up the text\nprovided in the encrypted file\nand decrypts it\nmaking it human readable", font="Helvetica 16 bold", fg="#464E47", bg="#C4DEC4")
ed.pack()
#####################################################################################################################################
fx = Frame(root, borderwidth=6, bg="#C4DEC4", relief=SUNKEN,pady=51)
fx.pack(side=TOP, fill="x")
exh = Label(fx, text="Exit :-", font="Helvetica 22 bold underline", fg="black", bg="#C4DEC4")
exh.pack()
ext = Label(fx, text="Exits the encrypter", font="Helvetica 16 bold", fg="#464E47", bg="#C4DEC4")
ext.pack()
#####################################################################################################################################
fc=Frame(root,borderwidth=6,bg='#232923',relief=SUNKEN)
fc.pack(side=LEFT,padx=220,fill=Y)
fci=PhotoImage(file="D:\\pythonpro\\endec-updated-GUI\\sourav.png")
fcl=Label(fc,image=fci,bg="#232923")
fcl.pack()
#####################################################################################################################################
root.mainloop()
