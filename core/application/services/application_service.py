from typing import Generic, TypeVar, Awaitable
from abc import ABC, abstractmethod
from ..results.result_wrapper import Result

T = TypeVar("T")
R = TypeVar("R")

class ApplicationService(ABC, Generic[T, R]):
    @abstractmethod
    def execute(self, input: T) -> Awaitable[Result[R]]:
        pass