from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.price_service import PriceService

router = APIRouter(prefix="/prices", tags=["prices"])


@router.get("/")
def get_all_prices(ticker: str, db: Session = Depends(get_db)):
    service = PriceService(db)
    return service.get_all(ticker)


@router.get("/latest")
def get_latest_price(ticker: str, db: Session = Depends(get_db)):
    service = PriceService(db)
    return service.get_latest(ticker)


@router.get("/by-date")
def get_prices_by_date(
    ticker: str,
    from_ts: int,
    to_ts: int,
    db: Session = Depends(get_db),
):
    service = PriceService(db)
    return service.get_by_period(ticker, from_ts, to_ts)
