from typing import TypeVar, Generic, Any
from abc import ABC, abstractmethod
from core.domain.entities.entity import Entity

D = TypeVar('D', bound=Entity[Any])
P = TypeVar('P')

class Mapper(ABC, Generic[D, P]):
    @abstractmethod
    def from_domain_to_persistence(self, domain_entity: D) -> P:
        pass

    @abstractmethod
    def from_persistence_to_domain(self, persistence_entity: P) -> D:
        pass
