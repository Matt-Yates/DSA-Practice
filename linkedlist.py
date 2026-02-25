# Practice creating and using data structures and algorithms to refresh my memory
#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)


    def traverse(self):
        if self.head == None:
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("End of list\n")

    def pop(self):
        if self.head == None:
            return
        if not self.head.next:
            self.head = None
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        #print("Removed the last node in the list\n")
        return

    def push(self, data):
        
        if self.head == None:
            self.head = Node(data)
            return

        if self.head.next == None:
            self.head.next = Node(data)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        #print(f"Added {data} to the end of the list\n")
        return


