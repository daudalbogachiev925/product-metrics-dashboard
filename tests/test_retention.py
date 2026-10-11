from app.core.retention import cohort_matrix, retention_rate

class C:
    def __init__(self, c, w, u):
        self.cohort = c; self.week = w; self.users = u

def test_cohort():
    cohorts = [C("2026-01", 0, 1000), C("2026-01", 1, 600),
               C("2026-02", 0, 500), C("2026-02", 1, 300)]
    m = cohort_matrix(cohorts)
    rates = retention_rate(m)
    assert rates["2026-01"][1] == 0.6
    assert rates["2026-02"][1] == 0.6
