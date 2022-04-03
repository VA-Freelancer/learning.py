from tkinter import *
import platform

root = Tk()
root.geometry('800x600+800+300') # размеры
root.title('Текстовый редактор') #Заголовок
if(platform.system() != 'Linux'):
    root.iconbitmap('practic/tx_sc/tx.ico') #иконка windows
else:  
    root.iconbitmap('@practic/tx_sc/tx.xbm') #иконка linux


frame_menu = Frame(root, bg="#1F252A", height=40)
frame_text = Frame(root)
frame_menu.pack(fill=X)
frame_text.pack(fill=BOTH, expand=1)

def add_str():
    text_area.insert('2.4', 'Hello!')

def del_str():
    text_area.delete('2.4', '2.10')

def get_str():
    print(text_area.get('1.0', END))

btn_add = Button(root, text="Add", command=add_str).place(x=50, y=10)
btn_del = Button(root, text="Delete", command=del_str).place(x=90, y=10)
btn_get = Button(root, text="Get", command=get_str).place(x=140, y=10)

label_menu = Label(frame_menu, text="Menu", bg="#2B3239", fg="#C6DEC1", font="Arial 10")
label_menu.place(x=10, y=10)
text_area = Text(frame_text, bg="#343D46", fg="#C6DEC1", padx=10, pady=10, wrap="word", insertbackground="#EDA756", selectbackground="#4E5A65", width=30, spacing3=10)
text_area.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_text, command=text_area.yview)
scroll.pack(fill=Y, side=LEFT)
text_area.config(yscrollcommand=scroll.set)

root.mainloop()