from tkinter import *

# рекомендуется называть переменную "root"
root = Tk()

# Размеры и положение появления окна Ширина * Высота 
root.geometry('500x500')

frame_top = LabelFrame(root, text='Top Frame', padx=10, pady=10,)
frame_bottom = LabelFrame(root, text='Bottom Frame', padx=10, pady=10,)
frame_top.pack(pady=10)
frame_bottom.pack()
# Меняем заголовок окна
root.title('VProger - Получаем Позиционирование и надписи')
# Меняем иконку окна
root.iconbitmap('practic/Pack/pack.ico')
# создаем метку

label1 = Label(frame_top, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(side=LEFT)
label2 = Label(frame_top, text="2", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack(side=LEFT)
label3 = Label(frame_bottom, text="3", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack(side=LEFT)
label4 = Label(frame_bottom, text="4", font="15", fg="#fff", bg="#34495e", width=8, height=4).pack(side=LEFT)


root.mainloop()