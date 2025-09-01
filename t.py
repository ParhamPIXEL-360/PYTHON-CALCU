import customtkinter as ctk
import math

# ساخت پنجره
app = ctk.CTk()
app.geometry("300*250")
app.title("CALAU")

# نمایشگر
display = ctk.CTkLabel(app, text="0", font=("Arial", 30))
display.pack(pady=20)

# فریم برای دکمه‌ها
frame_buttons = ctk.CTkFrame(app)
frame_buttons.pack()

# تابع اضافه کردن عدد
def press_number(num):
    current = display.cget("text")
    if current == "0":
        display.configure(text=str(num))
    else:
        display.configure(text=current + str(num))

# تابع اضافه کردن عملیات
def press_operator(op):
    current = display.cget("text")
    display.configure(text=current + op)

# تابع محاسبه
def calculate():
    try:
        expr = display.cget("text")
        expr = expr.replace("^", "**")  # تبدیل توان
        result = eval(expr)
        display.configure(text=str(result))
    except:
        display.configure(text="Error")

# تابع پاک کردن
def clear():
    display.configure(text="0")

# دکمه‌ها
buttons = [
    ("7",0,0), ("8",0,1), ("9",0,2), ("/",0,3),
    ("4",1,0), ("5",1,1), ("6",1,2), ("*",1,3),
    ("1",2,0), ("2",2,1), ("3",2,2), ("-",2,3),
    ("0",3,0), (".",3,1), ("=",4,1), ("+",3,3),
    ("C",4,0), ("^",3,2)
]

for (text,row,col) in buttons:
    if text.isdigit() or text == ".":
        cmd = lambda x=text: press_number(x)
    elif text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear
    else:
        cmd = lambda x=text: press_operator(x)
    
    button = ctk.CTkButton(frame_buttons, text=text, width=60, height=60, command=cmd)
    button.grid(row=row, column=col, padx=5, pady=5)

app.mainloop()
