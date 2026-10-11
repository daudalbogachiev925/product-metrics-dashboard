from datetime import date
from typing import Optional, List
from pydantic import BaseModel

class DailyMetricCreate(BaseModel):
    date: date
    active_users: int
    new_users: int
    churned_users: int
    mrr: float
    new_mrr: float = 0.0
    expansion_mrr: float = 0.0
    contraction_mrr: float = 0.0
    churn_mrr: float = 0.0

class DailyMetricRead(DailyMetricCreate):
    id: int
    class Config:
        from_attributes = True

class KpiSummary(BaseModel):
    dau: int
    mau: int
    stickiness: float
    total_mrr: float
    mrr_growth_mom: float
    nrr: float
    quick_ratio: float
    ltv: float
    ltv_cac: float
