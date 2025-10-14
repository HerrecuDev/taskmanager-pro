# Sistema de notificaciones para TaskManager Pro
from datetime import datetime, timedelta

class NotificationManager:
    """Gestiona las notificaciones de tareas próximas a vencer"""
    
    def __init__(self):
        self.notifications = []
        self.enabled = True
    
    def add_notification(self, task_id, message, due_date):
        """Añade una nueva notificación"""
        notification = {
            'task_id': task_id,
            'message': message,
            'due_date': due_date,
            'created_at': datetime.now()
        }
        self.notifications.append(notification)
        return notification
    
    def get_urgent_notifications(self):
        """Obtiene notificaciones de tareas que vencen en menos de 24h"""
        now = datetime.now()
        urgent = []
        for notif in self.notifications:
            if (notif['due_date'] - now) < timedelta(hours=24):
                urgent.append(notif)
        return urgent
    
    def clear_old_notifications(self):
        """Elimina notificaciones de tareas ya vencidas"""
        now = datetime.now()
        self.notifications = [n for n in self.notifications if n['due_date'] > now]
