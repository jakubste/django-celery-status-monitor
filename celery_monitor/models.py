from django.db import models
from model_utils.models import TimeStampedModel


class CeleryHeartBeat(TimeStampedModel):
    label = models.CharField(max_length=64)
