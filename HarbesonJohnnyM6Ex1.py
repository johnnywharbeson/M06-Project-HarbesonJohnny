import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (9/5) * celsius + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit}°F")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for Celsius.")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (5/9) * (fahrenheit - 32)
        result_label.config(text=f"{fahrenheit}°F = {celsius}°C")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for Fahrenheit.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Celsius to Fahrenheit
celsius_frame = tk.Frame(root)
celsius_frame.pack(pady=20)

celsius_label = tk.Label(celsius_frame, text="Enter Celsius:")
celsius_label.pack(side=tk.LEFT)

celsius_entry = tk.Entry(celsius_frame)
celsius_entry.pack(side=tk.LEFT)

celsius_button = tk.Button(celsius_frame, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
celsius_button.pack(side=tk.LEFT)

# Fahrenheit to Celsius
fahrenheit_frame = tk.Frame(root)
fahrenheit_frame.pack(pady=20)

fahrenheit_label = tk.Label(fahrenheit_frame, text="Enter Fahrenheit:")
fahrenheit_label.pack(side=tk.LEFT)

fahrenheit_entry = tk.Entry(fahrenheit_frame)
fahrenheit_entry.pack(side=tk.LEFT)

fahrenheit_button = tk.Button(fahrenheit_frame, text="Convert to Celsius", command=fahrenheit_to_celsius)
fahrenheit_button.pack(side=tk.LEFT)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
