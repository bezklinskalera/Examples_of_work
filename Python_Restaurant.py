class Python_Restaurant:

    class Customers_orders:

        def __init__(self, number, food):
            self.number=number
            self.food=food

    class Menu_items:

        def __init__(self, name, category, price):
            self.name = name
            self.category = category
            self.price = price

    def __init__(self, menu_items=None, booked_tables=None, customer_orders=None):
        if menu_items is None:
            menu_items = []
        if booked_tables is None:
            booked_tables = []
        if customer_orders is None:
            customer_orders = []

        self.menu_items = menu_items
        self.booked_tables = booked_tables
        self.customer_orders = customer_orders

    def add_item_to_menu(self, name, category, price):
        new_item = self.Menu_items(name, category, price)
        self.menu_items.append(new_item)

    def print_menu(self):
        menu_text = "Меню:"
        for item in self.menu_items:
            menu_text += f"\n{item.name} ({item.category}) - ${item.price}"
        return menu_text

    def print_orders(self):
        order_text = "Доступні замовлення:"
        for item in self.customer_orders:
            order_text += f"\nСтолик {item.number} ({item.food})"
        return order_text

    def add_item_order(self,number,food):
        new_item = self.Customers_orders(number, food)
        self.customer_orders.append(new_item)
