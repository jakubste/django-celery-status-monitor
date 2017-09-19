from django.conf import settings
from celery import Celery

from celery_monitor.models import CeleryHeartBeat

celery = Celery(settings.CELERY_MONITOR_CELER_APP_NAME)


@celery.task
def heartbeat(label='default'):
    CeleryHeartBeat.objects.get_or_create(label=label)[0].save()
