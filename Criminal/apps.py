from django.apps import AppConfig


class CriminalConfig(AppConfig):
    name = 'Criminal'

    def ready(self):
        import Criminal.signals
