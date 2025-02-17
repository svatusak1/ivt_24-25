from __future__ import annotations
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum

class Uzel:
    @abstractmethod
    def eval(self):
        ...

class Uoperace(Uzel):
    def __init__(self, left, right) -> None:
        self.left: Uzel = left
        self.right: Uzel = right

    @abstractmethod
    def eval(self):
        ...

class Ukratoperace(Uoperace):
    def eval(self) :
        return self.left.eval() * self.right.eval()

class Udelenooperace(Uoperace):
    def eval(self) -> float:
        return self.left.eval() / self.right.eval()
        


class Uplusoperace(Uoperace):
    def eval(self) -> float:
        return self.left.eval() + self.right.eval()


class Uminusoperace(Uoperace):
    def eval(self) -> float:
        return self.left.eval() - self.right.eval()



class Ulist(Uzel):
    def __init__(self, hodnota) -> None:
        self.hodnota: int = hodnota

    def eval(self) -> int:
        return self.hodnota

tri = Ulist(3)
dva = Ulist(2)
plus = Uplusoperace(tri, dva)
devet = Ulist(9)
krat = Ukratoperace(plus, devet)



print(krat.eval())


