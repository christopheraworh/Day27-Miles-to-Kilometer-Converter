from tkinter import *

window = Tk()
window.minsize(width=400, height=200)
window.title('Mile to Km converter')
window.config(padx=100)


label1 = Label(text='is equal to:')
label1.grid(row=1, column =0)

label2 = Label(text='Km')
label2.grid (row=1, column=3)
label3 = Label(text='Miles')
label3.grid(row=0, column=3)

output = Label(text='', font=('Arial',12,'bold'))
output.grid(row=1,column =1)

entry = Entry(width=10, border=3)
entry.grid(row=0, column=1)


def calculate():
    user_input = float(entry.get())
    kilometer_res = user_input/1000
    # output['text'] = kilometer_res # Alternative 1 of doing this
    output.config(text=f'{kilometer_res}')



cal_button  = Button(text='Calculate', command=calculate, background= '#E0415C')
cal_button.grid(row=5, column = 1)
# cal_button.config()
# def get_input():







window.mainloop()