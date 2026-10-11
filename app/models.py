from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.sql import func
from app.database import Base

class DailyMetric(Base):
    __tablename__ = "daily_metrics"
    id = Column(Integer, primary_key=True)
    date = Column(Date, index=True)
    active_users = Column(Integer, default=0)
    new_users = Column(Integer, default=0)
    churned_users = Column(Integer, default=0)
    mrr = Column(Float, default=0.0)
    new_mrr = Column(Float, default=0.0)
    expansion_mrr = Column(Float, default=0.0)
    contraction_mrr = Column(Float, default=0.0)
    churn_mrr = Column(Float, default=0.0)
    created_at = Column(DateTime, server_default=func.now())

class CohortRetention(Base):
    __tablename__ = "cohort_retention"
    id = Column(Integer, primary_key=True)
    cohort = Column(String, index=True)
    week = Column(Integer)
    users = Column(Integer)
