import sqlite3


def split(customers):
    if customers is None or customers.head is None:
        left_half = customers
        right_half = None
        return left_half, right_half
    else:
        size = customers.size()
        mid = size // 2
        mid_node = customers.node_at_index(mid - 1)
        left_half = customers
        right_half = Customer()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        return left_half, right_half


def merge(left, right):
    merged = Customer()
    merged.add(0)
    current = merged.head
    left_head = left.head
    right_head = right.head
    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
            current = current.next_node
        head = merged.head.next_node
        merged.head = head

        return merged


class Customer:
    def __init__(self, first_name="", last_name="", account_number="", list_of_dvd_rented=""):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.list_of_dvd_rented = list_of_dvd_rented

    def merge_sort(self, customers):
        if len(customers) == 1:
            return customers
        elif customers.head is None:
            return customers

        left_half, right_half = split(customers)
        left = self.merge_sort(left_half)
        right = self.merge_sort(right_half)

        return merge(left, right)

    def __str__(self):
        output = f"{self.first_name}{self.last_name}({self.account_number}) is rented {self.list_of_dvd_rented} from the store"
        return output


"""class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None"""

"""class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert((value, self.root))

    def _insert(self,value,current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._insert(value,current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(value,current_node.right_child)

        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self,current_node):
        if current_node is not None:
            self._print_tree(current_node.left_child)
            print(current_node.value)
            self._print_tree(current_node.right_child)

tree = BinarySearchTree()
tree.print_tree()"""
