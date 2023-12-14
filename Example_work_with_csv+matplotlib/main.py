# Безклинська В.В. ТВ-21 Варіант 2

#Аналіз відвідування онлайн занять студентами за місяць-два

import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import chardet
import tkinter as tk


class StudentAnalyticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Студентська аналітика")
        self.root.config(bg='#57D9D4')
        self.root.geometry('230x250+450+250')

        # Задати result як атрибут класу
        self.result = None

        self.load_data()

        # Поля вводу для нового студента
        self.label_name = tk.Label(root, text="Ім’я студента:", background= '#57D9D4')
        self.label_name.grid(row =1, column = 1,columnspan =1, pady=10, padx=10)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row =1, column = 2,columnspan =1, pady=10)

        self.label_month = tk.Label(root, text="Місяць:", background= '#57D9D4')
        self.label_month.grid(row =2, column = 1,columnspan =1, pady=5)
        self.entry_month = tk.Entry(root)
        self.entry_month.grid(row =2, column = 2,columnspan =1, pady=5)

        self.label_days = tk.Label(root, text="Кількість днів:", background= '#57D9D4')
        self.label_days.grid(row =3, column = 1,columnspan =1, pady=5)
        self.entry_days = tk.Entry(root)
        self.entry_days.grid(row =3, column = 2,columnspan =1, pady=5)

        # Кнопка для додавання нового студента
        self.add_button = tk.Button(root, text="Додати студента", command=self.add_student, background= '#57D9A8')
        self.add_button.grid(row =4, column = 1,columnspan = 2, pady=5, padx = 10)

        # Кнопка для видалення студента
        self.delete_button = tk.Button(root, text="Видалити студента", command=self.delete_student, background= '#57D9A8')
        self.delete_button.grid(row =5, column = 1,columnspan = 2, pady=5)

        # Кнопка для оновлення візуалізації
        self.update_button = tk.Button(root, text="Оновити візуалізацію", command=self.update_visualization, background= '#57D9A8')
        self.update_button.grid(row =6, column = 1,columnspan = 2, pady=5)

    def load_data(self):
        # Записати дані у CSV
        students_data = [
            ["Іванов Іван", "Вересень", 15],
            ["Іванов Іван", "Жовтень", 20],
            ["Іванов Іван", "Листопад", 20],
            ["Петров Петро", "Вересень", 18],
            ["Петров Петро", "Жовтень", 22],
            ["Петров Петро", "Листопад", 10],
            ["Сидорова Марія", "Вересень", 16],
            ["Сидорова Марія", "Жовтень", 19],
            ["Сидорова Марія", "Листопад", 15],
            ["Безклинська Валерія", "Вересень", 17],
            ["Безклинська Валерія", "Жовтень", 21],
            ["Безклинська Валерія", "Листопад", 16],
            ["Гаркавенко Ольга", "Вересень", 19],
            ["Гаркавенко Ольга", "Жовтень", 12],
            ["Гаркавенко Ольга", "Листопад", 25],
            ["Бондар Руслана", "Вересень", 20],
            ["Бондар Руслана", "Жовтень", 11],
            ["Бондар Руслана", "Листопад", 23],
        ]

        with open("data.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(("Ім’я студента", "Місяць", "Кількість днів"))
            writer.writerows(students_data)

        # Визначити кодування файлу
        with open("data.csv", 'rb') as f:
            self.result = chardet.detect(f.read())

        # Зчитати дані у DataFrame, вказавши кодування
        self.df = pd.read_csv("data.csv", encoding=self.result['encoding'])

    def add_student(self):
        # Отримати дані з полів вводу
        student_name = self.entry_name.get()
        month = self.entry_month.get()
        days_attended = int(self.entry_days.get())

        # Додати нового студента до списку та CSV-файлу
        new_student_data = [student_name, month, days_attended]
        with open("data.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_student_data)

        # Оновити DataFrame
        self.df = pd.read_csv("data.csv", encoding=self.result['encoding'])

        # Оновити візуалізацію
        self.update_visualization()

    def delete_student(self):
        # Отримати дані з полів вводу
        student_name = self.entry_name.get()

        # Видалити студента з CSV-файлу
        # Це фільтрація DataFrame (self.df), де обираються тільки ті рядки, де значення в стовпці 'Ім’я студента' не дорівнює введеному student_name.
        df_filtered = self.df[self.df['Ім’я студента'] != student_name]
        df_filtered.to_csv("data.csv", index=False, encoding=self.result['encoding'])

        # Оновити DataFrame
        self.df = pd.read_csv("data.csv", encoding=self.result['encoding'])

        # Оновити візуалізацію
        self.update_visualization()

    def update_visualization(self):
        # Статистичний аналіз
        #groupby(['Ім’я студента', 'Місяць'])['Кількість днів'].sum():
        # Групує дані за ім'ям студента та місяцем, після чого обчислює суму кількості днів для кожної групи
        #reset_index(): Перетворює індексовані груповані дані в новий DataFrame.
        day_counts = self.df.groupby(['Ім’я студента', 'Місяць'])['Кількість днів'].sum().reset_index()

        # Візуалізація графіку
        # sns.set(style="whitegrid"): Задає стиль графіка.
        # plt.figure(figsize=(12, 6)): Задає розмір фігури для графіка.
        # sns.barplot(...): Створює стовпчатий графік, де x - місяць, y - кількість днів, hue - розділення за ім'ям студента, data - дані для візуалізації,
        # palette - палітра кольорів.
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 6))
        ax = sns.barplot(x='Місяць', y='Кількість днів', hue='Ім’я студента', data=day_counts, palette="viridis")
        plt.title("Кількість днів відвідування студентів за місяцем")
        plt.xlabel("Місяць")
        plt.ylabel("Кількість днів")

        # Розміщення легенди ззовні графіка
        #ax.legend(...): Додає легенду до графіка. bbox_to_anchor вказує на положення легенди (зовні графіка).
        ax.legend(title="Ім’я студента", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()

        plt.show()

# Графічний інтерфейс Tkinter
root = tk.Tk()
app = StudentAnalyticsApp(root)
root.mainloop()




'''students_data = [
    ["Іванов Іван", "Вересень", 15],
    ["Іванов Іван", "Жовтень", 20],
    ["Іванов Іван", "Листопад", 20],
    ["Петров Петро", "Вересень", 18],
    ["Петров Петро", "Жовтень", 22],
    ["Петров Петро", "Листопад", 10],
    ["Сидорова Марія", "Вересень", 16],
    ["Сидорова Марія", "Жовтень", 19],
    ["Сидорова Марія", "Листопад", 15],
    ["Безклинська Валерія", "Вересень", 17],
    ["Безклинська Валерія", "Жовтень", 21],
    ["Безклинська Валерія", "Листопад", 16],
    ["Гаркавенко Ольга", "Вересень", 19],
    ["Гаркавенко Ольга", "Жовтень", 12],
    ["Гаркавенко Ольга", "Листопад", 25],
    ["Бондар Руслана", "Вересень", 20],
    ["Бондар Руслана", "Жовтень", 11],
    ["Бондар Руслана", "Листопад", 23],
]'''


