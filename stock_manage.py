import datetime


class Stock:
    def __init__(self, stock_name, stock_initial_quantity,
                 stock_price_per_unit):
        self.stock_name = stock_name
        self.stock_initial_quantity = stock_initial_quantity
        self.stock_price_per_unit = stock_price_per_unit
        # self.notification_threshold = notification_threshold  # This attribute will take the threshold limit to warn the user

    def add_new_quantity_stock(self, quantity_to_add):
        self.stock_initial_quantity += quantity_to_add
        return f"you added {quantity_to_add} of {self.stock_name} and the new quantity is {self.stock_initial_quantity}"

    def remove_quantity_stock(self, quantity_to_remove):
        if quantity_to_remove > self.stock_initial_quantity:
            return f"there is {self.stock_initial_quantity} a quantity of this stock " \
                   f"and you want to remove {quantity_to_remove}, which is impossible because the stock quantity cannot be negative"
        self.stock_initial_quantity -= quantity_to_remove
        return f"you removed {quantity_to_remove} of {self.stock_name} and the new quantity is {self.stock_initial_quantity} "

    def total_value_of_specific_stock(self):
        return f"Total of {self.stock_name} is: {self.stock_initial_quantity * self.stock_price_per_unit}€"

    # converting our objects to str
    def __str__(self):
        return f"(Stock_name='{self.stock_name}', Stock_quantity={self.stock_initial_quantity}, Stock_price={self.stock_price_per_unit})"

    # storage of objects in a dictionary
    def to_dict(self):
        return {
            'stock_name': self.stock_name,
            'stock_initial_quantity': self.stock_initial_quantity,
            'stock_price_per_unit': self.stock_price_per_unit
        }

    # Notification to send when a stock threshold is achieved
    def send_notification(self):
        return f"The stock level of {self.stock_name} is low. There are {self.stock_initial_quantity} units left."


class StockManager:
    def __init__(self):
        self.stock_list = []

    def add_stock_to_list_stock(self, stock_to_add):
        return self.stock_list.append(stock_to_add)

    def remove_stock_to_list_stock(self, stock_to_remove):
        return self.stock_list.remove(stock_to_remove)

    # This method returns the total amount of all stocks in €
    def get_total_value_stock(self):
        total_value = sum(stock.stock_initial_quantity * stock.stock_price_per_unit for stock in self.stock_list)
        return f"Total stocks value is : {total_value}€ "

    # This method returns the dictionary of all available stocks
    def get_stock_list(self):  # sourcery skip: dict-comprehension
        stock_dict = {}
        for stock in self.stock_list:
            stock_dict[stock.stock_name] = \
                {
                    "Total Quantity": stock.stock_initial_quantity,
                    "price per unit(€)": stock.stock_price_per_unit
                }
        return stock_dict


class SalesTracker:
    def __init__(self):
        self.sales_history = []

    def stock_sold(self, stock_name, quantity_sold, price_per_unit, date_of_sale=datetime.datetime.now()):
        sale = {
            'stock_name': stock_name,
            'quantity sold': quantity_sold,
            'price_per_unit': price_per_unit,
            'total_price_sold': quantity_sold * price_per_unit,
            'date_of_sale': date_of_sale
        }
        self.sales_history.append(sale)

    def get_sales_history(self):
        return self.sales_history

    def get_sales_by_stock(self, stock_name):
        return [sale for sale in self.sales_history if sale['stock_name'] == stock_name]

    def get_total_sales(self):
        return f"Total of sales : {sum(sale['total_price_sold'] for sale in self.sales_history)}€"
