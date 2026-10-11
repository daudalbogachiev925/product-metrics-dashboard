from app.core.dau_mau import compute_dau_mau

class D:
    def __init__(self, a): self.active_users = a

def test_dau_mau():
    daily = [D(100) for _ in range(30)]
    r = compute_dau_mau(daily)
    assert r["dau"] == 100
    assert r["mau"] == 3000
    assert abs(r["stickiness"] - 100/3000) < 1e-6

def test_empty():
    r = compute_dau_mau([])
    assert r["dau"] == 0
