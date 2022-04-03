from tkinter import *
import platform

root = Tk()
root.geometry('800x600+800+300') # размеры
root.title('Текстовый редактор') #Заголовок

main_menu = Menu(root)
root.config(menu=main_menu)

#File
file_nemu = Menu(main_menu, tearoff=0) # tearoff - открепление от расположения 1 - да 0 нет
file_nemu.add_command(label="Открыть")
file_nemu.add_command(label="Сохранить")
file_nemu.add_separator() #разделитель
file_nemu.add_command(label="Выход")

main_menu.add_cascade(label="Файл", menu=file_nemu)

#About
help_menu = Menu(main_menu, tearoff=0)

help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label="Онлайн")
help_menu_sub.add_command(label="Офлайн")

help_menu.add_cascade(label="Помощь", menu=help_menu_sub)
help_menu.add_command(label="О программе")
main_menu.add_cascade(label="Справка", menu=help_menu)


if(platform.system() != 'Linux'):
    root.iconbitmap('practic/tx_sc/tx.ico') #иконка
else:  
    root.iconbitmap('@practic/tx_sc/tx.xbm') #иконка

frame_text = Frame(root)
frame_text.pack(fill=BOTH, expand=1)


text_area = Text(frame_text, bg="#343D46", fg="#C6DEC1", padx=10, pady=10, wrap="word", insertbackground="#EDA756", selectbackground="#4E5A65", width=30, spacing3=10)
text_area.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_text, command=text_area.yview)
scroll.pack(fill=Y, side=LEFT)
text_area.config(yscrollcommand=scroll.set)

root.mainloop()