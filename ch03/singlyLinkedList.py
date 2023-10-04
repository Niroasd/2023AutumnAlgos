class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList: (contains {self._size} element{plural}): [{values.lstrip(", ")}]>'
    
    def __len__(self):
        return self._size
     
    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if self._tail is None:
            self._head = self._tail = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            self._tail.next = node
            self._tail = node

        self._size += 1
            
    def pop(self):

        #if empty return none
        if self._head is None:
            return None
        

        #removing a single element list
        if self._head.next is None:
            val = self._head.data
            del self._head
            self._head = None
            return val

        
        current_node = self._head
        val = self._tail.data
        
        valueToDelete = self._tail
        del(valueToDelete)

        while current_node.next != None:
            secondLast = current_node
            current_node = current_node.next


        
        self._tail = secondLast

        return val

list = SinglyLinkedList()
for i in 'abcfkgdgm':
    list.append(i)

print(list._tail.data)
val = list.pop()
print(val, list)