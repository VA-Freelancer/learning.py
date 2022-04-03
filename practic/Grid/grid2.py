from tkinter import *

root = Tk()
#второй вариант
# root.geometry('600x400+800+300') # размеры
root.title('Метод Grid') #Заголовок
root.iconbitmap('practic/Grid/z.ico') #иконка

text_login = Label(root, text="Login:").grid(row=0, column=0, padx=10, pady=10, sticky=W)
input_login = Entry(root).grid(row=0, column=1, columnspan=2, padx=10, sticky=W+E)

text_pass = Label(root, text="Password:").grid(row=1, column=0, padx=10, sticky=W)
input_pass = Entry(root, show='*').grid(row=1, column=1, columnspan=2, padx=10, sticky=W+E)

btn_login = Button(root, text="Вход", padx=5).grid(row=2, column=0, padx=10, pady=10, sticky=W)
btn_reg = Button(root, text="Регистрация", padx=5).grid(row=2, column=1)
btn_forgot = Button(root, text="Забыли пароль?", padx=5).grid(row=2, column=2, padx=10)

root.mainloop()