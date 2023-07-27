from tkinter import*
from tkinter import font
from PIL import Image, ImageTk, ImageDraw
from tkinter import ttk, messagebox

from math import *
# import pymysql
import sqlite3
from tkinter import messagebox
import os


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="SystemHighlight")

        # # ==========Frames========

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=(
            "Baloo Bhai 2", 30, "bold"), bg="white", fg="darkgreen").place(x=250, y=50)

        email = Label(login_frame, text="EMAIL ADDRESS", font=(
            "Baloo Bhai 2", 18, "bold"), bg="white", fg="purple").place(x=250, y=150)
        self.txt_email = Entry(login_frame,  font=(
            "Baloo Bhai 2", 15), bg="aliceblue")
        self.txt_email.place(x=250, y=180, width=350, height=25)

        pass_ = Label(login_frame, text="PASSWORD", font=(
            "Baloo Bhai 2", 18, "bold"), bg="white", fg="purple").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=(
            "Baloo Bhai 2", 15), bg="aliceblue", show="*")
        self.txt_pass_.place(x=250, y=280, width=350, height=25)

        btn_reg = Button(login_frame, cursor="hand2", command=self.register_window, text="Register New Account?", font=(
            "Baloo Bhai 2", 12), bg="white", bd=0, fg="crimson").place(x=250, y=320)
        btn_forget = Button(login_frame, cursor="hand2", command=self.forget_password_window, text="Forget Password?", font=(
            "Baloo Bhai 2", 12), bg="white", bd=0, fg="crimson").place(x=450, y=320)

        btn_login = Button(login_frame, text="Login", command=self.login, font=(
            "Baloo Bhai 2", 20, "bold"), fg="black", bg="lightseagreen", cursor="hand2").place(x=250, y=380, width=180, height=40)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_pass_.delete(0, END)

    def forget_password(self):
        if self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_pass.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root2)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",
                            (self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please Select the Correct Security Question / Enter Answer", parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",
                                (self.txt_new_pass.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Sucess", "Your password has been reset,Please login with new password", parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to: {str(es)}", parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror(
                "Error", "Please enter the email address to reset your password", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?",
                            (self.txt_email.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please enter the valid email address to reset your password", parent=self.root)

                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forget Password", font=(
                        "Baloo Bhai 2", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)

                    question = Label(self.root2, text="Security Question", font=(
                        "Baloo Bhai 2", 15, "bold"), bg="white", fg="purple").place(x=50, y=100)
                    self.cmb_quest = ttk.Combobox(self.root2, font=(
                        "Baloo Bhai 2", 13), state='readonly', justify=CENTER)
                    self.cmb_quest['values'] = (
                        "Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend's name")
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(self.root2, text="Answer", font=(
                        "Baloo Bhai 2", 15, "bold"), bg="white", fg="purple").place(x=50, y=180)
                    self.txt_answer = Entry(self.root2, font=(
                        "Baloo Bhai 2", 15), bg="aliceblue")
                    self.txt_answer.place(x=50, y=210, width=250)

                    new_password = Label(self.root2, text="New Password", font=(
                        "Baloo Bhai 2", 15, "bold"), bg="white", fg="purple").place(x=50, y=260)
                    self.txt_new_pass = Entry(self.root2, font=(
                        "Baloo Bhai 2", 15), bg="aliceblue", show="*")
                    self.txt_new_pass.place(x=50, y=290, width=250)

                    btn_change_password = Button(self.root2, text="Reset Password", command=self.forget_password, bg="green", fg="white", font=(
                        "Baloo Bhai 2", 15, "bold"), cursor="hand2").place(x=90, y=340)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to: {str(es)}", parent=self.root)

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and password=?",
                            (self.txt_email.get(), self.txt_pass_.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Email Address or Password ", parent=self.root)

                else:
                    messagebox.showinfo(
                        "Success", f"Welcome: {self.txt_email.get()}", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to: {str(es)}", parent=self.root)


root = Tk()
obj = login_window(root)
root.mainloop()
