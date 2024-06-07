from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class Result(Generic[T]):
    def __init__(
        self, 
        value: Optional[T] = None, 
        error: Optional[Exception] = None
    ) -> None:
        if(value is None and error is None):
            raise ValueError("Value and error cannot be both None")
        if(value is not None and error is not None):
            raise ValueError("Value and error cannot be both not None")
        self._value = value
        self._error = error
    
    def is_success(self) -> bool:
        return self._value is not None
    
    def is_error(self) -> bool:
        return self._error is not None

    def unwrap(self) -> T:
        if(self._value is not None):
            return self._value
        raise self._error # type: ignore
    
    def unwrap_or_default(self, default: T) -> T:
        if(self._value is not None):
            return self._value
        return default
        
    @staticmethod
    def success(value: T) -> "Result[T]":
        return Result(value=value)
    
    @staticmethod
    def failure(error: Exception) -> "Result[T]":
        return Result(error=error)
        
