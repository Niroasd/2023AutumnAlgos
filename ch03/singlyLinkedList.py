class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f'<ListNode: {self.data}>'



class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def append(self, value):
        """
        Append a value to the end of the list
        Parameters:
        - 'value': The data to append
        Returns: None
        """
        # Create the node with the given value
        node = ListNode(value, next=None)
        # If list is empty just point the header to the new node
        if self._head is None:
            self._head = node
        else:
        # if list is not empty, locate the last element and point it to the new node
            current_node = self._head

            while current_node.next != None:
                current_node = current_node.next
                current_node.next = node

    def pop(self):
        pass


    def __repr__(self):
        current_node = self._head
        values = ''

        while current_node:
            values += f', {current_node.data}'

            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'


list = SinglyLinkedList()
for i in 'abc':
    list.append(i)
val = list.pop()
print(val, list)