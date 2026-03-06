import tkinter as tk
from tkinter import messagebox

# Function to convert Celsius to Fahrenheit
def convert_temp():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        result_var.set(f"{fahrenheit:.2f}")   # precision 2
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Create window
root = tk.Tk()
root.title("Temperature Converter")

# Celsius input
tk.Label(root, text="Temperature (Celsius):").grid(row=0, column=0, padx=10, pady=10)

entry_celsius = tk.Entry(root)
entry_celsius.grid(row=0, column=1, padx=10, pady=10)

# Convert button
btn_convert = tk.Button(root, text="Convert to Fahrenheit", command=convert_temp)
btn_convert.grid(row=1, column=0, columnspan=2, pady=10)

# Result field (read-only)
tk.Label(root, text="Fahrenheit:").grid(row=2, column=0, padx=10, pady=10)

result_var = tk.StringVar()
entry_result = tk.Entry(root, textvariable=result_var, state="readonly")
entry_result.grid(row=2, column=1, padx=10, pady=10)

# Run GUI
root.mainloop()