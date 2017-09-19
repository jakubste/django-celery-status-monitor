from datetime import timedelta

from django.conf import settings
from django.template.response import TemplateResponse
from django.utils import timezone
from django.views.generic import DetailView, ListView

from celery_monitor.models import CeleryHeartBeat


class CeleryHeartBeatListView(ListView):
    model = CeleryHeartBeat
    template_name = 'celery_monitor/list.html'
    context_object_name = 'heartbeats'


class CeleryHeartBeatDetailView(DetailView):
    model = CeleryHeartBeat
    template_name = 'celery_monitor/detail.html'
    context_object_name = 'heartbeat'
    slug_url_kwarg = 'label'
    slug_field = 'label'


class ErrorTemplateResponse(TemplateResponse):
    status_code = 418


class CeleryHeartBeatStatusView(CeleryHeartBeatDetailView):
    def render_to_response(self, *args, **kwargs):
        if (timezone.now() - self.object.modified) > settings.CELERY_MONITOR_FREQ * 2:
            self.response_class = ErrorTemplateResponse

        return super().render_to_response(*args, **kwargs)
