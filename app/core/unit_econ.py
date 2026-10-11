from app.config import settings

def compute_ltv(arpu, monthly_churn_rate, gross_margin=None):
    gross_margin = gross_margin or settings.DEFAULT_GROSS_MARGIN
    if monthly_churn_rate <= 0:
        return 0.0
    return arpu * gross_margin / monthly_churn_rate

def ltv_cac(ltv, cac=None):
    cac = cac or settings.DEFAULT_CAC
    return ltv / cac if cac > 0 else 0.0
