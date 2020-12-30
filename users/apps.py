from django.apps import AppConfig

# Import signals created at the profile in here

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
