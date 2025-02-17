from collections import deque

class Printer():
    def __init__(self) -> None:
        self.queue: deque[tuple[str, str]] = deque()

    def enqueue(self, file: str, element: str) -> None:
        self.queue.append((file, element))

    def print_next(self) -> None:
        print(self.queue.popleft())

    def print_all(self) -> None:
        while self.queue:
            self.print_next()




printer = Printer()
printer.enqueue("tabulka.xls", "Karel")
printer.enqueue("referat.docx", "Lida")
printer.enqueue("dovolena.jpeg", "Rudolf")

printer.print_all()
