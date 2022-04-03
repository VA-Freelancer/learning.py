from tkinter import *

# рекомендуется называть переменную "root"
root = Tk()

# создаем словарь 

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
# создаем словарь 
colors = {
    "#FE080D" : "Красный",
    "#FE9307" : "Оранжевый",
    "#FEF506" : "Желтый",
    "#41C903" : "Зеленый",
    "#2AC3FC" : "Голубой",
    "#0225F3" : "Синий",
    "#5630C3" : "Фиолетовый",
    "#800000" : "Коричнево-малиновый",
    "#000080" : "Форма морских офицеров"
}
for k, v in colors.items():
    Button(root, bg=k, command=lambda text=v, hex=k: get_color(text, hex)).pack(fill=X)


root.mainloop()