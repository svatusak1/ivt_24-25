from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

@dataclass
class Uzel:
    hodnota: str
    left: Uzel | None = None
    right: Uzel | None = None

tri = Uzel("3")
dva = Uzel("2")
plus = Uzel("+", tri, dva)

def tisk(n: Uzel) -> None:
    if n.left is None:
        print(n.hodnota)
    else:
        print(n.hodnota)
        tisk(n.left)
        tisk(n.right)

tisk(plus)


