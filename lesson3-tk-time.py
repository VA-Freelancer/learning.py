from tkinter import *
import time

# рекомендуется называть переменную "root"
root = Tk()

# Размеры и положение появления окна Ширина * Высота + X + Y
root.geometry('600x400+500+300')
# Меняем заголовок окна
root.title('Vproger - check time')
# Меняем иконку окна
root.iconbitmap('python-three/python.ico')

# создаем функцию по получению и записи времени в кнопку
def check_time():
    btn_time['text'] = time.strftime('%H:%M:%S')
    # print(time.strftime('%H:%M:%S'))

btn_time = Button(root, text="Check time", command=check_time)
btn_time.pack()


root.mainloop()