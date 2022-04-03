from tkinter import *

# рекомендуется называть переменную "root"
root = Tk()
# Размеры и положение появления окна Ширина * Высота + X + Y
root.geometry('600x400+500+300')
# Меняем заголовок окна
root.title('Vproger - check time')
# Меняем иконку окна
root.iconbitmap('python.ico')
# создаем label
l = Label(root, text="Текст в строке 1\nТекст в строке 2\nТекст в строке 3\nТекст в строке 4\nТекст в строке 4\n", bg="#565656", fg="#e0ffff", font=("Comic Sans MS", 10, "bold"), justify=LEFT, width="100",height="10", anchor="w")

# размещаем в окне
l.pack()

root.mainloop()