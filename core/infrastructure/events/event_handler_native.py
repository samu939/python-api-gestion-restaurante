from typing import Awaitable, Callable
from src.core.domain.events.domain_event import DomainEvent
from src.core.application.events.event_handler import EventHandler

class NativeEventHandler(EventHandler):
  _subscribers: dict[str, list[Callable[[DomainEvent], Awaitable[None]]]]

  def __init__(self) -> None:
    self._subscribers = {}

  async def publish_events(self, events: list[DomainEvent]) -> None:
    for event in events:
      event_name = event.__class__.__name__
      subscribers = self._subscribers.get(event_name, [])
      for subscriber in subscribers:
        await subscriber(event)

  def subscribe(
    self, 
    event_name: str, 
    callback: Callable[[DomainEvent], Awaitable[None]]
  ) -> Callable[[], None]:
    if event_name not in self._subscribers:
      self._subscribers[event_name] = []
    self._subscribers[event_name].append(callback)
    return lambda: self._subscribers[event_name].remove(callback)
  