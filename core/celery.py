from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.conf.enable_utc = True

app.conf.update(timezone = 'UTC')

app.config_from_object(settings, namespace='CELERY')

# celery beat settings
app.conf.beat_schedule = {}
app.autodiscover_tasks()

@app.task(bind=True)
def dubug_task(self):
    print(f'request: {self.request!r}')