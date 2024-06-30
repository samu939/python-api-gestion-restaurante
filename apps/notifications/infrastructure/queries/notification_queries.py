
GET_ALL_USER_NOTIFICATIONS = """
    SELECT n.id, n.message, n.date, n.target_user FROM notifications as n WHERE target_user = :user_id
"""


SAVE_NOTIFICATION = """
    INSERT INTO notifications (id, message, target_user) VALUES (:id, :message, :target_user)
"""