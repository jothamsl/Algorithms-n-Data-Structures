"""
Like arrays, linked list is a linear data structure. Unlike arrays,
linked lists are not stored at a contiguous location; the elements
are linked using pointers
"""

# Define a node class (Instance of linked lists' elements)
class Node:
    """
    Node
    ----
    Single element of a linked list
    """
    # Initializes the Node object

    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize value next to it as NULL

# Define Linked list 
class Linkedlist:
    """
    Linkedlist
    ----------
    The Linked list Data structure 
    """
    # Initializes the linked list object

    def __init__(self):
        self.head = None


if __name__ == "__main__":
    # Simple linked list with 3 nodes
    llist = Linkedlist()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    ''' 
    Three nodes have been created. 
    We have references to these three blocks as head, 
    second and third 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  | None |     | 2  | None |     |  3 | None | 
    +----+------+     +----+------+     +----+------+ 
    '''

    llist.head.next = second  # Link first node with second

    ''' 
    Now next of first Node refers to second.  So they 
    both are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | null |     |  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''

    second.next = third  # Link second node with the third node

    ''' 
    Now next of second Node refers to third.  So all three 
    nodes are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''

