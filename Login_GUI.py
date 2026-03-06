import tkinter as tk
from tkinter import messagebox

def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == "" or pwd == "":
        messagebox.showwarning("Error", "Username or Password cannot be empty")
    elif user == "admin" and pwd == "1234":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Credentials")

root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username").grid(row=0, column=0)
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0)
entry_pass = tk.Entry(root, show="*")
entry_pass.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2)

root.mainloop()