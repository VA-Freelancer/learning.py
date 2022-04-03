from tkinter import *

# рекомендуется называть переменную "root"
root = Tk()

# Размеры и положение появления окна Ширина * Высота 
root.geometry('300x500')
# Меняем заголовок окна
root.title('VProger - Получаем цвет')
# Меняем иконку окна
root.iconbitmap('practic/colors/rainbow.ico')
# создаем метку
label_text = Label(root)
# создаем поля ввод
input_color = Entry(root, width=30, justify='center')

def get_color(text_color, hex_color):
    label_text['text'] = text_color
    input_color.delete(0, END)
    input_color.insert(0, hex_color)

label_text.pack()
input_color.pack()
# создаем кучу кнопок 😂
btn_red = Button(root, bg="#FE080D", command=lambda: get_color('Красный', '#FE080D')).pack(fill=X)
btn_orange = Button(root, bg="#FE9307", command=lambda: get_color('Оранжевый', '#FE9307')).pack(fill=X)
btn_yellow = Button(root, bg="#FEF506", command=lambda: get_color('Желтый', '#FEF506')).pack(fill=X)
btn_green = Button(root, bg="#41C903", command=lambda: get_color('Зеленый', '#41C903')).pack(fill=X)
btn_blue = Button(root, bg="#2AC3FC", command=lambda: get_color('Голубой', '#2AC3FC')).pack(fill=X)
btn_indigo = Button(root, bg="#0225F3", command=lambda: get_color('Синий', '#0225F3')).pack(fill=X)
btn_violet = Button(root, bg="#5630C3", command=lambda: get_color('Фиолетовый', '#5630C3')).pack(fill=X)



root.mainloop()