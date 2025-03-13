import tkinter
window = tkinter.Tk()
window.title("My first gui program")
window.minsize(500,300)
window.config(padx=20, pady=20)


#Label
label = tkinter.Label(text="label", font=("Arial", 24, "bold"))
label.grid(column= 0, row = 0)
label["text"] = "new text"

#Entry
my_input = tkinter.Entry(width=10)
my_input.grid(column= 3, row =2)

#button
def handle_button_click ():
    text = my_input.get()
    label.config(text= text)
    print(text)

button = tkinter.Button( text="click me", command=handle_button_click)
button.grid(column= 1, row =1)
button.config(padx=20, pady=20)
button_new = tkinter.Button( text="button_new")
button_new.grid(column= 2, row =0)

window.mainloop()
