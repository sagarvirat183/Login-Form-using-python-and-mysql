from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox


root=Tk()
class Mainwindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1200x700+200+70")
        self.root.resizable(False, False)

# adding image to root window
        self.image=ImageTk.PhotoImage(file="html-color-codes-color-tutorials.jpg")
        self.label=Label(self.root, image=self.image)  #added image on label
        self.label.pack()


# CREATING HEADING FOR ROOT WINDOW
        self.lbel=Label(self.root, text="LOGIN SYSTEM",font=("times new roman",15,'bold'),bg='gold2')
        self.lbel.place(x=0,y=5,width=1200,height=100)



#creating  frame on root window
        self.frame=Frame(self.root)
        self.frame.place(x=390, y=170, width=400, height=450)


#creating labels and entrybox on frame
        self.userlabel = Label(self.frame, text="USER_ID", font=("Andalus", 15, 'bold'), bg='white', fg='gray')
        self.userlabel.place(x=80, y=50)

        self.entry1 = Entry(self.frame, font=("times new roman", 15))  #creating entry box
        self.entry1.place(x=80, y=100, width=250)

        self.passlabel = Label(self.frame, text="PASSWORD", font=("Andalus", 15 ,'bold'), bg='white', fg='gray')#password
        self.passlabel.place(x=80, y=150)

        self.entry2 = Entry(self.frame, show="*", font=("times new roman", 15))
        self.entry2.place(x=80, y=200, width=250)


        self.button = Button(self.frame, text='LOGIN', activebackground="#00B0F0", activeforeground='white', fg='gray',
                            bg="#F0F8FF", font=("Arial", 15, 'bold'), command=lambda: self.logindata())
        self.button.place(x=80, y=250, width=250)


#creating forget password button on Frame
        self.button1=Button(self.frame,text="Forget Password?",activebackground="blue",
                            command=lambda:self.fwindow(),font=("times new roman",13,'bold'),fg='black')
        self.button1.place(x=80,y=320)

#creating button and labels for forget password
    def fwindow(self):
        forgetwindow=Toplevel()
        self.forgetwindow=forgetwindow
        self.forgetwindow.title("Forget Password")
        self.forgetwindow.geometry("600x500+450+250")
        self.forgetwindow.resizable(False,False)

        self.userID=Label(self.forgetwindow,text="USER_ID",font=("times new roman",15,'bold'))
        self.userID.place(x=100,y=90)

        self.entry3=Entry(self.forgetwindow,font=("times new roman",15))
        self.entry3.place(x=100,y=140,width=250)

        self.userID = Label(self.forgetwindow, text="NEW PASSWORD", font=("times new roman", 15, 'bold'))
        self.userID.place(x=100, y=190)

        self.entry4 = Entry(self.forgetwindow, font=("times new roman", 15))
        self.entry4.place(x=100, y=240, width=250)

        self.userID = Label(self.forgetwindow, text="CONFIRM PASSWORD", font=("times new roman", 15, 'bold'))
        self.userID.place(x=100, y=290)

        self.entry5= Entry(self.forgetwindow, font=("times new roman", 15))
        self.entry5.place(x=100, y=340, width=250)



        self.chbutton=Button(self.forgetwindow,text="Change password",font=("times new roman",15,'bold')
                             ,bd=5,activebackground="green",command=lambda:self.chpass())
        self.chbutton.place(x=100,y=390,width=250)


#create database connectivity

    def logindata(self):
        con = pymysql.connect(host="localhost", user='root', password='root@123', db='sagar')

        #con=pymysql.connect('localhost' , 'root','root@123','sagar')

        cur = con.cursor()
        cur.execute("Select * from admin_data where User_ID=%s and Password=%s", (self.entry1.get(), self.entry2.get()))
        row = cur.fetchone()
        if row == None:
            messagebox.showerror("WARNING", "USER NOT FOUND")

        else:
            messagebox.showinfo("Success", "Login Succesfully")

# Working on forget window database
    def chpass(self):
        if self.entry3.get=="" and self.entry4.get()=="" and self.entry5.get=='':
            messagebox.showerror("Warning","All fields are required")

        else:
            con = pymysql.connect(host="localhost", user='root', password='root@123', db='sagar')
            cur=con.cursor()
            cur.execute("UPDATE admin_data set Password=%s WHERE User_ID=%s",(self.entry4.get(),self.entry3.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","PASSWORD CHANGED SUCCESSFULLY ")


main = Mainwindow(root)
root.mainloop()
