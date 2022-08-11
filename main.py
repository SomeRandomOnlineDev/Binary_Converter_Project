import tkinter as tk
from tkinter import ttk


def clear_result():
    for w in result.winfo_children():
        w.destroy()
    result.grid_remove()

    entry.delete(0, tk.END)


def binary_to_text(convert):
    for w in result.winfo_children():
        w.destroy()

    # the line below is copy and pasted, just to let you know, I'm probably not as good as python as you think I am
    ascii_string = "".join([chr(int(binary, 2)) for binary in convert.split(" ")])
    ttk.Label(result, text=ascii_string).pack()

    result.grid(row=2, column=0, padx=3, pady=3)


def text_to_binary(convert):
    # clear existing result
    for w in result.winfo_children():
        w.destroy()

    for x in convert:  # iterates over each character in the list
        ascii_values = ord(x)  # gets the ascii value for x
        binary = format(ascii_values, '08b')
        ttk.Label(result, text=f'{x} = {binary}').pack()

    result.grid(row=2, column=0, padx=3, pady=3)


def mode_execution():
    mode = variable.get()
    if mode == 'Text to binary':
        text_to_binary(entry.get())
    elif mode == 'Binary to text':
        binary_to_text(entry.get())


# yo, you looked through the source code! Yeah, it's a mess, but it's mine :)

# mainline

window = tk.Tk()
window.title('Binary Converter')

window.minsize(330, 80)

entry = ttk.Entry(window, width=20)
entry.grid(row=0, column=0, padx=3, pady=3)

options = ['Select a conversion mode', 'Text to binary', 'Binary to text']

variable = tk.StringVar()
variable.set(options[0])

# frame for the conversion result
result = ttk.Frame(master=window)
result.grid(row=2, column=0, padx=3, pady=3)

drop = ttk.OptionMenu(window, variable, *options)
drop.grid(row=0, column=1, padx=3, pady=3)

btn_clear_result = ttk.Button(master=window, text='Clear results', command=lambda: clear_result())
btn_clear_result.grid(row=1, column=1, padx=3, pady=3)

btn_misc_convert = ttk.Button(master=window, text='Convert it!', command=lambda: mode_execution())
btn_misc_convert.grid(row=1, column=0, padx=3, pady=3)

# these are relics from a previous version, still here, just in case
# btn_binary_convert = tk.Button(master=window, relief=tk.RIDGE, text='Convert the binary to text', command=lambda: binary_to_text(entry.get()))
# btn_binary_convert.grid(row=0, column=1, padx=3, pady=3)

# btn_text_convert = tk.Button(master=window, relief=tk.RIDGE, text='Convert the text to binary', command=lambda: text_to_binary(entry.get()))
# btn_text_convert.grid(row=1, column=1, padx=3, pady=3)

window.mainloop()
