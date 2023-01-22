import tkinter as tk
import tkinter.messagebox
import time
from tkinter import ttk
import os
from stock_manage import Stock

from stock_manage import *


class App:

    def __init__(self, mon_app):
        self.mon_app = mon_app
        self.stock_manager = StockManager()

        # Creating a frame to organise widgets
        self.stock_frame = tk.Frame(self.mon_app)
        self.stock_frame.pack(side="left", fill="both", expand=True, pady=100)
        self.stock_frame.config(bg="#F08080", width=142, height=265)

        # Image in the main app
        self.image = tk.PhotoImage(file="stock.png")
        self.image_label = tk.Label(self.mon_app, image=self.image)
        # self.image_label.pack(side="top", fill='both', expand=True, pady=100)

        # Creating widgets and adding them to the frame
        self.stock_list_label = tk.Label(self.stock_frame, text="STOCK LIST:", font=("Consolas", 17, "underline"),
                                         bg="#F08080")
        self.stock_list_label.grid(row=0, column=0)
        self.stock_list_box = tk.Listbox(self.stock_frame, relief="groove", font=("Consolas", 11))
        self.stock_list_box.grid(row=1, column=0, rowspan=4, sticky="n")

        # Price widgets
        self.price_label = tk.Label(self.stock_frame, text="Price:")
        self.price_label.config(fg="blue", font="Consolas 12", bd=5, bg="#F08080")
        self.price_label.grid(row=3, column=1)
        self.price_entry = tk.Entry(self.stock_frame)
        self.price_entry.grid(row=3, column=2)

        # Name widgets
        self.name_label = tk.Label(self.stock_frame, text="Name:")
        self.name_label.config(fg="blue", font="Consolas 12", bd=5, bg="#F08080")
        self.name_label.grid(row=1, column=1)
        self.name_entry = tk.Entry(self.stock_frame)  # bg="#7aa600"
        self.name_entry.grid(row=1, column=2)

        # Quantity widgets
        self.quantity_label = tk.Label(self.stock_frame, text="Quantity:")
        self.quantity_label.config(fg="blue", font="Consolas 12", bd=5, bg="#F08080")
        self.quantity_label.grid(row=2, column=1)
        self.quantity_entry = tk.Entry(self.stock_frame)  # bg="#7aa600"
        self.quantity_entry.grid(row=2, column=2)

        # Date print
        self.label_date = tk.Label(self.stock_frame, text="Hello")
        self.label_date.grid(row=18)

        def print_date():
            heure_date = time.strftime("%d/%m/ %H:%M:%S")
            self.label_date.configure(text=heure_date, bg="#F08080")
            self.mon_app.after(1000, print_date)

        # Calling every time this fonction who print the date
        print_date()

        # add_button widgets
        self.add_button = tk.Button(self.stock_frame, text="Add Stock", command=self.add_stock)
        self.add_button.grid(row=6, column=2)
        self.add_button.config(fg="blue", font="Consolas 12", bd=5, bg="#7aa600")

        # update_button widgets
        self.update_button = tk.Button(self.stock_frame, text="Total value", command=self.display_selected_item_info)
        # self.update_button.grid(row=6, column=1)
        self.update_button.config(fg="blue", font="Arial 12", bd=5)

        # remove_button widgets
        self.remove_button = tk.Button(self.stock_frame, text="Remove Stock", command=self.remove_stock)
        self.remove_button.grid(row=6, column=3)
        self.remove_button.config(bg="red", font="Consolas 12", fg="white", bd=5)

        # quit bouton
        self.quit_button = tk.Button(mon_app, text="Quit apk", command=self.mon_app.quit)
        self.quit_button.pack(side="bottom")
        self.quit_button.config(bg="red", font="Consolas 12", fg="white", bd=6)

        self.deconnexion_button = tk.Button(mon_app, text="Deconnexion", command=self.deco)
        self.deconnexion_button.pack(side='top')
        self.deconnexion_button.config(bg="red", font="Consolas 12", fg="white", bd=6)

    def deco(self):
        if self.deconnexion_button:
            self.mon_app.destroy()
            os.system("python login_to_stock_app.py")

        # Creating menu
        """
        self.var = tk.StringVar(self.mon_app)
        self.var.set("Menu")

        # Create the drop-down menu
        self.menu = tk.OptionMenu(self.mon_app, self.var, "saint Heraud", "Option 3", "mbouma", "Anna")
        self.menu.pack(side=tk.TOP)
        self.menu.config(bg="#00FFFF", font="Consolas 12")

        # Add news options to the menu
        self.menu["menu"].add_command(label="Option 4")
        """

    def add_stock(self):  # sourcery skip: extract-method
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        if name == "" or quantity == "" or price == "":
            tk.messagebox.showerror("Input Error", "It should not have empty values")
        else:
            self.stock_manager.add_stock_to_list_stock(Stock(name, quantity, price))
            self.stock_list_box.insert(tk.END, name)
            self.name_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.name_entry.focus_set()
            tk.messagebox.showinfo("gg", f"{self.stock_manager.get_stock_list()}")

    # Attention ici
    def display_selected_item_info(self):
        # get the index of the selected item
        self.index = self.stock_list_box.curselection()

        # get the selected item from the list
        selected_item = self.stock_list_box.get(self.index)

        # display the selected item's information

        self.name_label.config(text=f"Informations sur {selected_item}: ...")
        if not self.stock_list_box.curselection():
            self.name_label.config(text="Name: ", fg="blue")  # Attention ici

    def remove_stock(self):
        # name = self.name_entry.get()
        # price = self.price_entry.get()
        # quantite = self.quantity_entry.get()
        self.stock_list_box.delete("anchor")  # anchor to delete a cursor selection
        self.stock_manager.get_stock_list()

    def total_value(self):
        # name = self.name_entry.get()
        # quantity = float(self.quantity_entry.get())
        # price = int(self.price_entry.get())
        # self.stock_list_box.insert(tk.END, self.stock_manager.get_stock_list())
        # self.stock_list_box.insert("end", self.stock_manager.get_stock_list())
        """ if self.stock_list_box.curselection():
            index = self.stock_list_box.curselection()[0]
            stock = self.stock_manager.stock_list[index]
            tk.messagebox.showerror("result", f"{price*quantity}")


"""


application = tk.Tk()
application.title("Stock Manager")
application.config(bg="#FFFFF4")
gp = App(application)
application.mainloop()
