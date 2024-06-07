from datetime import datetime

class DomainEvent:
    def __init__(self):
        self.__event_time = datetime.now()

    @property
    def event_time(self) -> datetime:
        return self.__event_time

    @property
    @classmethod
    def name(cls) -> str:
        return cls.__name__
   