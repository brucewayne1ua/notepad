import tkinter as tk
from tkinter import filedialog
from tkinter import font

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text.delete('1.0', tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text.get('1.0', tk.END))

# Создаем окно
root = tk.Tk()
root.title("Мой блокнот")
root.configure(bg='#1E1E1E')  # Задаем цвет фона окна

# Задаем шрифт и размер текста
font_style = font.Font(family="Bold Italic", size=16)

# Создаем поле для ввода текста
text = tk.Text(root, bg='#1E1E1E', fg='#FFFFFF', insertbackground='#FFFFFF', font=font_style)
text.pack(fill=tk.BOTH, expand=True)

# Создаем меню
menu_bar = tk.Menu(root, bg='#1E1E1E', fg='#FFFFFF')
file_menu = tk.Menu(menu_bar, tearoff=0, bg='#1E1E1E', fg='#FFFFFF')
file_menu.add_command(label="Открыть", command=open_file, background='#1E1E1E', foreground='#FFFFFF')
file_menu.add_command(label="Сохранить", command=save_file, background='#1E1E1E', foreground='#FFFFFF')
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit, background='#1E1E1E', foreground='#FFFFFF')
menu_bar.add_cascade(label="Файл", menu=file_menu)

# Подключаем меню к окну
root.config(menu=menu_bar)

# Запускаем приложение
root.mainloop()