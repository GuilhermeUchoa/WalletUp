import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backEndApiFinanceApp.settings') 


app = Celery('backEndApiFinanceApp') 
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'updatePortfolio1Minute': {
        'task': 'portfolioAPI.tasks.atualizar_ativos',
        'schedule': crontab(minute='30,0', hour='9-18', day_of_week='1-5'), # A cada 30 minutos nos dias uteis das 9 as 17, vai dar um total de 16 chamadas por dia
    }
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

