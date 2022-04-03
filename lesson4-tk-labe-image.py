from tkinter import *

# рекомендуется называть переменную "root"
root = Tk()
# Размеры и положение появления окна Ширина * Высота + X + Y
root.geometry('600x400+500+300')
# Меняем заголовок окна
root.title('Vproger - check time')
# Меняем иконку окна
root.iconbitmap('python.ico')
# Создаем объект для картинки
img = PhotoImage(file='my-image.png')
# Изменение размера изображения
img_res = img.subsample( 10 , 10 )
# Создаем label для картинки
l_logo = Label(root, image=img_res)

# размещаем в окне
l_logo.pack()

root.mainloop()