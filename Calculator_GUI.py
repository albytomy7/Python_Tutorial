import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        a = int(entry1.get())
        b = int(entry2.get())

        if op == "add":
            result.set(a + b)
        elif op == "sub":
            result.set(a - b)
        elif op == "mul":
            result.set(a * b)
        elif op == "div":
            result.set(a / b)

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
    except ValueError:
        messagebox.showerror("Error", "Enter valid integers")

root = tk.Tk()
root.title("Calculator")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=1)

tk.Button(root,text="Add",command=lambda:calculate("add")).grid(row=1,column=0)
tk.Button(root,text="Subtract",command=lambda:calculate("sub")).grid(row=1,column=1)
tk.Button(root,text="Multiply",command=lambda:calculate("mul")).grid(row=2,column=0)
tk.Button(root,text="Divide",command=lambda:calculate("div")).grid(row=2,column=1)

result = tk.StringVar()
tk.Entry(root,textvariable=result,state="readonly").grid(row=3,column=0,columnspan=2)

root.mainloop()