def mrr_metrics(daily):
    if len(daily) < 2:
        return {"mrr": 0, "growth": 0.0, "nrr": 0.0, "quick_ratio": 0.0}
    last = daily[-1]
    prev = daily[-2]
    mrr = last.mrr
    growth = (mrr - prev.mrr) / prev.mrr if prev.mrr > 0 else 0.0
    net_new = last.new_mrr + last.expansion_mrr + last.contraction_mrr + last.churn_mrr
    nrr = 1 + net_new / prev.mrr if prev.mrr > 0 else 0.0
    positives = last.new_mrr + last.expansion_mrr
    negatives = abs(last.contraction_mrr + last.churn_mrr)
    quick = positives / negatives if negatives > 0 else 0.0
    return {"mrr": mrr, "growth": growth, "nrr": nrr, "quick_ratio": quick}
