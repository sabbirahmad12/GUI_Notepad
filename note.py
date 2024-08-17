from tkinter import *
from tkinter import filedialog

root = Tk()

root.title('NotePad')
root.geometry('600x600+600+100')
root.resizable(False,False)
root.config(bg = 'lightblue')

# Funtion section
def save_file():
    open_file= filedialog.asksaveasfile(mode = 'w', defaultextension='.text')
    if open_file is None:
        return
    text = str(entry.get(1.0, END))
    open_file.write(text)
    open_file.close()

def open_file():
    file = filedialog.askopenfile(mode = 'r', filetype =[('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)



# Button section
btn1 = Button(root, text = 'Save File', width = 20, height = 2, bg = '#fff', command = save_file)
btn2 = Button(root, text = 'Open File', width = 20, height = 2, bg = '#fff', command = open_file)

btn1.place(x = 100, y = 5)
btn2.place(x = 350, y = 5)

#entry section

entry = Text(root, width=72, height = 33, wrap=WORD)
entry.place(x = 10, y=60)

root.mainloop()