# Sistema de filtros avanzados para TaskManager Pro

class TaskFilter:
    """Proporciona filtrado multi-criterio de tareas"""
    
    def __init__(self, tasks):
        self.tasks = tasks
        self.filtered_tasks = tasks.copy()
    
    def by_priority(self, priority):
        """Filtra tareas por prioridad (high, medium, low)"""
        self.filtered_tasks = [
            t for t in self.filtered_tasks 
            if t.get('priority') == priority
        ]
        return self
    
    def by_status(self, status):
        """Filtra tareas por estado (pending, in_progress, completed)"""
        self.filtered_tasks = [
            t for t in self.filtered_tasks 
            if t.get('status') == status
        ]
        return self
    
    def by_category(self, category):
        """Filtra tareas por categoría"""
        self.filtered_tasks = [
            t for t in self.filtered_tasks 
            if t.get('category') == category
        ]
        return self
    
    def by_date_range(self, start_date, end_date):
        """Filtra tareas por rango de fechas"""
        self.filtered_tasks = [
            t for t in self.filtered_tasks
            if start_date <= t.get('due_date') <= end_date
        ]
        return self
    
    def get_results(self):
        """Obtiene los resultados filtrados"""
        return self.filtered_tasks
    
    def reset(self):
        """Reinicia los filtros"""
        self.filtered_tasks = self.tasks.copy()
        return self
