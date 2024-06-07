from typing import Callable, Awaitable
from abc import ABC, abstractmethod
from src.core.domain.events.domain_event import DomainEvent

class EventHandler(ABC):
    @abstractmethod
    def publish_events(self, events: list[DomainEvent]) -> None:
        pass

    @abstractmethod
    def subscribe(
        self, 
        event: DomainEvent, 
        callback: Callable[[DomainEvent], Awaitable[None]]
    ) -> Callable[[], None]:
        pass