import tkinter as tk

def show_output():
    number = int(text_input.get())

    if number == 0:
        output_label.configure(text='คูณไม่ได้จ้า')
        return

    result = ""
    for i in range(1, 13):
        result += str(number) + ' x ' + str(i)
        result += ' = ' + str(number * i) + '\n'

    output_label.configure(text=result)

window = tk.Tk()
window.title("Justpython")
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text="สูตรคูณแม่")
title_label.pack(pady=20)

text_input = tk.Entry(master=window, width=20)
text_input.pack(pady=5)

button_input = tk.Button(
    master=window, text="ได้แก่", 
    command=show_output, width=10, height=1
)
button_input.pack(pady=20)

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()