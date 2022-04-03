from tkinter import *

root = Tk()
#первый вариант
root.geometry('600x400+800+300') # размеры
root.title('Метод Place') #Заголовок
root.iconbitmap('practic/Grid/z.ico') #иконка

l1 = Label(root, text="Hello world!", bg="#3498db", fg="#fff", font="16", padx=20, pady=8)
l1.place(x=0, y=0)

l2 = Label(root, text="Hello world!", bg="#2ecc71", fg="#fff", font="16", padx=20, pady=8)
l2.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()