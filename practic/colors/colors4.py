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

# создаем словарь 
colors = {
    "#FE080D" : "Красный",
    "#FE9307" : "Оранжевый",
    "#FEF506" : "Желтый",
    "#41C903" : "Зеленый",
    "#2AC3FC" : "Голубой",
    "#0225F3" : "Синий",
    "#5630C3" : "Фиолетовый",
}
# Создаем класс
class MyButtonsColor:

    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.btn = Button(root, bg=hex_color, command=self.get_color)
        self.btn.pack(fill=X)
        
    def get_color(self):
        label_text['text'] = self.text_color
        input_color.delete(0, END)
        input_color.insert(0, self.hex_color)


# создаем метку
label_text = Label(root)
# создаем поля ввод
input_color = Entry(root, width=30, justify='center')

label_text.pack()
input_color.pack()

for k, v in colors.items():
    MyButtonsColor(root, v, k)

root.mainloop()