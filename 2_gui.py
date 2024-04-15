# Write a GUI program to find the sum of two numbers
import tkinter as tk

def find_sum():
    try:
        num1 = first_number_entry.get()
        num2 = second_number_entry.get()
        if "." in num1 or "." in num2:
            _sum = float(num1)+float(num2)
        else:
            _sum = int(num1)+int(num2)
        result.config(text=f"The sum of {num1} and {num2} is {_sum}")
    except ValueError:
        result.config(text="Invalid Input")

root = tk.Tk()
root.title("Sum Calculator")
root.geometry("353x129")

first_number_label = tk.Label(root,text="Enter first number: ")
first_number_label.grid(row=0,column=0)
first_number_entry = tk.Entry(root)
first_number_entry.grid(row=0,column=1)

second_number_label = tk.Label(root,text="Enter second number: ")
second_number_label.grid(row=1,column=0)
second_number_entry = tk.Entry(root)
second_number_entry.grid(row=1,column=1)

sum_button = tk.Button(root,text="Sum",command=find_sum)
sum_button.grid(row=2,column=0,columnspan=4,pady=4)

result = tk.Label(root,text="")
result.grid(row=3,column=0,columnspan=4)

root.mainloop()
