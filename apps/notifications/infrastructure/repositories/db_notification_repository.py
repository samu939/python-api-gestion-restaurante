from uuid import UUID
from apps.notifications.application.notification_in_db import NotificationInDB
from apps.notifications.application.notification_repository import NotificationRepository




class DbNotificationRepository (NotificationRepository):
    def __init__ (self, db):
        self.db = db
        
    async def get_all_notifications_by_user(self, user_id: str) -> list[NotificationInDB]:
        from apps.notifications.infrastructure.queries.notification_queries import GET_ALL_USER_NOTIFICATIONS
        notifications = await self.db.fetch_all(GET_ALL_USER_NOTIFICATIONS, {"user_id": str(user_id)})
        return [NotificationInDB( id=notification['id'], 
                                 message=notification['message'], 
                                 date=notification['date'], 
                                 target_user=notification['target_user'] ) for notification in notifications]
    
    async def save_notification(self, id:UUID, message: str, target_user: UUID) -> None:
        from apps.notifications.infrastructure.queries.notification_queries import SAVE_NOTIFICATION
        await self.db.execute(SAVE_NOTIFICATION, {"id":id, "message": message, "target_user": str(target_user)})