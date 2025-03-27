class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

class SinglyLinkedList:
    def __init__(self, value):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_the_list(self):
        the_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() is not None:
                if current_node.get_next_node() == None:
                    the_list += str(current_node.get_value())
                else:
                    the_list += str(current_node.get_value()) + "->"
            current_node = current_node.get_next_node()
        return the_list
    
    def remove_node(self, value):
        current_node = self.get_head_node()
        if current_node.get_value() == value:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node


#testing out functionality
my_linked_list = SinglyLinkedList(25)
print(my_linked_list.stringify_the_list())
my_linked_list.insert_beginning(24)
print(my_linked_list.stringify_the_list())
my_linked_list.insert_beginning(55)
print(my_linked_list.stringify_the_list())
my_linked_list.insert_beginning(52)
print(my_linked_list.stringify_the_list())
my_linked_list.insert_beginning(22)
print(my_linked_list.stringify_the_list())
my_linked_list.insert_beginning(21)
print(my_linked_list.stringify_the_list())
my_linked_list.remove_node(24)
print(my_linked_list.stringify_the_list())



    