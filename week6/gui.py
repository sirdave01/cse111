# Write a Python program named gui.py that gets user input from a GUI, 
# performs a simple calculation, and displays the result in a GUI.

# Your program must include a GUI that opens when you run your program.
# The GUI must allow a user to enter input.
# When the user enters valid input, your program must compute correct results and display those results in the GU

"""
Program: GUI calculator

Developer: Osigwe Uchechukwu David

"""
import tkinter as tk
from tkinter import messagebox
import number_entry

# defining the calculate function
def calculate():
    """Runs when Calculate button is clicked"""
    try:
        # ← Use .get() and convert to float yourself
        age_years = float(ent_age.get())
        width = float(ent_width.get())
        height = float(ent_height.get())

        age_months = age_years * 12
        area = width * height
        perimeter = 2 * (width + height)

        lbl_result_age.config(text=f"Age in months: {age_months:.0f}")
        lbl_result_area.config(text=f"Area: {area:.2f}")
        lbl_result_perimeter.config(text=f"Perimeter: {perimeter:.2f}")
        status_bar.config(text="Success!", fg="green")

    except ValueError:
        status_bar.config(text="Please enter valid numbers only", fg="red")


def clear_all():
     # ← .clear() exists in number_entry.py
    ent_age.clear()     
    ent_width.clear()
    ent_height.clear()
    
    lbl_result_age.config(text="Age in months: ")
    lbl_result_area.config(text="Area: ")
    lbl_result_perimeter.config(text="Perimeter: ")
    status_bar.config(text="Cleared", fg="blue")


# ====================== Main Window ======================
window = tk.Tk()
window.title("Simple GUI Calculator")
window.geometry("400x520")
window.configure(padx=20, pady=20)

tk.Label(window, text="Simple GUI Calculator", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

# Age
tk.Label(window, text="Enter your age in years:").grid(row=1, column=0, sticky="w")
ent_age = number_entry.FloatEntry(window)        # ← from your downloaded file
ent_age.grid(row=1, column=1, pady=5)

lbl_result_age = tk.Label(window, text="Age in months: ")
lbl_result_age.grid(row=2, column=0, columnspan=2, pady=10)

# Rectangle
tk.Label(window, text="Rectangle width:").grid(row=3, column=0, sticky="w")
ent_width = number_entry.FloatEntry(window)
ent_width.grid(row=3, column=1, pady=5)

tk.Label(window, text="Rectangle height:").grid(row=4, column=0, sticky="w")
ent_height = number_entry.FloatEntry(window)
ent_height.grid(row=4, column=1, pady=5)

lbl_result_area = tk.Label(window, text="Area: ")
lbl_result_area.grid(row=5, column=0, columnspan=2)

lbl_result_perimeter = tk.Label(window, text="Perimeter: ")
lbl_result_perimeter.grid(row=6, column=0, columnspan=2, pady=10)

# Buttons
tk.Button(window, text="Calculate", command=calculate, bg="lightgreen", font=("Arial", 12, "bold"), width=15).grid(row=7, column=0, columnspan=2, pady=15)
tk.Button(window, text="Clear", command=clear_all, bg="lightcoral", width=15).grid(row=8, column=0, columnspan=2, pady=5)

# Status bar
status_bar = tk.Label(window, text="Ready", relief="sunken", anchor="w")
status_bar.grid(row=9, column=0, columnspan=2, sticky="we")

window.mainloop()