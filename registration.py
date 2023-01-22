import tkinter as tk
import tkinter.messagebox
import sqlite3
import os


class Registration:
    def __init__(self, master_2):
        self.master = master_2
        self.login_frame = tk.Frame(master_2)
        self.login_frame.pack(pady=200)
        self.login_frame.config(bg="#B0E0E6", padx=100)


        self.username_label = tk.Label(self.login_frame, text="Username*: ", font=("Consolas", 14), fg="blue",
                                       bg="#000080")
        self.username_label.config(bg="#B0E0E6")

        self.password_label = tk.Label(self.login_frame, text="Password*: ", font=("Consolas", 14), fg="blue",
                                       bg="#000080")
        self.password_label.config(bg="#B0E0E6")

        self.phone_number_label = tk.Label(self.login_frame, text="Phone number : ", font=("Consolas", 14), fg="blue",
                                           bg="#000080")
        self.phone_number_label.config(bg="#B0E0E6")

        self.email_label = tk.Label(self.login_frame, text="Email adresse* : ", font=("Consolas", 14), fg="blue",
                                    bg="#000080")
        self.email_label.config(bg="#B0E0E6")

        self.date_of_birth_label = tk.Label(self.login_frame, text="Your birthday date : ", font=("Consolas", 14),
                                            fg="blue",
                                            bg="#B0E0E6")

        self.username_entry = tk.Entry(self.login_frame, font=("Consolas", 14), bg="#7aa600")
        self.password_entry = tk.Entry(self.login_frame, font=("Consolas", 14), bg="#7aa600")
        self.phone_entry = tk.Entry(self.login_frame, font=("Consolas", 14), bg="#7aa600")
        self.email_entry = tk.Entry(self.login_frame, font=("Consolas", 14), bg="#7aa600")
        self.date_of_birth_entry = tk.Entry(self.login_frame, font=("Consolas", 14), bg="#7aa600")

        self.username_label.grid(row=0, column=0, sticky="E", padx=15, pady=15)
        self.username_entry.grid(row=0, column=1, padx=15, pady=15)

        self.password_label.grid(row=1, column=0, sticky="E", padx=15, pady=15)
        self.password_entry.grid(row=1, column=1, padx=15, pady=15)

        self.phone_number_label.grid(row=2, column=0, sticky="E", padx=15, pady=15)
        self.phone_entry.grid(row=2, column=1, padx=15, pady=15)

        self.email_label.grid(row=3, column=0, sticky="E", padx=15, pady=15)
        self.email_entry.grid(row=3, column=1, padx=15, pady=15)

        self.date_of_birth_label.grid(row=4, column=0, sticky="E", padx=15, pady=15)
        self.date_of_birth_entry.grid(row=4, column=1, padx=15, pady=15)

        self.submit_button = tk.Button(self.login_frame, text="SUBMIT", command=self.submit)
        self.submit_button.grid(row=5, column=1)

        # connection to Db
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()

    def submit(self):  # sourcery skip: extract-method, use-named-expression
        # check the username and password against a database
        username = self.username_entry.get()
        user_password = self.password_entry.get()
        phone = self.phone_entry.get()
        email_adresse = self.email_entry.get()
        date = self.date_of_birth_entry.get()
        if username == "" or user_password == "" or email_adresse == "":
            tk.messagebox.showerror("need it", "YOU MUST ENTER THE MANDATORY INFORMATION MARKED WITH A * ")
        else:
            self.cur.execute("insert into data(username, passeword, phone, email, date_of_birth) values(?,?,?,?,?)",
                             (username, user_password, phone, email_adresse, date))
            self.con.commit()
            tk.messagebox.showinfo("Registration done", f"Welcome you are our new user {username}")

            # After submit data, We will redirect the user to the login page
            self.master.destroy()
            os.system("python login_to_stock_app.py")


app = tk.Tk()
app.title("Registration Page")
top_label = tk.Label(app, text="PLEASE REGISTER ", font=("Consolas", 20), pady=10)
top_label.pack(side='top')
go = Registration(app)
app.mainloop()
