import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_output.delete(0, tk.END)
            password_output.insert(0, "Invalid length")
            return
    except ValueError:
         password_output.delete(0, tk.END)
         password_output.insert(0, "Invalid input")
         return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_output.delete(0, tk.END)
    password_output.insert(0, password)

def copy_password():
    password = password_output.get()
    pyperclip.copy(password)

window = tk.Tk()
window.title("Password Generator")

length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

password_output = tk.Entry(window)
password_output.pack()

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_password)
copy_button.pack()

window.mainloop()