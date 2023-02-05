import sqlite3
from customer import Customer


class CustomerBTreeType:
    def __init__(self):
        self.customers = []
        self.left = None
        self.right = None
        self.data = self.customers

    def load_customer_detail(self):
        try:
            a = Customer()
            db_connection = sqlite3.connect("customer_data.db")
            sql_query = "SELECT * FROM customer;"
            cursor = db_connection.cursor()
            cursor.execute(sql_query)
            customer_record = cursor.fetchall()
            print(customer_record)
            for customer in customer_record:
                first_name = customer[1]
                last_name = customer[2]
                account_number = customer[0]
                list_of_dvd = customer[3]
                new_customer = Customer(first_name, last_name, account_number, list_of_dvd)
                self.customers.append(new_customer)
                a.merge_sort(self.customers)


        except sqlite3.Error as error:
            print(f"An error has occurred: Please contact the DB administrator")
        finally:
            if db_connection:
                db_connection.close()


class Node(CustomerBTreeType):
    def __init__(self, data):
        self.data = self.customers
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert((value, self.root))

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)

        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left_child)
            print(current_node.value)
            self._print_tree(current_node.right_child)
