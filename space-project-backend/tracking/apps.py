from django.apps import AppConfig


class TrackingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracking'

    def ready(self):

        from apscheduler.schedulers.background import BackgroundScheduler
        from .tasks import fetch_and_store_iss

        scheduler = BackgroundScheduler()
        scheduler.add_job(fetch_and_store_iss, "interval", seconds=10)
        scheduler.start()