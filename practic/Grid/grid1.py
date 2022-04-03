from tkinter import *

root = Tk()
#первый вариант
root.geometry('600x400+800+300') # размеры
root.title('Метод Grid') #Заголовок
root.iconbitmap('practic/Grid/z.ico') #иконка

container_frame = Frame(root)
container_frame.pack(pady=10)

btn_list = [
    '7','8','9',
    '4','5','6',
    '1','2','3',
    '0'
]

row = 0
column = 0

for i in btn_list:
    if i == '0':
        Button(container_frame, text=i, padx=10, pady=5).grid(row=row, columnspan=3)
    else:
        Button(container_frame, text=i, padx=10, pady=5).grid(row=row, column=column)
        column += 1
        if column == 3:
            column = 0
            row += 1


root.mainloop()