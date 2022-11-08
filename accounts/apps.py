from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

# class voteresultsConfig(AppConfig):
#     name="voteResults"
#     def ready(self):
#         from . import signals