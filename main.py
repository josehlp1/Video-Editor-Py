from tkinter import *
from tkinter import filedialog
from editor import Editor
from unidecode import unidecode
import os

editor = Editor()

# Functions

def open_file():
    file_path = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("MP4 files","*.mp4"),("all files","*.*")) )

    if file_path != '':
        file_size = os.path.getsize(file_path)
        file_size = file_size *1000
        root.MsgSizeFile["text"] = "Tamanho do arquivo: "+str(round(file_size/(1000000000)))+"MB"

        editor.setVideoPath(file_path)
        file_path_arr = file_path.split('/')
        indice = len(file_path_arr) - 1

        editor.setVideoName(unidecode(file_path_arr[indice][:-4]))
        root.BtnSelectFile["text"] = file_path_arr[indice]

def audioEstractStatus():
    if root.extractAudioBtn["text"]  == "NÃO":
        root.extractAudioBtn["text"] = "SIM"
        editor.setExtractAudio(True)
    else:
        root.extractAudioBtn["text"] = "NÃO"
        editor.setExtractAudio(False)

def startEdition():
    editor.setVideoCuts(root.CutsInput.get())
    if editor.startEdition() == True:
        print('Sucesso')
        root.LabelError["fg"] = "#0eab20"
        root.LabelError["text"] = "Sucesso: Video editado com sucesso!"
    else:
        print('Erro')
        root.LabelError["fg"] = "#c40424"
        root.LabelError["text"] = "Erro: Verifique se todos os campos estão preenchidos!"


def cancelEdition():
    root.BtnSelectFile["text"] = "Selecionar"
    editor.setVideoPath("")
    root.CutsInput.delete(0, END)


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

root.MsgSize = Frame(root)
root.MsgSize["pady"] = 10
root.MsgSize["width"] = 800
root.MsgSize.pack()

root.SelectOptions = Frame(root)
root.SelectOptions["pady"] = 10
root.SelectOptions["width"] = 800
root.SelectOptions.pack()

root.FinalOptions = Frame(root)
root.FinalOptions["pady"] = 10
root.FinalOptions["width"] = 800
root.FinalOptions.pack()

root.Msgs = Frame(root)
root.Msgs["pady"] = 10
root.Msgs["width"] = 800
root.Msgs.pack()


# Components
root.titulo = Label(root.Header, text="Editor de Video!")
root.titulo["font"] = ("Robot", "20", "bold")
root.titulo["fg"] = ("#30138f")

root.BtnSelectFile = Button(root.SelectFile)
root.BtnSelectFile["text"] = "Selecionar"
root.BtnSelectFile["font"] = root.fontePadrao
root.BtnSelectFile["width"] = 20
root.BtnSelectFile["font"] = ("bold")
root.BtnSelectFile["fg"] = ("#30138f")
root.BtnSelectFile["command"] = lambda:open_file()
root.BtnSelectFile.pack(side="left")

root.MsgSizeFile = Label(root.MsgSize, text="", font=root.fontePadrao)
root.MsgSizeFile["font"] = root.fontePadrao
root.MsgSizeFile["width"] = 90
root.MsgSizeFile.grid(row=0, column=3, padx=10, pady=10)

video_label = Label(root.BtnSelectFile)

root.CutsLabel = Label(root.SelectOptions, text="Número de Cortes: ", font=root.fontePadrao)
root.CutsLabel.pack(side=LEFT)
root.CutsLabel["font"] = root.fontePadrao
root.CutsLabel["width"] = 15
root.CutsLabel.grid(row=0, column=1, padx=10, pady=10)

root.CutsInput = Entry(root.SelectOptions)
root.CutsInput["font"] = root.fontePadrao
root.CutsInput["width"] = 20
root.CutsInput.grid(row=0, column=2, padx=10, pady=10)

root.extractAudioLabel = Label(root.SelectOptions, text="Extrair Áudio: ", font=root.fontePadrao)
root.extractAudioLabel["font"] = root.fontePadrao
root.extractAudioLabel["width"] = 15
root.extractAudioLabel.grid(row=0, column=3, padx=10, pady=10)

root.extractAudioBtn = Button(root.SelectOptions)
root.extractAudioBtn["text"] = "NÃO"
root.extractAudioBtn["font"] = root.fontePadrao
root.extractAudioBtn["width"] = 10
root.extractAudioBtn.grid(row=0, column=4, padx=10, pady=10)
root.extractAudioBtn["font"] = ("bold")
root.extractAudioBtn["fg"] = ("#30138f")
root.extractAudioBtn["command"] = lambda:audioEstractStatus()

root.BtnStart = Button(root.FinalOptions)
root.BtnStart["text"] = "Iniciar"
root.BtnStart["font"] = root.fontePadrao
root.BtnStart["width"] = 10
root.BtnStart.grid(row=0, column=1, padx=20, pady=20)
root.BtnStart["font"] = ("bold")
root.BtnStart["fg"] = ("#30138f")
root.BtnStart["command"] = lambda:startEdition()


root.BtnCancel = Button(root.FinalOptions)
root.BtnCancel["text"] = "Cancelar"
root.BtnCancel["font"] = root.fontePadrao
root.BtnCancel["width"] = 10
root.BtnCancel.grid(row=0, column=2, padx=20, pady=20)
root.BtnCancel["font"] = ("bold")
root.BtnCancel["fg"] = ("#30138f")
root.BtnCancel["command"] = lambda:cancelEdition()

root.LabelError = Label(root.Msgs, text="", font=root.fontePadrao)
root.LabelError["font"] = root.fontePadrao
root.LabelError["font"] = ("bold")
root.LabelError["width"] = 50
root.LabelError.grid(row=1, column=3, padx=20, pady=20)

root.titulo.pack()
root.mainloop()
