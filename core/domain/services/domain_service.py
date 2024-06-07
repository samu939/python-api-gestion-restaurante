from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")
R = TypeVar("R")

class DomainService(ABC, Generic[T, R]):
    @abstractmethod
    def execute(self, input: T) -> R:
        pass