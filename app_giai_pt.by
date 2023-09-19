# Bai tap ngay 19/9: tao app giai phuong trinh n an n phuong trinh
import numpy as np
import tkinter as tk
from tkinter import Entry, Label, Button, messagebox

def solve_equation():
    try:
        # Get the number of variables (n)
        n = int(variables_entry.get())

        # Create a matrix A from the coefficient entries
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i][j] = float(coeff_entries[i][j].get())

        # Create a column vector B from the constant entries
        B = np.zeros((n, 1))
        for i in range(n):
            B[i] = float(constant_entries[i].get())

        # Solve the system of equations
        X = np.linalg.solve(A, B)

        # Convert the solution to a string
        solution_str = ", ".join(map(str, X))

        # Display the solution
        solution_label.config(text="Solution (X): " + solution_str)

    except ValueError as e:
        messagebox.showerror("Error", "Invalid input. Please check your entries.")

# Create a Tkinter window
root = tk.Tk()
root.title("Linear Equation Solver")

# Create labels and entry fields for the number of variables and coefficients
variables_label = Label(root, text="Number of Variables (n):")
variables_label.pack()
variables_entry = Entry(root)
variables_entry.pack()

coeff_entries = []
constant_entries = []

# Function to create entry fields dynamically based on the number of variables
def create_entries():
    n = int(variables_entry.get())
    for i in range(n):
        coeff_label = Label(root, text=f"Coefficient {i + 1}:")
        coeff_label.pack()
        coeff_entry = Entry(root)
        coeff_entry.pack()
        coeff_entries.append(coeff_entry)

    for i in range(n):
        const_label = Label(root, text=f"Constant {i + 1}:")
        const_label.pack()
        const_entry = Entry(root)
        const_entry.pack()
        constant_entries.append(const_entry)

    solve_button = Button(root, text="Solve", command=solve_equation)
    solve_button.pack()

solution_label = Label(root, text="")
solution_label.pack()

root.mainloop()
