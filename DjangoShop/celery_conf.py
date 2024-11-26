from celery import Celery
from datetime import timedelta
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoShop.settings')

celery_app = Celery('DjangoShop')
celery_app.autodiscover_tasks()

celery_app.conf.broker_url = 'D:\prj2\DjangoShop\venv\Lib\site-packages\rabbitmq:'
celery_app.conf.result_backend = 'rpc://'
