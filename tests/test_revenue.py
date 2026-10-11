from app.core.revenue import mrr_metrics

class D:
    def __init__(self, mrr, new=0, exp=0, contr=0, churn=0):
        self.mrr = mrr
        self.new_mrr = new; self.expansion_mrr = exp
        self.contraction_mrr = contr; self.churn_mrr = churn

def test_mrr_growth():
    daily = [D(100000, new=10000), D(110000, new=15000, churn=-5000)]
    r = mrr_metrics(daily)
    assert r["mrr"] == 110000
    assert r["growth"] > 0
