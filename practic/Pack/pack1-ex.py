from tkinter import *

# рекомендуется называть переменную "root"
root = Tk()

# Размеры и положение появления окна Ширина * Высота 
root.geometry('500x500')

root.title('VProger - центруем')
# Меняем иконку окна
root.iconbitmap('practic/Pack/pack.ico')
label1 = Label(root, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(expand=1, fill=BOTH)

root.mainloop()