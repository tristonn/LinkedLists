class Node:
    def __init__(self, value, link_node = None):
        self.value = value
        self.link_node = link_node

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_link_node(self, link_node):
        self.link_node = link_node



    