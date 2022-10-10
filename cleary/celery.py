from __future__ import absolute_import,unicode_literals
from django.conf import settings
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE','cleary.settings')
app=Celery('cleary')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings , namespace= 'CELERY')

######### FOR SENDING MAIL ON FIX TIME ##############

# app.conf.beat_schedule = {
#     'send-mail': {
#         'task': 'CL.tasks.send_mail',
#         'schedule': crontab(hour=12, minute=45),
#         #'args': (2,)
#     }
# }
 
######### FOR SENDING MAIL ON TIME INTERVAL EVERY 50 MIN ##########

app.conf.beat_schedule = {
    'send-mail': {
        'task': 'CL.tasks.send_mail',
        'schedule': crontab( minute= "*/50"),
        #'args': (2,)
    }
}

######### FOR SENDING MAIL ON TIME INTERVAL EVERY 5 MIN ##########

app.conf.beat_schedule = {
    'send-mail': {
        'task': 'CL.tasks.api_mail',
        'schedule': crontab( minute= "*/5"),
        #'args': (2,)
    }
}


# app.autodiscover_tasks(settings.INSTALLED_APPS)
app.autodiscover_tasks()

app.conf.beat_scheduler='django_celery_beat.schedulers.DatabaseScheduler'

@app.task(bind=True)
def debug_task(self):
    print(f'request:{self.request!r}')

