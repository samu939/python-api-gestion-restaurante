from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")

class ValueObject(ABC, Generic[T]):
    def __init__(self, value: T):
        self.value = value
        super().__init__()

    @abstractmethod
    def equals(self, other: "ValueObject[T]") -> bool:
        pass
