from tkinter import *
import platform

root = Tk()
#первый вариант
root.geometry('600x600+800+300') # размеры
root.title('Метод Place') #Заголовок
if(platform.system() != 'Linux'):
    root.iconbitmap('/practic/place/z.ico') #иконка
else:  
    root.iconbitmap('@z.xbm') #иконка

l = Label(root, bg="#000")
l.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

root.mainloop()