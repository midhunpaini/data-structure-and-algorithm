from singly_linked_list import Node,LinkedList

# removing duplictes from singly linked list





linked_list = LinkedList()

linked_list.append(5)
linked_list.append(10)
linked_list.append(5)
linked_list.append(8)
linked_list.append(6)
linked_list.append(8)
linked_list.append(5)
linked_list.display()

def remove_dup():
    s = set()
    current  = linked_list.head
    while current:
        if current.data not in s:
            print('adding', current.data,)
            s.add(current.data)
        else:
            print('removing', current.data)
            linked_list.delete(current.data)
        current = current.next
print()
remove_dup()
print("Head: ", linked_list.head.data)
print("Tail: ", linked_list.tail.data)
linked_list.display()