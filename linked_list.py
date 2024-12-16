class Head:
    def __init__(self) -> None:
        self.next: Elem | None = None

class Elem(Head):
    def __init__(self, value, next) -> None:
        self.next: Elem | None = next
        self.value: int = value

class Linked_list:
    def __init__(self) -> None:
        self.head: Head = Head()


    def prepend(self, elem_to_insert: int) -> None:
        if self.is_empty():
            self.head.next = Elem(elem_to_insert, None)
        else:
            self.head.next = Elem(elem_to_insert, self.head.next)

    def print_all(self, node: Elem = None) -> None:
        if not node:
            print("list: ")
            print("[", end='')
            node = self.head

        if self.is_empty():
            raise Exception("prazdny seznam")


        if not node.next:
            print(str(node.value) + "]")
            return

        if not node is self.head:
            print(str(node.value) + ", ", end='')

        self.print_all(node.next)



    def pop_last(self) -> None:
        if self.is_empty():
            raise Exception("prazdny seznam")

        curr_elem: Elem = self.head.next
        if not curr_elem.next:
            self.head.next = None
            return
        next: Elem = curr_elem.next
        while next.next:
            curr_elem = next
            next = next.next
        curr_elem.next = None

    def is_empty(self) -> bool:
        if not self.head.next:
            return True
        return False

    def insert(self, elem_to_insert: int, index: int) -> None:
        preceding_elem = self.go_to_elem(index-1)
        next_elem = preceding_elem.next
        if not next_elem:
            preceding_elem.next = Elem(elem_to_insert, None)
        else:
            preceding_elem.next = Elem(elem_to_insert, preceding_elem.next)

    def go_to_elem(self, index: int) -> Elem:
        if self.is_empty():
            raise Exception("prazdny seznam")

        curr_elem: Elem = self.head.next
        for i in range(index):
            if not curr_elem.next:
                raise Exception("index out of bounds")
            curr_elem = curr_elem.next
        return curr_elem

    def get(self, index: int) -> int:
        return self.go_to_elem(index).value


list = Linked_list()

list.prepend(3)
list.prepend(2)
list.prepend(5)
list.print_all()
list.insert(10, 2)
list.print_all()
list.pop_last()
list.print_all()
