

from app import percentage_to_cash, get_allocation

def calculate_allocation():
    age = int(age_entry.get())
    salary = float(salary_entry.get())
    expense = float(expense_entry.get())


    invest_amount = salary - expense

    equity, gold = get_allocation(age)

    result= f'''invest amount: ₹ {invest_amount} 
Investment breakdown:
equity:₹ {percentage_to_cash (invest_amount, equity)}
gold : ₹ {percentage_to_cash (invest_amount, gold)}'''

    result_label.config(text=result)

# 1. create a tkinter app
import tkinter as tk

root = tk.Tk()
root.title("stock market investment tool")
root.geometry("500x400")

label = tk.Label(root, text = "Enter details", font =("areial",14, "bold"))
label.pack()

frame = tk.Frame(root)
frame.pack()


# 2. fetch age from user

age_label = tk.Label(frame,text="Age:")
age_label.grid(row=0, column=0)

age_entry = tk.Entry(frame)
age_entry.grid(row=0, column=1)

#3. fetch salary from user

salary_label = tk.Label(frame,text="Monthly salary:")
salary_label.grid(row=1, column=0)

salary_entry = tk.Entry(frame)
salary_entry.grid(row=1, column=1)

expense_label = tk.Label(frame,text =" Monthly expense:")
expense_label.grid(row=2, column=0)

expense_entry = tk.Entry(frame)
expense_entry.grid(row=2,column=1)

# 5. button to calculate investable amount
button = tk.Button(root,text="calculate_investment",command=calculate_allocation)
button.pack(pady=15)

# 6  display asset allocation based on age and investable amount

result_label = tk.Label(root, text = "")
result_label.pack()

root.mainloop()

