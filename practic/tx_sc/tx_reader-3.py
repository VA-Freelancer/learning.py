from tkinter import *
import platform

root = Tk()
root.geometry('800x600+800+300') # размеры
root.title('Текстовый редактор') #Заголовок

main_menu = Menu(root)
root.config(menu=main_menu)

main_menu.add_command(label="File")
main_menu.add_command(label="About")

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