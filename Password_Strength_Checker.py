import tkinter as tk
import string

def check_strength():
    pwd = entry.get()

    length = len(pwd) >= 8
    digit = any(c.isdigit() for c in pwd)
    special = any(c in string.punctuation for c in pwd)

    if length and digit and special:
        result.set("Strong")
    elif length and (digit or special):
        result.set("Moderate")
    else:
        result.set("Weak")

root = tk.Tk()
root.title("Password Strength")

tk.Label(root,text="Enter Password").pack()

entry = tk.Entry(root, show="*")
entry.pack()

tk.Button(root,text="Check Strength",command=check_strength).pack()

result = tk.StringVar()
tk.Label(root,textvariable=result).pack()

root.mainloop()