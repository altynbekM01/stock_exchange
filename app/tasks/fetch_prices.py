import asyncio
import time
from celery import shared_task

from app.core.config import settings
from app.services.deribit_client import DeribitClient
from app.db.session import SessionLocal
from app.services.price_service import PriceService


@shared_task
def fetch_prices():
    db = SessionLocal()
    service = PriceService(db)
    client = DeribitClient()
    timestamp = int(time.time())

    async def _fetch():
        for ticker in settings.tickers:
            price = await client.get_index_price(ticker)
            service.save_price(ticker, price, timestamp)

    asyncio.run(_fetch())
    db.close()
