from linked_list_intro import Node, Linkedlist


class LL(Linkedlist):

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    # Start with an empty list
    llist = LL()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second  # Link first node with second
    second.next = third  # Link second node with third

    llist.printList()
