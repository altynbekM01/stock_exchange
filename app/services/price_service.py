from sqlalchemy.orm import Session
from app.db.models import Price


class PriceService:
    def __init__(self, db: Session):
        self.db = db

    def save_price(self, ticker: str, price: float, timestamp: int) -> None:
        self.db.add(
            Price(
                ticker=ticker,
                price=price,
                timestamp=timestamp
            )
        )
        self.db.commit()

    def get_all(self, ticker: str):
        return self.db.query(Price).filter(Price.ticker == ticker).all()

    def get_latest(self, ticker: str):
        return (
            self.db.query(Price)
            .filter(Price.ticker == ticker)
            .order_by(Price.timestamp.desc())
            .first()
        )

    def get_by_period(self, ticker: str, from_ts: int, to_ts: int):
        return (
            self.db.query(Price)
            .filter(
                Price.ticker == ticker,
                Price.timestamp >= from_ts,
                Price.timestamp <= to_ts
            )
            .all()
        )
