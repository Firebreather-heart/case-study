from django.apps import AppConfig


class HackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hacker'

    def ready(self):
        from jobs import updater 
        updater.start()
