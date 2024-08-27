import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        temp = float(entry.get())  
        conversion = conversion_type.get()  
        
        
        if conversion == "Celsius to Fahrenheit":
            result = celsius_to_fahrenheit(temp)
        elif conversion == "Celsius to Kelvin":
            result = celsius_to_kelvin(temp)
        elif conversion == "Fahrenheit to Celsius":
            result = fahrenheit_to_celsius(temp)
        elif conversion == "Fahrenheit to Kelvin":
            result = fahrenheit_to_kelvin(temp)
        elif conversion == "Kelvin to Celsius":
            result = kelvin_to_celsius(temp)
        elif conversion == "Kelvin to Fahrenheit":
            result = kelvin_to_fahrenheit(temp)
        
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

root = tk.Tk()
root.title("Temperature Converter")

entry_label = tk.Label(root, text="Enter Temperature:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

conversion_type = tk.StringVar(root)
conversion_type.set("Celsius to Fahrenheit")  # Set default option

options = [
    "Celsius to Fahrenheit",
    "Celsius to Kelvin",
    "Fahrenheit to Celsius",
    "Fahrenheit to Kelvin",
    "Kelvin to Celsius",
    "Kelvin to Fahrenheit"
]

dropdown = tk.OptionMenu(root, conversion_type, *options)
dropdown.pack()

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()


root.mainloop()
