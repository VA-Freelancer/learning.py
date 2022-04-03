from tkinter import *
from tkinter import ttk

def clicked():
    print('I am, button')

# рекомендуется называть переменную "root"
root = Tk()

# создаем кнопку 
# ttk - приводим интерфейс к виду операционной системы 
# command - привязываем функцию или метод на клик
#  ttk не работает со сторонней настройкой кнопки шрифт
# btn = ttk.Button(root, text="Submit", command=clicked, width=18, font="Arial")

# Передаем шрифт обычным путем 
# btn = Button(root, text="Submit", command=clicked, width=18, font="Ubuntu 14")

# Передаем шрифт картежем 
# btn = Button(root, text="Submit", command=clicked, width=18, font=("Ubuntu, serif", 20))


# justify - работает только если текст в 2 строки
# Передаем конфиг словарем
btn = Button(root, text="Submit")
btn.configure(width=20, height=2)
btn['font'] = 'Ubuntu 18'
btn['command'] = clicked

# размещаем кнопку в окне pack - мало подходит для тонких настроек(подходит для не сложных интерфейсов)
btn.pack()

# Меняем заголовок окна
root.title('Vproger - Two GUI app')

# Меняем иконку окна
root.iconbitmap('python-three/python.ico')

# Размеры и положение появления окна Ширина * Высота + X + Y
root.geometry('600x400+500+300')

# Разрешаем или запрещаем растягивание (Ширина, Высота)
root.resizable(True, False)

# Первый способ поменять фон
# root.config(bg='#E0FFFF')

# Второй способ поменять фон
root['bg']='#E0FFFF'

# цикл обработки окна
root.mainloop()
