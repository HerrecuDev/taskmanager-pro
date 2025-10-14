# Dashboard de estadísticas para TaskManager Pro

class StatsDashboard:
    """Genera métricas y estadísticas de productividad"""
    
    def __init__(self, tasks):
        self.tasks = tasks
    
    def get_completion_rate(self):
        """Calcula el porcentaje de tareas completadas"""
        if not self.tasks:
            return 0
        completed = len([t for t in self.tasks if t.get('status') == 'completed'])
        return (completed / len(self.tasks)) * 100
    
    def get_tasks_by_priority(self):
        """Agrupa tareas por nivel de prioridad"""
        stats = {'high': 0, 'medium': 0, 'low': 0}
        for task in self.tasks:
            priority = task.get('priority', 'medium')
            stats[priority] = stats.get(priority, 0) + 1
        return stats
    
    def get_overdue_tasks(self):
        """Cuenta tareas atrasadas"""
        from datetime import datetime
        now = datetime.now()
        overdue = [
            t for t in self.tasks 
            if t.get('due_date') < now and t.get('status') != 'completed'
        ]
        return len(overdue)
    
    def get_productivity_score(self):
        """Calcula puntuación de productividad (0-100)"""
        completion_rate = self.get_completion_rate()
        overdue_count = self.get_overdue_tasks()
        total_tasks = len(self.tasks)
        
        if total_tasks == 0:
            return 0
        
        # Penalizar por tareas atrasadas
        penalty = (overdue_count / total_tasks) * 30
        score = max(0, completion_rate - penalty)
        return round(score, 2)
    
    def generate_report(self):
        """Genera un informe completo de estadísticas"""
        return {
            'total_tasks': len(self.tasks),
            'completion_rate': self.get_completion_rate(),
            'tasks_by_priority': self.get_tasks_by_priority(),
            'overdue_tasks': self.get_overdue_tasks(),
            'productivity_score': self.get_productivity_score()
        }
