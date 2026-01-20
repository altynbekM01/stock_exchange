from fastapi import FastAPI
from app.api.prices import router as prices_router
from app.db.base import Base
from app.db.session import engine
import time
import sqlalchemy

app = FastAPI(title="Crypto Prices API")

app.include_router(prices_router)

@app.on_event("startup")
def on_startup():
    for i in range(10):
        try:
            with engine.connect() as conn:
                conn.execute(sqlalchemy.text("SELECT 1"))
            break
        except Exception:
            time.sleep(2)
    else:
        raise RuntimeError("DB not ready")

    Base.metadata.create_all(bind=engine)
