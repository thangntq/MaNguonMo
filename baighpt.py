import numpy as np
import tkinter as tk
from tkinter import Entry, Label, Button, messagebox

def solve_equation():
    try:
        # Lấy số biến (n)
        n = int(variables_entry.get())
        # nhóm bạn có thể thêm 1 vò while vào đây để lặp lại số phương trình, vì có thể người dùng có thể nhập 0 hoặc 1 như thế sẽ bị lỗi
        # ví dụ như sau 
        # while (n < 2 ) :
        #      n = int (input ("Nhập lại số n vì đây không phải hệ Phương trình: "))
        # Tạo ma trận A từ các giá trị nhập vào
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i][j] = float(coeff_entries[i][j].get())

        # Tạo vector cột B từ các giá trị nhập vào
        B = np.zeros((n, 1))
        for i in range(n):
            B[i] = float(constant_entries[i].get())

        # Giải hệ phương trình
        X = np.linalg.solve(A, B)

        # Hiển thị nghiệm trên giao diện
        solution_label.config(text="Nghiệm của hệ phương trình (X): " + ", ".join(map(str, X)))

    except ValueError as e:
        messagebox.showerror("Lỗi", "Giá trị nhập không hợp lệ. Vui lòng kiểm tra lại.")

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Ứng dụng giải hệ phương trình tuyến tính")

# Tạo nhãn và ô nhập dữ liệu cho số biến
variables_label = Label(root, text="Số biến (n):")
variables_label.pack()
variables_entry = Entry(root)
variables_entry.pack()

coeff_entries = []
constant_entries = []

# Hàm tạo các ô nhập dữ liệu dựa trên số biến n sau khi nhấn nút "Tạo"
def create_entries():
    n = int(variables_entry.get())
    for i in range(n):
        row_entries = []
        for j in range(n):
            coeff_label = Label(root, text=f"Hệ số {i + 1}{j + 1}:")
            coeff_label.pack()
            coeff_entry = Entry(root)
            coeff_entry.pack()
            row_entries.append(coeff_entry)
        coeff_entries.append(row_entries)

    for i in range(n):
        const_label = Label(root, text=f"Hằng số {i + 1}:")
        const_label.pack()
        const_entry = Entry(root)
        const_entry.pack()
        constant_entries.append(const_entry)

    solve_button = Button(root, text="Giải", command=solve_equation)
    solve_button.pack()

solution_label = Label(root, text="")
solution_label.pack()

create_button = Button(root, text="Tạo", command=create_entries)
create_button.pack()

root.mainloop()
