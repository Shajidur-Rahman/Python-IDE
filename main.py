from tkinter import *

compiler = Tk()
compiler.title("Python IDE")


def run():
    code = editor.get('1.0', END)
    # print("Code will be run")
    # print(code)
    exec(code)


menu_bar = Menu(compiler)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)

# menu_bar.add_cascade(lable='Run', menu=run_bar)
menu_bar.add_cascade(label="Run", menu=run_bar)
compiler.config(menu=menu_bar)


editor = Text()
editor.pack()

compiler.mainloop()