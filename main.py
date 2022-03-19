from tkinter import *
from tkinter import filedialog

# Functions
def open_file():
    file_path = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )

    if file_path != '':
        file_path_arr = file_path.split('/')
        indice = len(file_path_arr) - 1

        root.BtnSelectFile["text"] = file_path_arr[indice]

# Windows Config
root = Tk()
root.title(string='Video Editor - Py')
root.fontePadrao = ("Robot", "10")
root.geometry('800x800')
root.iconbitmap('./icon.ico')

# Containers
root.Header = Frame(root)
root.Header["pady"] = 10
root.Header.pack()

root.SelectFile = Frame(root)
root.SelectFile["pady"] = 10
root.SelectFile["width"] = 800
root.SelectFile.pack()


# Componts
root.titulo = Label(root.Header, text="Editor de Video!")
root.titulo["font"] = ("Robot", "20", "bold")
root.titulo["fg"] = ("#30138f")

root.BtnSelectFile = Button(root.SelectFile)
root.BtnSelectFile["text"] = "Selecionar"
root.BtnSelectFile["font"] = root.fontePadrao
root.BtnSelectFile["width"] = 12
root.BtnSelectFile["font"] = ("bold")
root.BtnSelectFile["fg"] = ("#30138f")
root.BtnSelectFile["command"] = lambda:open_file()
root.BtnSelectFile.pack(side="left")

root.titulo.pack()
root.mainloop()
