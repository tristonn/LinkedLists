class UniDirNode:
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
        self.head_node = UniDirNode(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, value):
        new_node = UniDirNode(value)
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

class BiDirNode:
    def __init__(self, value, prev_node = None, next_node = None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def get_prev_node(self):
        return self.prev_node
    
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, value):
        new_head_node = BiDirNode(value)
        current_head_node = self.head_node

        if current_head_node is not None:
            current_head_node.set_prev_node(new_head_node)
            new_head_node.set_next_node(current_head_node)

        self.head_node = new_head_node

        if self.tail_node is None:
            self.tail_node = new_head_node

    def add_to_tail(self, value):
        new_tail = BiDirNode(value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
        
        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    def remove_head(self):
        removed_head = self.head_node

        if removed_head == None:
            return None

        self.head_node = removed_head.get_next_node()

        if self.head_node != None:
            self.head_node.set_prev_node(None)

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail == None:
            return None

        self.tail_node = removed_tail.get_prev_node()

        if self.tail_node != None:
            self.tail_node.set_next_node(None)

        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail.get_value()


    