from tkinter import *

def add_str():
    user_input.insert(END, 'Hello!')

def del_str():
    user_input.delete(0, END)

def get_str():
    user_text['text'] = user_input.get()

# рекомендуется называть переменную "root"
root = Tk()
# Размеры и положение появления окна Ширина * Высота + X + Y
root.geometry('600x400+500+300')
# Меняем заголовок окна
root.title('Vproger - check time')
# Меняем иконку окна
root.iconbitmap('python.ico')
#создаем label
label_input = Label(root, text="Поле ввода")
label_input.pack()
#создаем поля ввода
user_input = Entry(root)
# Вставляем текст в поле ввода
# user_input.insert(0, 'Hello')
# user_input.insert(END, ' world')
user_input.pack()
# добавляем кнопки
btn_add = Button(root, text="Add", command=add_str).pack()
btn_del = Button(root, text="Delete", command=del_str).pack()
btn_get = Button(root, text="Get", command=get_str).pack()
# Создаем доп поле(изначально пустое)
user_text = Label(root, bg="#565656", fg="#e0ffff")
user_text.pack(fill=X)

root.mainloop()