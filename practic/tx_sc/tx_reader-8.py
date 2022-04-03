from tkinter import *
import platform
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.geometry('800x600+800+300')  # размеры
root.title('Текстовый редактор')  # Заголовок


# функкции тестовая
def about_programm():
    messagebox.showinfo(title='About notepad', message='Программа Notepad 0.0.1')


def quit_programm():
    answer = messagebox.askokcancel(title="Выход", message='Закрыть программу')
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title="ВЫбор файла",
                                           filetypes=(("Тектовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))
    if file_path:
        text_area.delete('1.0', END)
        my_text = open(file_path, encoding='utf-8').read()
        text_area.insert('1.0', my_text)


def save_file():
    file_path = filedialog.asksaveasfilename(title="Сохранить файл", defaultextension=".txt",
                                             filetypes=(("Тектовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))
    my_text = open(file_path, "w", encoding="utf-8")
    text = text_area.get('1.0', END)
    my_text.write(text)
    my_text.close()


def change_theme(theme):
    text_area["bg"] = theme_colors[theme]['text_bg']
    text_area["fg"] = theme_colors[theme]['text_fg']
    text_area["insertbackground"] = theme_colors[theme]['cursor']
    text_area["selectbackground"] = theme_colors[theme]['select_bg']


main_menu = Menu(root)
root.config(menu=main_menu)

# File
file_nemu = Menu(main_menu, tearoff=0)  # tearoff - открепление от расположения 1 - да 0 нет
file_nemu.add_command(label="Открыть", command=open_file)
file_nemu.add_command(label="Сохранить", command=save_file)
file_nemu.add_separator()  # разделитель
file_nemu.add_command(label="Выход", command=quit_programm)

main_menu.add_cascade(label="Файл", menu=file_nemu)

# Theme
theme_menu = Menu(main_menu, tearoff=0)

theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label="Светлая тема", command=lambda: change_theme('light'))
theme_menu_sub.add_command(label="Темная тема", command=lambda: change_theme('dark'))

theme_menu.add_cascade(label="Оформление", menu=theme_menu_sub)
theme_menu.add_command(label="О Программе", command=about_programm)
main_menu.add_cascade(label="Разное", menu=theme_menu)

if (platform.system() != 'Linux'):
    root.iconbitmap('tx.ico')  # иконка
else:
    root.iconbitmap('@tx.xbm')  # иконка

frame_text = Frame(root)
frame_text.pack(fill=BOTH, expand=1)

theme_colors = {
    "dark": {
        "text_bg": "#343D46", "text_fg": "#fff", "cursor": "#EDA756", "select_bg": "#4E5A65"
    },
    "light": {
        "text_bg": "#fff", "text_fg": "#000", "cursor": "#8000FF", "select_bg": "#777"
    }
}

text_area = Text(frame_text, bg=theme_colors["dark"]["text_bg"], fg=theme_colors["dark"]["text_fg"], padx=10, pady=10,
                 wrap="word", insertbackground=theme_colors["dark"]["cursor"],
                 selectbackground=theme_colors["dark"]["select_bg"], width=30, spacing3=10, font=("Courier New", "11"))
text_area.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_text, command=text_area.yview)
scroll.pack(fill=Y, side=LEFT)
text_area.config(yscrollcommand=scroll.set)

root.mainloop()
