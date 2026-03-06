import tkinter as tk

def generate_bill():
    price = float(entry_price.get())
    qty = int(entry_qty.get())

    total = price * qty

    if total > 1000:
        total = total * 0.9   # 10% discount

    result.set(f"Final Amount: {total:.2f}")

root = tk.Tk()
root.title("Billing System")

tk.Label(root,text="Item Price").grid(row=0,column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=0,column=1)

tk.Label(root,text="Quantity").grid(row=1,column=0)
entry_qty = tk.Entry(root)
entry_qty.grid(row=1,column=1)

tk.Button(root,text="Generate Bill",command=generate_bill).grid(row=2,column=0,columnspan=2)

result = tk.StringVar()
tk.Label(root,textvariable=result).grid(row=3,column=0,columnspan=2)

root.mainloop()