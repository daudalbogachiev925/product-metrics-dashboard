def compute_dau_mau(daily_list):
    if not daily_list:
        return {"dau": 0, "mau": 0, "stickiness": 0.0}
    dau = daily_list[-1].active_users
    mau = sum(d.active_users for d in daily_list[-30:])
    stickiness = dau / mau if mau > 0 else 0.0
    return {"dau": dau, "mau": mau, "stickiness": stickiness}
