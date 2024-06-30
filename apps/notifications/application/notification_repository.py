from abc import abstractmethod
from typing import Awaitable, Optional
from uuid import UUID
from apps.notifications.application.notification_in_db import NotificationInDB


class NotificationRepository:

    @abstractmethod
    def get_all_notifications_by_user(self, user_id: str) -> Awaitable[list[NotificationInDB]]:
        pass
    @abstractmethod
    def save_notification(self,id:UUID, message: str, target_user: UUID) -> Awaitable[None]:
        pass
    

