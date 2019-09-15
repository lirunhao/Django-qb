from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Django2.settings')

app = Celery('Django2',
             broker='redis://10.36.174.43:6379/6',
             backend='redis://10.36.174.43:6379/7',
             namespace='Celery')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()