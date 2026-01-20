import aiohttp
from app.core.config import settings


class DeribitClient:
    async def get_index_price(self, ticker: str) -> float:
        url = f"{settings.DERIBIT_BASE_URL}/public/get_index_price"
        params = {"index_name": ticker}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                data = await response.json()
                return data["result"]["index_price"]


