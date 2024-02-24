import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# ----------------------------------GLOBALS------------------------------------

FILE_NAME = ''

# ----------------------------------GLOBALS------------------------------------


root = tk.Tk()
root.geometry('500x500')
root.configure(bg='black')
root.title('Untitled')

text_widget = tk.Text(root)
text_widget.pack(expand=True, fill='both')

#FUNCTIONS
#--------------------File(start)-----------------------------
def New_File():
    txt_area.delete(1.0,'end')

def Save():
    global FILE_NAME
    if FILE_NAME:
        with open(FILE_NAME, "w") as file:
            file.write(text_widget.get("1.0", tk.END))
        print("File saved successfully:", FILE_NAME)
    else:
        Save_As()

def set_file_name(file_path):
    global FILE_NAME
    FILE_NAME = file_path
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    root.title(file_name)  # Update the window title with just the file name

def Save_As():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get("1.0", tk.END))
        set_file_name(file_path)
        print("File saved successfully:", file_path)


def Exit():
    res =  messagebox.askquestion('Exit','You sure ???')
    if res == 'yes':
        root.destroy()
    else:
        root.deiconify()
#--------------------File(end)-----------------------------


#--------------------Edit(start)-----------------------------

def Undo():
    txt_area.edit_undo()

def Redo():
    txt_area.edit_redo()

def Cut():
    txt_area.event_generate("<<Cut>>")

def Copy():
    txt_area.event_generate("<<Copy>>")

def Paste():
    txt_area.event_generate("<<Paste>>")

def Find():
    pass

def Replace():
    pass

#--------------------Edit(end))-----------------------------


#Text area
txt_area = tk.Text(root,wrap='word', undo=True) #word-> wrap at word boundries
txt_area.pack(expand=True,fill='both')

#Menu
menu_bar = tk.Menu(root)

#-----------------------File(start)------------------------------
file_menu = tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New',command=New_File)
file_menu.add_command(label='Save',command=Save)
file_menu.add_command(label='Save As',command=Save_As)

file_menu.add_separator()

file_menu.add_command(label='Exit',command=Exit)
menu_bar.add_cascade(label='File',menu=file_menu)
#------------------------File(end)------------------------------

#------------------------edit(start)------------------------------
Edit_menu = tk.Menu(menu_bar,tearoff=0)
Edit_menu = tk.Menu(menu_bar,tearoff=0)
Edit_menu.add_command(label='Undo',command=Undo)
Edit_menu.add_command(label='Redo',command=Redo)

Edit_menu.add_separator()

Edit_menu.add_command(label='Cut',command=Cut)
Edit_menu.add_command(label='Copy',command=Copy)
Edit_menu.add_command(label='Paste',command=Paste)

Edit_menu.add_separator()

Edit_menu.add_command(label='Find',command=Find)
Edit_menu.add_command(label='Replace',command=Replace)
#------------------------edit(end)------------------------------

menu_bar.add_cascade(label='Edit',menu=Edit_menu)

Format_menu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Format',menu=Format_menu)

View_menu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='View',menu=View_menu)

Help_menu = tk.Menu(menu_bar,tearoff=0)

menu_bar.add_cascade(label='Help',menu=Help_menu)
root.config(menu=menu_bar)



root.mainloop()