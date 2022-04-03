from tkinter import *

# рекомендуется называть переменную "root"
root = Tk()

# Размеры и положение появления окна Ширина * Высота + X + Y
root.geometry('600x400+500+300')
# Меняем заголовок окна
root.title('Vproger - counter')
# Меняем иконку окна
root.iconbitmap('python-three/python.ico')

clicks = 0
# создаем функцию для подсчета кликов и записи, этих кликов в заголовок
def counter():
    global clicks
    clicks += 1
    root.title(f'Counter: {clicks}')

btn_cnt = Button(root, text="Counter", command=counter)
btn_cnt.pack()


root.mainloop()