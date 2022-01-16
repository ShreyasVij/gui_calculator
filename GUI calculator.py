from tkinter import *

root = Tk()
root.title("calculator by shreyas vij ")
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=50, pady=50)

# this function takes the number


def Button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# this clears


def clearing():
    entry.delete(0, END)


# this adds
def adding():
    first_num = entry.get()
    global num_1
    global math
    math = "adition"
    num_1 = int(first_num)
    entry.delete(0, END)

# this subtracts


def subtracting():
    first_num = entry.get()
    global num_1
    global math
    math = "sub"
    num_1 = int(first_num)
    entry.delete(0, END)

# this multiplys


def multiplying():
    first_num = entry.get()
    global num_1
    global math
    math = "mul"
    num_1 = int(first_num)
    entry.delete(0, END)

# this divides


def dividing():
    first_num = entry.get()
    global num_1
    global math
    math = "div"
    num_1 = int(first_num)
    entry.delete(0, END)

# this gives the answer


def equalling():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "adition":
        entry.insert(0, num_1+int(second_number))
    if math == "sub":
        entry.insert(0, num_1 - int(second_number))
    if math == "mul":
        entry.insert(0, num_1 * int(second_number))
    if math == "div":
        entry.insert(0, num_1 / int(second_number))


# defining the buttons


button_0 = Button(root, text="0", padx=40, pady=20,
                  command=lambda: Button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20,
                  command=lambda: Button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: Button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: Button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: Button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: Button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: Button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: Button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: Button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: Button_click(9))
button_add = Button(root, text="+", padx=40, pady=20, command=adding)
button_equal = Button(root, text="=", padx=120, pady=20, command=equalling)
button_clear = Button(root, text="clear", padx=110,
                      pady=20, command=clearing)
button_subtract = Button(root, text="-", padx=40,
                         pady=20, command=subtracting)
button_multiplication = Button(root, text="X", padx=40,
                               pady=20, command=multiplying)
button_division = Button(root, text="/", padx=40,
                         pady=20, command=dividing)

# positioning the buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0, )
button_multiplication.grid(row=4, column=1)
button_division.grid(row=4, column=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
