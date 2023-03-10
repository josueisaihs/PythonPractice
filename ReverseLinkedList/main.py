class LinkedList:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: LinkedList|None = None

    def __repr__(self) -> str:
        return f"LinkedList({self.value})"

    def get_list(self) -> list[int]:
        result = [self.value]
        current = self.next
        while current:
            result.append(current.value)
            current = current.next
        return result


def create_linked_list(arr: list[int]) -> LinkedList:
    head = LinkedList(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = LinkedList(arr[i])
        current = current.next
    return head

def reverse_linked_list(head: LinkedList) -> LinkedList:
    current = head
    previous: LinkedList|None = None
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
        
    return previous

def reverse_linked_list_recursive(head: LinkedList) -> LinkedList:
    if not head or not head.next:
        return head
    
    new_head = reverse_linked_list(head.next)
    
    head.next.next = head
    head.next = None
    
    return new_head
