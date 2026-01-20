from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["app.tasks.fetch_prices"],
)

celery_app.conf.beat_schedule = {
    "fetch-prices-every-10s": {
        "task": "app.tasks.fetch_prices.fetch_prices",
        "schedule": 
    }
}

celery_app.conf.timezone = "UTC"
