from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import DailyMetric
from app.schemas import DailyMetricCreate, DailyMetricRead

router = APIRouter()

@router.post("", response_model=DailyMetricRead, status_code=201)
def add(payload: DailyMetricCreate, db: Session = Depends(get_db)):
    existing = db.query(DailyMetric).filter(DailyMetric.date == payload.date).first()
    if existing:
        for k, v in payload.model_dump().items():
            setattr(existing, k, v)
        db.commit()
        db.refresh(existing)
        return existing
    m = DailyMetric(**payload.model_dump())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

@router.get("", response_model=List[DailyMetricRead])
def list_all(db: Session = Depends(get_db), limit: int = 365):
    return db.query(DailyMetric).order_by(DailyMetric.date.desc()).limit(limit).all()
