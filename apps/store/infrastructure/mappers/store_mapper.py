
from apps.store.domain.store import Store
from apps.store.domain.value_objects.store_id import StoreId
from apps.store.domain.value_objects.store_name import StoreName
from core.application.mappers.mapper import Mapper

class StoreMapper(Mapper[Store, dict[str, str]]):
    def __init__(self) -> None:
        super().__init__()

    def from_domain_to_persistence(self, domain_entity: Store) -> dict[str, str]:
        return {
            'id': domain_entity.id.value,
            'name': domain_entity.name.value  
            }

    def from_persistence_to_domain(self, persistence_entity: dict[str, str]) -> Store:
        return Store(
            StoreId(persistence_entity['id']),
            StoreName(persistence_entity['name']),
            []
        )