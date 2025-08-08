from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import datetime


def create_file():
    form = tk.Toplevel(root)
    form.title("Create Record")
    form.geometry("600x600")
    form.configure(bg="#e6f7ff")

    
    records = []

    
    tk.Label(form, text="Item Number:", bg="#e6f7ff", font=("Arial", 20), fg="black").grid(row=0, column=0, pady=10, padx=10)
    entry_ino = tk.Entry(form, font=("Arial", 20))
    entry_ino.grid(row=0, column=1, pady=10, padx=10)

    tk.Label(form, text="Item Name:", bg="#e6f7ff", font=("Arial", 20), fg="black").grid(row=1, column=0, pady=10, padx=10)
    entry_iname = tk.Entry(form, font=("Arial", 20))
    entry_iname.grid(row=1, column=1, pady=10, padx=20)

    tk.Label(form, text="Quantity:", bg="#e6f7ff", font=("Arial", 20), fg="black").grid(row=2, column=0, pady=10, padx=10)
    entry_qty = tk.Entry(form, font=("Arial", 20))
    entry_qty.grid(row=2, column=1, pady=10, padx=10)

    tk.Label(form, text="Expiry Date (YYYY-MM-DD):", bg="#e6f7ff", font=("Arial", 20), fg="black").grid(row=3, column=0, pady=10, padx=10)
    entry_expiry = tk.Entry(form, font=("Arial", 20))
    entry_expiry.grid(row=3, column=1, pady=10, padx=10)

    tk.Label(form, text="Price:", bg="#e6f7ff", font=("Arial", 20), fg="black").grid(row=4, column=0, pady=10, padx=10)
    entry_price = tk.Entry(form, font=("Arial", 20))
    entry_price.grid(row=4, column=1, pady=10, padx=10)


    def save_data():
        nonlocal records
        try:
            
            ino = int(entry_ino.get())
            iname = entry_iname.get()
            qty = int(entry_qty.get())
            expiry_date = entry_expiry.get()
            price = int(entry_price.get())


            # Append new record
            records.append([ino, iname, qty, expiry_date, price])

            # Clear form fields
            entry_ino.delete(0, tk.END)
            entry_iname.delete(0, tk.END)
            entry_qty.delete(0, tk.END)
            entry_expiry.delete(0, tk.END)
            entry_price.delete(0, tk.END)

            # Ask user whether to continue or finish
            if messagebox.askyesno("Continue?", "Add more items?"):
                return  # Exit this iteration, stay on the form
            else:
                # Save to file
                with open('Stock.dat', 'wb') as f:
                    pickle.dump(records, f)
                messagebox.showinfo("Success", "File created successfully.")
                form.destroy()  # Close the form
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check the fields.")
    
    tk.Button(form, text="Save", command=save_data, bg="#0080ff", font=("Arial", 20), width=10, fg="black").grid(row=5, column=1, pady=20)


    
    
def add_at_end():
    form = tk.Toplevel(root)
    form.title("Add Items")
    form.geometry("600x600")
    form.configure(bg="#e6f7ff")

    tk.Label(form, text="Item Number:", bg="#e6f7ff", font=("Arial", 20),fg="black").grid(row=0, column=0, pady=10, padx=10)
    entry_ino = tk.Entry(form, font=("Arial", 20))
    entry_ino.grid(row=0, column=1, pady=10, padx=10)

    tk.Label(form, text="Item Name:", bg="#e6f7ff", font=("Arial", 20),fg="black").grid(row=1, column=0, pady=10, padx=10)
    entry_iname = tk.Entry(form, font=("Arial", 20))
    entry_iname.grid(row=1, column=1, pady=10, padx=10)

    tk.Label(form, text="Quantity:", bg="#e6f7ff", font=("Arial", 20),fg="black").grid(row=2, column=0, pady=10, padx=10)
    entry_qty = tk.Entry(form, font=("Arial", 20))
    entry_qty.grid(row=2, column=1, pady=10, padx=10)

    tk.Label(form, text="Expiry Date (YYYY-MM-DD):", bg="#e6f7ff", font=("Arial", 20),fg="black").grid(row=3, column=0, pady=10,
                                                                                            padx=10)
    entry_expiry = tk.Entry(form, font=("Arial", 20))
    entry_expiry.grid(row=3, column=1, pady=10, padx=10)

    tk.Label(form, text="Price:", bg="#e6f7ff", font=("Arial", 20),fg="black").grid(row=4, column=0, pady=10,
                                                                                            padx=10)
    entry_price = tk.Entry(form, font=("Arial", 20))
    entry_price.grid(row=4, column=1, pady=10, padx=10)

    

    try:
        with open('Stock.dat', 'rb') as f:
            records = pickle.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return

    def save_data():
        nonlocal records
        try:
            ino = int(entry_ino.get())
            iname = entry_iname.get()
            qty = int(entry_qty.get())
            expiry_date = entry_expiry.get()
            price = int(entry_price.get())
            records.append([ino, iname, qty, expiry_date, price])
            entry_ino.delete(0, tk.END)
            entry_iname.delete(0, tk.END)
            entry_qty.delete(0, tk.END)
            entry_expiry.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            if messagebox.askyesno("Continue?", "Add more items?"):
                return
            with open('Stock.dat', 'wb+') as f:
                pickle.dump(records, f)
            messagebox.showinfo("Success", "Items added successfully.")
            form.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check the fields.")
    tk.Button(form, text="Save", command=save_data, bg="#0080ff", fg="black", font=("Arial", 20), width=10).grid(row=5,
                                                                                                                 column=1,
                                                                                                                 pady=20)


    

def read_file():
    try:
        with open('Stock.dat', 'rb') as f:
            records = pickle.load(f)
            output = "INo\tName\tQty\tExpiry Date\nPrice\n" + "\n".join(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}" for r in records)
        messagebox.showinfo("Inventory", output)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")


def sort_file():
    try:
        with open('Stock.dat', 'ab+') as f:
            records = pickle.load(f)
            records.sort()
            f.seek(0)
            pickle.dump(records, f)
        messagebox.showinfo("Success", "File sorted successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")


def search_item_by_number():
    search_window = tk.Toplevel(root, bg="#e6f7ff")
    search_window.title("Search by Item Number")
    search_window.geometry("400x400")
    search_window.configure(bg="#e6f7ff")

    tk.Label(search_window, text="Item Number:", bg="#e6f7ff", fg="black", font=("Arial", 20)).grid(row=0, column=0, padx=10, pady=10)
    entry_item_number = tk.Entry(search_window)
    entry_item_number.grid(row=0, column=1)

    
    def search():
        try:
            item_number = int(entry_item_number.get())
            with open("Stock.dat", "rb") as file:
                inventory = pickle.load(file)
            for item in inventory:
                if item[0] == item_number:
                    result = f"Item Found:\nName: {item[1]}\nQuantity: {item[2]}\nExpiry Date:{item[3]}\nPrice:{item[4]}\n"
                    messagebox.showinfo("Result", result)
                    return
            messagebox.showinfo("Result", "Item not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error searching item: {e}")
    tk.Button(search_window, text="Search", command=search, bg="#0080ff", fg="black", font=("Arial", 20), width=10).grid(row=1, column=0, columnspan=2, pady=20)

    

def search_item_by_name():
    search_window = tk.Toplevel(root, bg="#e6f7ff")
    search_window.title("Search by Item Name")
    search_window.geometry("400x400")
    search_window.configure(bg="#e6f7ff")

    tk.Label(search_window, text="Name:", bg="#e6f7ff", fg="black", font=("Arial",20)).grid(row=0, column=0, padx=10, pady=10)
    entry_name = tk.Entry(search_window)
    entry_name.grid(row=0, column=1)
    
    def search():
        try:
            name = entry_name.get().lower()
            with open("Stock.dat", "rb") as file:
                inventory = pickle.load(file)
            for item in inventory:
                if item[1].lower() == name:
                    result = f"Item Found:\nName: {item[1]}\nQuantity: {item[2]}\nExpiry Date:{item[3]}\nPrice:{item[4]}\n"
                    messagebox.showinfo("Result", result)
                    return
            messagebox.showinfo("Result", "Item not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error searching item: {e}")
    tk.Button(search_window, text="Search", command=search, bg="#0080ff", fg="black", font=("Arial", 20), width=10).grid(row=1, column=0, columnspan=2, pady=20)

    
def issue_item():
    issue_window = tk.Toplevel(root)
    issue_window.title("Issue Item")
    issue_window.geometry("400x400")
    issue_window.configure(bg="#e6f7ff")

    tk.Label(issue_window, text="Item Number:", bg="#e6f7ff", font=("Arial", 20),fg="black").grid(row=0, column=0, padx=10, pady=10)
    entry_item_number = tk.Entry(issue_window)
    entry_item_number.grid(row=0, column=1)

    tk.Label(issue_window, text="Quantity:", bg="#e6f7ff", font=("Arial", 20),fg="black").grid(row=1, column=0, padx=10, pady=10)
    entry_quantity = tk.Entry(issue_window)
    entry_quantity.grid(row=1, column=1)
    def issue():
        try:
            item_number = int(entry_item_number.get())
            quantity = int(entry_quantity.get())
            with open("Stock.dat","rb") as file:
                inventory = pickle.load(file)
            for item in inventory:
                if item[0] == item_number:
                    if item[2] >= quantity:
                        item[2] -= quantity
                        with open("Stock.dat", "wb+") as file:
                            pickle.dump(inventory, file)
                        messagebox.showinfo("Success", "Items issued successfully! \n The price is: "+str(item[4]*quantity))
                        issue_window.destroy()
                        return
                    else:
                        messagebox.showinfo("Error", "Insufficient quantity!")
                        return
            messagebox.showinfo("Error", "Item not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error issuing item: {e}")

    tk.Button(issue_window, text="Issue", command=issue, bg="#0080ff", fg="black", font=("Arial", 20), width=10).grid(row=2, column=0, columnspan=2, pady=20)



def procure_item():
    def procure():
        try:
            item_number = int(entry_item_number.get())
            quantity = int(entry_quantity.get())
            with open("Stock.dat", "rb") as file:
                inventory = pickle.load(file)
            for item in inventory:
                if item[0] == item_number:
                    item[2] += quantity
                    with open("Stock.dat", "wb+") as file:
                        pickle.dump(inventory, file)
                    messagebox.showinfo("Success", "Item procured successfully! \n You will get: "+str(item[4]*quantity))
                    procure_window.destroy()
                    return
            messagebox.showinfo("Error", "Item not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error procuring item: {e}")

    procure_window = tk.Toplevel(root)
    procure_window.title("Procure Item")
    procure_window.geometry("400x400")
    procure_window.configure(bg="#e6f7ff")

    tk.Label(procure_window, text="Item Number:", bg="#e6f7ff", font=("Arial", 20),fg="black").grid(row=0, column=0, padx=10, pady=10)
    entry_item_number = tk.Entry(procure_window)
    entry_item_number.grid(row=0, column=1)

    tk.Label(procure_window, text="Quantity:", bg="#e6f7ff", font=("Arial", 20),fg="black").grid(row=1, column=0, padx=10, pady=10)
    entry_quantity = tk.Entry(procure_window)
    entry_quantity.grid(row=1, column=1)

    tk.Button(procure_window, text="Procure", command=procure, bg="#0080ff", fg="black", font=("Arial", 20), width=10).grid(row=2, column=0, columnspan=2, pady=20)


def display_all_items():
    try:
        with open('Stock.dat', 'rb') as f:
            records = pickle.load(f)
        if not records:
            messagebox.showinfo("Inventory", "No items in the inventory.")
            return
        output = "Item Number\t\tItem Name\t\tQuantity\t\tExpiry Date\t\tPrice\n" + "\n".join(
            f"{item[0]}\t\t{item[1]}\t\t{item[2]}\t\t{item[3]}\t\t{item[4]}" for item in records
        )
        display_window = tk.Toplevel(root)
        display_window.title("All Inventory Items")
        display_window.geometry("1000x400")

        text_widget = tk.Text(display_window, wrap=tk.WORD, font=("Arial", 20), bg="#e6f7ff", fg="black", padx=10, pady=10)
        text_widget.insert(tk.END, output)
        text_widget.configure(state="disabled")
        text_widget.pack(expand=True, fill="both")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Inventory Management System")
root.geometry("1500x1500")

bg_image_path = '/Users/lakshyasarin/Desktop/CS Board Project/bg_img_3.jpg' 
bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((1500, 1500))  
bg_photo = ImageTk.PhotoImage(bg_image)


bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)


tk.Label(root, text="Inventory Management System", font=("Arial", 25, "bold"),
         bg="#4da6ff", fg="white", padx=10, pady=10).pack(pady=20)


button_style = {
    "bg": "#0080ff",
    "fg": "black",
    "font": ("Arial", 20),
    "activebackground": "#0059b3",
    "activeforeground": "white",
    "width": 25,
    "pady": 5,
    "bd": 3,
}


tk.Button(root, text="Create file", command=create_file, **button_style).pack(pady=10)
tk.Button(root, text="Add an Item", command=add_at_end, **button_style).pack(pady=10)
tk.Button(root, text="Sort Items", command=sort_file, **button_style).pack(pady=10)
tk.Button(root, text="Search by Item Number", command=search_item_by_number, **button_style).pack(pady=10)
tk.Button(root, text="Search by Item Name", command=search_item_by_name, **button_style).pack(pady=10)
tk.Button(root, text="Issue Item", command=issue_item, **button_style).pack(pady=10)
tk.Button(root, text="Procure Item", command=procure_item, **button_style).pack(pady=10)
tk.Button(root, text="Display All Items", command=display_all_items, **button_style).pack(pady=10)
tk.Button(root, text="Exit", command=root.destroy, **button_style).pack(pady=20)

root.mainloop()
