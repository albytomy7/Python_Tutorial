import tkinter as tk

# Function to clear the label
def clear_label():
    label.config(text="")
    clear_button.config(state=tk.DISABLED)
    restore_button.config(state=tk.NORMAL)

# Function to restore the label
def restore_label():
    label.config(text="Python GUI Demo")
    restore_button.config(state=tk.DISABLED)
    clear_button.config(state=tk.NORMAL)

# Create main window
root = tk.Tk()
root.title("Python GUI")

# Label
label = tk.Label(root, text="Python GUI Demo", font=("Arial", 14))
label.pack(pady=10)

# Clear Button
clear_button = tk.Button(root, text="Clear", command=clear_label)
clear_button.pack(side="left", padx=20, pady=10)

# Restore Button
restore_button = tk.Button(root, text="Restore", command=restore_label, state=tk.DISABLED)
restore_button.pack(side="right", padx=20, pady=10)

# Run the GUI
root.mainloop()