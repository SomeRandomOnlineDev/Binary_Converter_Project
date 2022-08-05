import tkinter as tk

def clear_result():
    for w in result.winfo_children():
        w.destroy()
    result.grid_remove()

    entry.delete(0, tk.END)

def binary_to_text(convert):
    for w in result.winfo_children():
        w.destroy()

    window.minsize(420, 80)

    # the line below is copy and pasted, just to let you know, I'm probably not as good as python as you think I am
    ascii_string = "".join([chr(int(binary, 2)) for binary in convert.split(" ")])
    tk.Label(result, text=ascii_string).pack()

    result.grid(row=2, column=0)

def text_to_binary(convert):
    # clear existing result
    for w in result.winfo_children():
        w.destroy()

    window.minsize(420, 80)

    for x in convert:  # iterates over each character in the list
        ascii_values = ord(x)  # gets the ascii value for x
        binary = format(ascii_values, '08b')
        tk.Label(result, text=f'{x} {binary}').pack()

    result.grid(row=2, column=0)

# this is scrap code
# CORRECTION: It's no longer scrap code
# CORRECTION's CORRECTION: It's scrap again
# def mode_execution():
        # mode = variable.get()
    # if mode == 'Text to binary':
        # text_to_binary(entry.get())
    # else:
        # binary_to_text(entry.get())

# mainline

window = tk.Tk()
window.title('Binary Converter')

window.minsize(420, 80)

entry = tk.Entry(window, width=25)
entry.grid(row=0, column=0)

# options = ['Text to binary', 'Binary to text']

# variable = tk.StringVar()
# variable.set(options[1])

# frame for the conversion result
result = tk.Frame(master=window)
result.grid(row=2, column=0)

# scrap code turned into comment
# drop = tk.OptionMenu(window, variable, *options, command=mode_execution())
# drop.grid(row=0, column=2)

btn_clear_result = tk.Button(master=window, relief=tk.RIDGE, text='Clear results', command=lambda: clear_result())
btn_clear_result.grid(row=1, column=0)

# btn_misc_convert = tk.Button(master=window, relief=tk.RIDGE, text='Convert it!', command=lambda: drop)
# btn_misc_convert.grid(row=1, column=2)

btn_binary_convert = tk.Button(master=window, relief=tk.RIDGE, text='Convert the binary to text', command=lambda: binary_to_text(entry.get()))
btn_binary_convert.grid(row=0, column=1)

btn_text_convert = tk.Button(master=window, relief=tk.RIDGE, text='Convert the text to binary', command=lambda: text_to_binary(entry.get()))
btn_text_convert.grid(row=1, column=1)

window.mainloop()
