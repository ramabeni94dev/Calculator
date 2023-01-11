from tkinter import *

root = Tk()
root.title("Calculator")



display = Entry(root, font=("arial", 20, "bold"), bd=10, insertwidth=2, fg="white", bg="#0D0D0D", justify="right")
display.grid(row=0, columnspan=6, sticky="nsew")

root.iconbitmap ("calculator.ico")
root.geometry("400x500")




i = 0

#Function

def get_numbers(n):
    global i
    display.insert(i, n)
    i+=1


def get_operation(operator):
    global i
    operator_len = len(operator)
    display.insert(i, operator)
    i+= operator_len

def clear_elements():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_elements()
        display.insert(0, display_new_state)
    else:
        clear_elements()
        display.insert(0, "Error")

def calculate():
    display_state = display.get()
    try:
        math_expression =  compile(display_state, 'app.py', 'eval')
        result = eval(math_expression)
        clear_elements()
        display.insert(0,result)
    except:
        clear_elements()
        display.insert(0,"error")

#format buttom

Color_text=("#065954")

background_display=("#0D0D0D")

background_button=("#737373")

Color_button_numeric=("#8C6E49")

Color_button_arimetic=("#A68E17")

Especial_color=("#8C7303")

class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground






#Arimetic buttom



button_1 = HoverButton(root, text="C", font="arial 16", bg=Color_button_arimetic, activebackground=background_button, command=lambda:undo())
button_1.grid(row=1, column=0, sticky="nsew")

button_2 = HoverButton(root, text="/", font="arial 16 bold", bg=Color_button_arimetic, activebackground=background_button, command=lambda:get_operation("/"))
button_2.grid(row=1, column=1, sticky="nsew")

button_3 = HoverButton(root, text="*", font="arial 16 bold", bg=Color_button_arimetic, activebackground=background_button, command=lambda:get_operation("*"))
button_3.grid(row=1, column=2, sticky="nsew")

button_4 = HoverButton(root, text="-", font="arial 16 bold", bg=Color_button_arimetic, activebackground=background_button, command=lambda:get_operation("-"))
button_4.grid(row=2, column=4, sticky="nsew")

button_5 = HoverButton(root, text="+", font="arial 16 bold", bg=Color_button_arimetic, activebackground=background_button, command=lambda:get_operation("+"))
button_5.grid(row=2, column=3, sticky="nsew")

button_6 = HoverButton(root, text="=", font="arial 16", bg=Color_button_arimetic, activebackground=background_button, command=lambda:calculate())
button_6.grid(row=5, column=3, sticky="nsew", columnspan=3)

button_7 = HoverButton(root, text="%", font="arial 16 bold", bg=Color_button_arimetic, activebackground=background_button, command=lambda:get_operation("%"))
button_7.grid(row=3, column=3, sticky="nsew")

button_8 = HoverButton(root, text="(", font="arial 16 bold", bg=Color_button_arimetic, activebackground=background_button, command=lambda:get_operation("("))
button_8.grid(row=1, column=4, sticky="nsew")

button_9 = HoverButton(root, text=")", font="arial 16 bold", bg=Color_button_arimetic, activebackground=background_button, command=lambda:get_operation(")"))
button_9.grid(row=1, column=3, sticky="nsew")

button_10 = HoverButton(root, text="*2", font="arial 16 bold", bg=Color_button_arimetic, activebackground=background_button, command=lambda:get_operation("**2"))
button_10.grid(row=4, column=4, sticky="nsew")

button_11 = HoverButton(root, text="exp", font="arial 16 bold", bg=Color_button_arimetic, activebackground=background_button, command=lambda:get_operation("**"))
button_11.grid(row=3, column=4, sticky="nsew")

# #numeric buttom

button_12 = HoverButton(root, text="7", font="arial 16 bold", bg=Color_button_numeric, activebackground=background_button, command=lambda:get_numbers(7))
button_12.grid(row=2, column=0, sticky="nsew")

button_13 = HoverButton(root, text="8", font="arial 16 bold", bg=Color_button_numeric, activebackground=background_button, command=lambda:get_numbers(8))
button_13.grid(row=2, column=1, sticky="nsew")

button_14 = HoverButton(root, text="9", font="arial 16 bold", bg=Color_button_numeric, activebackground=background_button, command=lambda:get_numbers(9))
button_14.grid(row=2, column=2, sticky="nsew")

button_15 = HoverButton(root, text="4", font="arial 16", bg=Color_button_numeric, activebackground=background_button, command=lambda:get_numbers(4))
button_15.grid(row=3, column=0, sticky="nsew")

button_16 = HoverButton(root, text="5", font="arial 16 bold", bg=Color_button_numeric, activebackground=background_button, command=lambda:get_numbers(5))
button_16.grid(row=3, column=1, sticky="nsew")

button_17 = HoverButton(root, text="6", font="arial 16 bold", bg=Color_button_numeric, activebackground=background_button, command=lambda:get_numbers(6))
button_17.grid(row=3, column=2, sticky="nsew")

button_18 = HoverButton(root, text="1", font="arial 16 bold", bg=Color_button_numeric, activebackground=background_button, command=lambda:get_numbers(1))
button_18.grid(row=4, column=0, sticky="nsew")

button_19 = HoverButton(root, text="2", font="arial 16 bold", bg=Color_button_numeric, activebackground=background_button, command=lambda:get_numbers(2))
button_19.grid(row=4, column=1, sticky="nsew")

button_20 = HoverButton(root, text="3", font="arial 16 bold", bg=Color_button_numeric, activebackground=background_button, command=lambda:get_numbers(3))
button_20.grid(row=4, column=2, sticky="nsew")

button_21 = HoverButton(root, text="0", font="arial 16 bold", bg=Color_button_numeric, activebackground=background_button, command=lambda:get_numbers(0))
button_21.grid(row=5, column=0, sticky="nsew", columnspan=3)

button_22 = HoverButton(root, text=".", font="arial 16 bold", bg=Color_button_arimetic, activebackground=background_button, command=lambda:get_operation("."))
button_22.grid(row=4, column=3, sticky="nsew")

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 1, weight=1)

Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 2, weight=1)

Grid.rowconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 3, weight=1)

Grid.rowconfigure(root, 4, weight=1)
Grid.columnconfigure(root, 4, weight=1)

Grid.rowconfigure(root, 5, weight=1)







root.mainloop()

