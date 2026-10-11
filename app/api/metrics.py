from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import DailyMetric
from app.schemas import KpiSummary
from app.core.dau_mau import compute_dau_mau
from app.core.revenue import mrr_metrics
from app.core.unit_econ import compute_ltv, ltv_cac

router = APIRouter()

@router.get("/kpi", response_model=KpiSummary)
def kpi(db: Session = Depends(get_db)):
    daily = db.query(DailyMetric).order_by(DailyMetric.date.asc()).all()
    if not daily:
        return KpiSummary(dau=0, mau=0, stickiness=0.0, total_mrr=0.0,
                           mrr_growth_mom=0.0, nrr=0.0, quick_ratio=0.0,
                           ltv=0.0, ltv_cac=0.0)
    dm = compute_dau_mau(daily)
    rev = mrr_metrics(daily)
    arpu = daily[-1].mrr / max(dm["mau"], 1)
    churn_rate = abs(daily[-1].churn_mrr) / max(daily[-1].mrr, 1)
    ltv = compute_ltv(arpu, churn_rate)
    return KpiSummary(
        dau=dm["dau"], mau=dm["mau"], stickiness=dm["stickiness"],
        total_mrr=daily[-1].mrr, mrr_growth_mom=rev["growth"],
        nrr=rev["nrr"], quick_ratio=rev["quick_ratio"],
        ltv=ltv, ltv_cac=ltv_cac(ltv))

@router.get("/revenue")
def revenue(db: Session = Depends(get_db)):
    daily = db.query(DailyMetric).order_by(DailyMetric.date.asc()).all()
    return [{"date": d.date.isoformat(), "mrr": d.mrr,
             "new": d.new_mrr, "expansion": d.expansion_mrr,
             "contraction": d.contraction_mrr, "churn": d.churn_mrr}
            for d in daily]
