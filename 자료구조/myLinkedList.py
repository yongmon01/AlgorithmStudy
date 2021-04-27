class node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = None


class linkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def appen(self, nd):
        if self.head is None:
            self.head = nd
            self.tail = nd
        else:
            self.tail.next_node = nd
            self.tail = nd

    def __str__(self):
        s = ""
        iterate = self.head
        while iterate is not None:
            print(iterate.value)
            s += str(iterate.value) + " "
            iterate = iterate.next_node
        return s

ll = linkedList()
ll.appen(node(1))
ll.appen(node(2))
ll.appen(node(3))
print(ll)