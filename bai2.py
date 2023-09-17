import numpy as np
import tkinter as tk

def create_array(rows, cols, value):
    arr = np.full((rows, cols), value, dtype=np.uint)
    return arr

def generate_array():
    rows = int(entry_rows.get())
    cols = int(entry_cols.get())
    value = int(entry_value.get())

    result_array = create_array(rows, cols, value)
    display_array(result_array)

def display_array(arr):
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(arr))

# Create the main window
window = tk.Tk()
window.title("Array Generator")

# Create labels and entry fields for user input
label_rows = tk.Label(window, text="Number of rows:")
label_rows.pack()
entry_rows = tk.Entry(window)
entry_rows.pack()

label_cols = tk.Label(window, text="Number of columns:")
label_cols.pack()
entry_cols = tk.Entry(window)
entry_cols.pack()

label_value = tk.Label(window, text="Value to fill the array with:")
label_value.pack()
entry_value = tk.Entry(window)
entry_value.pack()

# Create the generate button
generate_button = tk.Button(window, text="Generate Array", command=generate_array)
generate_button.pack()

# Create the text area to display the array
result_text = tk.Text(window, height=10, width=30)
result_text.pack()

# Start the main event loop
window.mainloop()