from tkinter import *

# рекомендуется называть переменную "root"
root = Tk()
# Меняем заголовок окна
root.title('Vproger - First GUI app')
# Меняем иконку окна
root.iconbitmap('python-three/python.ico')
# Размеры и положение появления окна Ширина * Высота + X + Y
root.geometry('600x400+500+300')
# Разрешаем или запрещаем растягивание (Ширина, Высота)
root.resizable(True, False)
# Первый способ поменять фон
# root.config(bg='#E0FFFF')
root['bg']='#E0FFFF'

# цикл обработки окна
root.mainloop()