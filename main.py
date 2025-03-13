from tkinter import *
FONT = ("Roboto", 16, "normal")

window = Tk()
window.title("My first gui program")
window.minsize(500,300)
window.config(padx=20, pady=20)

equal_label = Label(text="is equal to: ", font=FONT)
equal_label.grid(column= 0, row = 1)

miles_label = Label(text="miles ", font=FONT)
miles_label.grid(column= 2, row = 0)

km_label = Label(text="km ", font=FONT)
km_label.grid(column= 2, row = 1)

miles_input = Entry(width=10)
miles_input.insert(END, string="0.00")
miles_input.grid(column= 1, row =0)
km_value = 0.00

def handle_button_click ():
    global km_value
    miles = miles_input.get()
    km_value = round(1.60934*float(miles), 2)
    km_value_label.config(text=f"{km_value}")

calculate_button = Button( text="click me", command=handle_button_click)
calculate_button.grid(column= 1, row =2)

km_value_label =  Label(text=km_value, font=("Roboto", 16, "normal"))
km_value_label.grid(column= 1, row =1)

window.mainloop()
