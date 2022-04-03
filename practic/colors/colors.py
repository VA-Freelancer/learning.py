from tkinter import *

# рекомендуется называть переменную "root"
# не очень удачная функция 
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

def color_red():
    label_text['text'] = 'Красный'
    input_color.delete(0, END)
    input_color.insert(0, '#ff0000')
    

def color_orange():
    label_text['text'] = 'Оранжевый'
    input_color.delete(0, END)
    input_color.insert(0, '#ffa500')


def color_yellow():
    label_text['text'] = 'Желтый'
    input_color.delete(0, END)
    input_color.insert(0, '#ffff00')

label_text.pack()
input_color.pack()

btn_red = Button(root, bg="#ff0000", command=color_red).pack(fill=X)
btn_orange = Button(root, bg="#ffa500", command=color_orange).pack(fill=X)
btn_yellow = Button(root, bg="#ffff00",command=color_yellow).pack(fill=X)
# btn_green = Button(root, bg="#008000").pack(fill=X)
# btn_blue = Button(root, bg="#0000ff").pack(fill=X)
# btn_indigo = Button(root, bg="#4b0082").pack(fill=X)
# btn_violet = Button(root, bg="#ee82ee").pack(fill=X)



root.mainloop()