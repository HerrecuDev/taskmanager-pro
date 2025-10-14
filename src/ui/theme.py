# Sistema de temas para TaskManager Pro

class ThemeManager:
    """Gestiona los temas de la interfaz"""
    
    THEMES = {
        'light': {
            'background': '#ffffff',
            'text': '#333333',
            'primary': '#673ab7',
            'secondary': '#9c27b0',
            'border': '#e0e0e0',
            'hover': '#f5f5f5'
        },
        'dark': {
            'background': '#1a1a1a',
            'text': '#e0e0e0',
            'primary': '#9575cd',
            'secondary': '#ba68c8',
            'border': '#424242',
            'hover': '#2d2d2d'
        }
    }
    
    def __init__(self):
        self.current_theme = 'light'
    
    def set_theme(self, theme_name):
        """Cambia el tema activo"""
        if theme_name in self.THEMES:
            self.current_theme = theme_name
            return True
        return False
    
    def get_theme(self):
        """Obtiene el tema actual"""
        return self.THEMES[self.current_theme]
    
    def toggle_theme(self):
        """Alterna entre tema claro y oscuro"""
        self.current_theme = 'dark' if self.current_theme == 'light' else 'light'
        return self.current_theme
    
    def get_color(self, property_name):
        """Obtiene un color específico del tema actual"""
        return self.THEMES[self.current_theme].get(property_name, '#000000')
