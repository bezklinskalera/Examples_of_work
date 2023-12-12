import tkinter as tk
from tkinter import ttk
from Python_Restaurant import *

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Ресторан Python')
        self.root.config(bg='#D6F5B6')
        self.root.geometry('420x200+450+250')
        self.root.resizable(False, False)

        self.custom_font = ('Courier New', 9)

        self.available_table = {1: False, 2: True, 3: True, 4: True,
                       5: True, 6: False}

        self.client_orders = []

        self.restaurant = Python_Restaurant()
        self.restaurant.add_item_to_menu("Сік", "Безалкогольні напої", 100)
        self.restaurant.add_item_to_menu("Борщ", "Основні страви", 200)

        self.label_1 = tk.Label(self.root, text='''Вас вітає Python Restaurant!
        Оберіть пункт меню, який вас цікавить.''',
                                background='#D6F5B6',
                                foreground='#363833',
                                font=self.custom_font,
                                pady=30,
                                padx=20,
                                relief=tk.RAISED,
                                bd=10)
        self.label_1.grid(row=0,column=0, columnspan=2 )

        self.btn1 = tk.Button(self.root, text='Додати пункт до меню', command=self.add_item_gui,font=self.custom_font,activebackground='#2F6B56')
        self.btn1.grid(row=1,column=0, stick = 'we')

        self.btn2 = tk.Button(self.root, text='Прийняти замовлення', command=self.customer_order_gui,font=self.custom_font,activebackground='#2F6B56')
        self.btn2.grid(row=1,column=1, stick = 'we')

        self.btn3 = tk.Button(self.root, text='Надрукувати меню', command=self.add_label,font=self.custom_font,activebackground='#2F6B56')
        self.btn3.grid(row=2,column=0, stick = 'we')

        self.btn4 = tk.Button(self.root, text='Скасувати бронювання столика', command=self.show_booked_tables_gui,font=self.custom_font,activebackground='#2F6B56')
        self.btn4.grid(row=2,column=1, stick = 'we')

        self.btn5 = tk.Button(self.root, text='Подивитися доступні столики', command=self.show_available_tables_gui,font=self.custom_font,activebackground='#2F6B56')
        self.btn5.grid(row=3,column=0, stick = 'we')

        self.btn6 = tk.Button(self.root, text='Надрукувати замовлення клієнта', command=self.print_client_order,font=self.custom_font,activebackground='#2F6B56')
        self.btn6.grid(row=3,column=1, stick = 'we')

        self.root.mainloop()

    def show_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label_1 = tk.Label(self.root, text='''Вас вітає Python Restaurant!
        Оберіть пункт меню, який вас цікавить.''',
                                background='#D6F5B6',
                                foreground='#363833',
                                font=self.custom_font,
                                pady=30,
                                padx=20,
                                relief=tk.RAISED,
                                bd=10)
        self.label_1.grid(row=0,column=0, columnspan=2 )

        self.btn1 = tk.Button(self.root, text='Додати пункт до меню', command=self.add_item_gui,font=self.custom_font,activebackground='#2F6B56')
        self.btn1.grid(row=1,column=0, stick = 'we')

        self.btn2 = tk.Button(self.root, text='Прийняти замовлення', command=self.customer_order_gui,font=self.custom_font,activebackground='#2F6B56')
        self.btn2.grid(row=1,column=1, stick = 'we')

        self.btn3 = tk.Button(self.root, text='Надрукувати меню', command=self.add_label,font=self.custom_font,activebackground='#2F6B56')
        self.btn3.grid(row=2,column=0, stick = 'we')

        self.btn4 = tk.Button(self.root, text='Скасувати бронювання столика', command=self.show_booked_tables_gui,font=self.custom_font,activebackground='#2F6B56')
        self.btn4.grid(row=2,column=1, stick = 'we')

        self.btn5 = tk.Button(self.root, text='Подивитися доступні столики', command=self.show_available_tables_gui,font=self.custom_font,activebackground='#2F6B56')
        self.btn5.grid(row=3,column=0, stick = 'we')

        self.btn6 = tk.Button(self.root, text='Надрукувати замовлення клієнта', command=self.print_client_order,font=self.custom_font,activebackground='#2F6B56')
        self.btn6.grid(row=3,column=1, stick = 'we')

    def add_item_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        label_2 = tk.Label(self.root, text="Введіть назву пункту меню:",
                           background='#D6F5B6',
                           foreground='#363833',
                           font=self.custom_font)
        label_2.grid(row=0, column=0, columnspan=2, stick='we')

        item_menu = tk.Entry(self.root)
        item_menu.grid(row=0, column=2, columnspan=2, stick='we')

        label_3 = tk.Label(self.root, text="Введіть категорію:",
                           background='#D6F5B6',
                           foreground='#363833',
                           font=self.custom_font)
        label_3.grid(row=1, column=0, columnspan=2, stick='we')

        category_menu = tk.Entry(self.root)
        category_menu.grid(row=1, column=2, columnspan=2, stick='we')

        label_4 = tk.Label(self.root, text="Введіть ціну:",
                           background='#D6F5B6',
                           foreground='#363833',
                           font=self.custom_font)
        label_4.grid(row=2, column=0, columnspan=2, stick='we')

        price_menu = tk.Entry(self.root)
        price_menu.grid(row=2, column=2, columnspan=2, stick='we')

        def ready_label():
            value1 = item_menu.get()
            value2 =category_menu.get()
            value3 =price_menu.get()
            self.restaurant.add_item_to_menu(value1,value2,value3)

            label_4 = tk.Label(self.root, text="Додано до меню!",
                               background='#D6F5B6',
                               foreground='#363833',
                               font=self.custom_font)
            label_4.grid(row=3, column=0, columnspan=2, stick='we')

        ready_button = tk.Button(self.root, text='Підтвердити', command=ready_label ,
                                font=self.custom_font, activebackground='#2F6B56')
        ready_button.grid(row=4, column=2, columnspan=2, stick='we')

        back_button = tk.Button(self.root, text='Повернутися до головного екрану', command=self.show_main_screen,
                                font=self.custom_font, activebackground='#2F6B56')
        back_button.grid(row=5, column=2)

    def add_label(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        menu_text = self.restaurant.print_menu()
        label_2 = tk.Label(self.root, text=menu_text,
                           background='#D6F5B6',
                           foreground='#363833',
                           font=self.custom_font,
                           pady=30,
                           padx=20,
                           relief=tk.RAISED,
                           bd=10)
        label_2.grid(row=0,column=0, columnspan=2,stick = 'we')
        back_button = tk.Button(self.root, text='Повернутися до головного екрану', command=self.show_main_screen,font=self.custom_font,activebackground='#2F6B56')
        back_button.grid(row=1,column=0, columnspan=2, stick = 'we')

    def customer_order_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        label_1 = tk.Label(self.root, text="Введіть номер столика",
                           background='#D6F5B6',
                           foreground='#363833',
                           font=self.custom_font)
        label_1.grid(row=0, column=0, columnspan=2, stick='we')

        client_table= tk.Entry(self.root)
        client_table.grid(row=0, column=2, columnspan=2, stick='we')

        label_2 = tk.Label(self.root, text="Що бажаєте замовити?"
                                           "\n (перелік через кому)",
                           background='#D6F5B6',
                           foreground='#363833',
                           font=self.custom_font)
        label_2.grid(row=1, column=0, columnspan=2, stick='we')

        client_order = tk.Entry(self.root)
        client_order.grid(row=1, column=2, columnspan=2, stick='we')

        def new_order():
            value_table = client_table.get()
            try:
                number = int(value_table)
                if 1 <= number <= 6:
                    value_order = client_order.get()
                    self.restaurant.add_item_order(value_table, value_order)
                    label_1 = tk.Label(self.root, text="Дякуємо за замовлення!",
                                       background='#D6F5B6',
                                       foreground='#363833',
                                       font=self.custom_font)
                    label_1.grid(row=2, column=0, columnspan=2, stick='we')
                else:
                    label_1 = tk.Label(self.root, text="Число має бути від 1-6!",
                                       background='#D6F5B6',
                                       foreground='#363833',
                                       font=self.custom_font)
                    label_1.grid(row=2, column=0, columnspan=2, stick='we')
            except ValueError:
                label_1 = tk.Label(self.root, text="Значення має бути числом",
                                   background='#D6F5B6',
                                   foreground='#363833',
                                   font=self.custom_font)
                label_1.grid(row=2, column=0, columnspan=2, stick='we')

        back_button = tk.Button(self.root, text='Підтвердити', command=new_order,
                                font=self.custom_font, activebackground='#2F6B56')
        back_button.grid(row=3, column=2)

        back_button = tk.Button(self.root, text='Повернутися до головного екрану', command=self.show_main_screen,
                                font=self.custom_font, activebackground='#2F6B56')
        back_button.grid(row=4, column=2)

    def print_client_order(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        order_text = self.restaurant.print_orders()
        label_2 = tk.Label(self.root, text=order_text,
                           background='#D6F5B6',
                           foreground='#363833',
                           font=self.custom_font,
                           pady=30,
                           padx=20,
                           relief=tk.RAISED,
                           bd=10)
        label_2.grid(row=0, column=0, columnspan=2, stick='we')
        back_button = tk.Button(self.root, text='Повернутися до головного екрану', command=self.show_main_screen,
                                font=self.custom_font, activebackground='#2F6B56')
        back_button.grid(row=len(self.client_orders) + 2, column=1)

    def show_available_tables_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        label_1 = tk.Label(self.root, text="Вільні столики (Натискайте для бронювання)",
                           background='#D6F5B6',
                           foreground='#363833',
                           font=self.custom_font)
        label_1.grid(row=0, column=0, columnspan=2, stick='we')

        for table, available in self.available_table.items():
            row_position = table
            if available:
                btn_text = f'Столик {table}'
                btn_command = lambda t=table: self.book_table(t)
            else:
                btn_text = 'Заброньовано'
                btn_command = None

            btn = tk.Button(self.root, text=btn_text,
                            command=btn_command,
                            font=self.custom_font, activebackground='#2F6B56')
            if not available:
                btn.config(state=tk.DISABLED)

            btn.grid(row=row_position, column=1, columnspan=2, stick='we')

        back_button = tk.Button(self.root, text='Повернутися до головного екрану', command=self.show_main_screen,
                                font=self.custom_font, activebackground='#2F6B56')
        back_button.grid(row=len(self.available_table) + 1, column=1)

    def book_table(self, table_id):
        if self.available_table[table_id]:
            self.available_table[table_id] = False
            self.show_available_tables_gui()

    def cancel_booking(self, table_id):
        if not self.available_table[table_id]:
            self.available_table[table_id] = True
            self.show_booked_tables_gui()

    def show_booked_tables_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        label_1 = tk.Label(self.root, text="Заброньовані столи (Натискайте для відміни)",
                           background='#D6F5B6',
                           foreground='#363833',
                           font=self.custom_font)
        label_1.grid(row=0, column=0, columnspan=2, stick='we')

        for table, available in self.available_table.items():
            row_position = table
            if not available:
                btn_text = f'Столик {table}'
                btn_command = lambda t=table: self.cancel_booking(t)
            else:
                btn_text = 'Вільно'
                btn_command = None

            btn = tk.Button(self.root, text=btn_text,
                            command=btn_command,
                            font=self.custom_font, activebackground='#2F6B56')
            if available:
                btn.config(state=tk.DISABLED)

            btn.grid(row=row_position, column=1, columnspan=2, stick='we')

        back_button = tk.Button(self.root, text='Повернутися до головного екрану', command=self.show_main_screen,
                                font=self.custom_font, activebackground='#2F6B56')
        back_button.grid(row=len(self.available_table) + 1, column=1)