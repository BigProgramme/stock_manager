import os
import tkinter as tk
import sqlite3
from tkinter import messagebox


# Authentification:
class Login:
    def __init__(self, master):
        self.master = master
        self.login_frame = tk.Frame(master)
        self.login_frame.pack(pady=100)
        self.login_frame.config(bg="#B0E0E6", width=200, height=100)

        self.username_label = tk.Label(self.login_frame, text="Username*: ", font=("Consolas", 14), fg="blue",
                                       bg="#000080")
        self.username_label.config(bg="#B0E0E6")

        self.password_label = tk.Label(self.login_frame, text="Password*: ", font=("Consolas", 14), fg="blue",
                                       bg="#000080")
        self.password_label.config(bg="#B0E0E6")

        self.username_entry = tk.Entry(self.login_frame, font=("Consolas", 14), bg="#7aa600")
        self.password_entry = tk.Entry(self.login_frame, font=("Consolas", 14), show="*", bg="#7aa600")

        self.username_label.grid(row=0, column=0, sticky="E", padx=15, pady=15)
        self.username_entry.grid(row=0, column=1, padx=15, pady=15)
        self.password_label.grid(row=1, column=0, sticky="E", padx=15, pady=15)
        self.password_entry.grid(row=1, column=1, padx=15, pady=15)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1)

        self.sign_button = tk.Button(self.login_frame, text="Sign up", command=self.sign)
        self.sign_button.grid(row=5, column=1)

        self.ask_label = tk.Label(self.login_frame, text="Not yet registered? ", bg="#B0E0E6")
        self.ask_label.grid(row=5, column=0)

        self.welcome_label = tk.Label(self.master, text="WELCOME\nLOGIN TO THE STOCK MANAGER", font=("Consolas", 15),
                                      fg="purple")
        self.welcome_label.pack(side=tk.BOTTOM)
        self.welcome_label.config(bg="#B0E0E6")

        # connection to Db
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()

    def login(self):  # sourcery skip: extract-method, use-named-expression
        # check the username and password against a database
        username = self.username_entry.get()
        user_password = self.password_entry.get()

        # Get data from database
        self.cur.execute("select * from data where username=? and passeword=?", (username, user_password))
        user_data = self.cur.fetchone()

        # check user data
        if user_data:
            tk.messagebox.showinfo("login done", "successful Login")
            self.master.destroy()
            os.system("python stock_app.py")
            # Closing of db
            self.con.close()

        else:
            tk.messagebox.showerror("Login error", "Incorrect username or password")

    # define the function for submit button which go to load registration page
    def sign(self):
        self.master.destroy()
        os.system("python registration.py")


ap = tk.Tk()
ap.config(bg="#B0E0E6")
ap.title("Login")
go = Login(ap)
ap.mainloop()
