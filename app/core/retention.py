def cohort_matrix(cohorts):
    by_cohort = {}
    for c in cohorts:
        by_cohort.setdefault(c.cohort, {})[c.week] = c.users
    return by_cohort

def retention_rate(by_cohort):
    result = {}
    for cohort, weeks in by_cohort.items():
        base = weeks.get(0, 1)
        result[cohort] = {w: round(v / base, 4) for w, v in weeks.items()}
    return result
