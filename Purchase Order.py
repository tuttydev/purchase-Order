from tkinter import *
import tkinter as tk
from tkinter import messagebox


class MyApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tuttyDev Purchase Order")

        # Labels
        self.titleLabel = tk.Label(self, text="Purchase Order", font=("Helvetica", 18, "bold"))
        self.logo = tk.PhotoImage(file="Good 6.png")
        self.logoLabel = tk.Label(self, image=self.logo)
        self.logoLabel.pack()
        self.titleLabel.pack(pady=10)
        self.companyLabel = tk.Label(self, text="Company Name", font=("Helvetica", 14))
        self.companyLabel.pack(pady=5)

        self.nameLabel = tk.Label(self, text="Name:")
        self.nameLabel.pack(pady=5)
        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack()

        self.productLabel = tk.Label(self, text="Product:")
        self.productLabel.pack(pady=5)
        self.productEntry = tk.Entry(self)
        self.productEntry.pack()

        self.quantityLabel = tk.Label(self, text="Quantity:")
        self.quantityLabel.pack(pady=5)
        self.quantityEntry = tk.Entry(self)
        self.quantityEntry.pack()

        self.priceLabel = tk.Label(self, text="Price:")
        self.priceLabel.pack(pady=5)
        self.priceEntry = tk.Entry(self)
        self.priceEntry.pack()

        # Button
        self.submitButton = tk.Button(self, text="Submit", command=self.submit_order)
        self.submitButton.pack(pady=10)

    def submit_order(self):
        name = self.nameEntry.get()
        product = self.productEntry.get()
        quantity = self.quantityEntry.get()
        price = self.priceEntry.get()
        total = self.calculate_total(quantity, price)

        if total > 0:
            self.display_order(name, product, quantity, price, total)
        else:
            messagebox.showerror("Error", "Invalid quantity or price.")

    def calculate_total(self, quantity, price):
        try:
            quantity = int(quantity)
            price = float(price)
            total = quantity * price
            return total
        except ValueError:
            return 0.0

    def display_order(self, name, product, quantity, price, total):
        self.nameEntry.delete(0, tk.END)
        self.productEntry.delete(0, tk.END)
        self.quantityEntry.delete(0, tk.END)
        self.priceEntry.delete(0, tk.END)

        orderInfo = f"Purchase Order: \n"
        orderInfo += f"Name: {name}\n"
        orderInfo += f"Product: {product}\n"
        orderInfo += f"Quantity: {quantity}\n"
        orderInfo += f"Price: {price}\n"
        orderInfo += f"Total: {total}\n"

        # Display the purchase order details in a new window or console
        messagebox.showinfo("Purchase Order", orderInfo)


app = MyApplication()
app.mainloop()
