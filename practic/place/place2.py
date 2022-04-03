from tkinter import *
import platform

root = Tk()

root.geometry('600x400+800+300') # размеры
root.title('Метод Place') #Заголовок
if(platform.system() != 'Linux'):
    root.iconbitmap('/practic/place/z.ico') #иконка
else:  
    root.iconbitmap('@z.xbm') #иконка

       

btn1 = Button(text="Button1",  bg="#3498db", fg="#fff", font="16", padx=20, pady=8)
btn1.place(x=0, y=0)

btn2 = Button(text="Button2",  bg="#2ecc71", fg="#fff", font="16", padx=20, pady=8)
btn2.place(relx=0.5, rely=0.5, anchor='c')

btn3 = Button(text="Button3",  bg="#f1c40f", fg="#fff", font="16", padx=20, pady=8)
btn3.place(relx=1, rely=1, anchor='se')

root.mainloop()