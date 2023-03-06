import tkinter as tk

calculation = ""


def add_to_caculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.title("Calculator ")
root.geometry("300x275")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)
# text_result.pack()

buton1 = tk.Button(root, text="1", command=lambda: add_to_caculation(1), width=5, font=("Arial", 14))
buton1.grid(row=2, column=1)
buton2 = tk.Button(root, text="2", command=lambda: add_to_caculation(2), width=5, font=("Arial", 14))
buton2.grid(row=2, column=2)
buton3 = tk.Button(root, text="3", command=lambda: add_to_caculation(3), width=5, font=("Arial", 14))
buton3.grid(row=2, column=3)
buton4 = tk.Button(root, text="4", command=lambda: add_to_caculation(4), width=5, font=("Arial", 14))
buton4.grid(row=3, column=1)
buton5 = tk.Button(root, text="5", command=lambda: add_to_caculation(5), width=5, font=("Arial", 14))
buton5.grid(row=3, column=2)
buton6 = tk.Button(root, text="6", command=lambda: add_to_caculation(6), width=5, font=("Arial", 14))
buton6.grid(row=3, column=3)
buton7 = tk.Button(root, text="7", command=lambda: add_to_caculation(7), width=5, font=("Arial", 14))
buton7.grid(row=4, column=1)
buton8 = tk.Button(root, text="8", command=lambda: add_to_caculation(8), width=5, font=("Arial", 14))
buton8.grid(row=4, column=2)
buton9 = tk.Button(root, text="9", command=lambda: add_to_caculation(9), width=5, font=("Arial", 14))
buton9.grid(row=4, column=3)
buton0 = tk.Button(root, text="0", command=lambda: add_to_caculation(0), width=5, font=("Arial", 14))
buton0.grid(row=5, column=2)

buton_plus = tk.Button(root, text="+", command=lambda: add_to_caculation("+"), width=5, font=("Arial", 14))
buton_plus.grid(row=2, column=4)
buton_minus = tk.Button(root, text="-", command=lambda: add_to_caculation("-"), width=5, font=("Arial", 14))
buton_minus.grid(row=3, column=4)
buton_carp = tk.Button(root, text="*", command=lambda: add_to_caculation("*"), width=5, font=("Arial", 14))
buton_carp.grid(row=4, column=4)
buton_divide = tk.Button(root, text="/", command=lambda: add_to_caculation("/"), width=5, font=("Arial", 14))
buton_divide.grid(row=5, column=4)

buton_open = tk.Button(root, text="(", command=lambda: add_to_caculation("("), width=5, font=("Arial", 14))
buton_open.grid(row=5, column=1)
buton_close = tk.Button(root, text=")", command=lambda: add_to_caculation(")"), width=5, font=("Arial", 14))
buton_close.grid(row=5, column=3)

buton_equ = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
buton_equ.grid(row=6, column=1, columnspan=2)

buton_clear = tk.Button(root, text="C", command=clear_field(), width=11, font=("Arial", 14))
buton_clear.grid(row=6, column=3, columnspan=2)






root.mainloop()
