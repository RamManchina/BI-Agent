from datetime import datetime

def compute_metrics(items):
    now = datetime.now()

    total_revenue = sum(i["revenue"] for i in items)

    open_deals = [
        i for i in items if i["status"] and "working" in i["status"].lower()
    ]

    stalled_deals = []
    for i in items:
        if i["last_activity"]:
            days = (now - i["last_activity"]).days
            if days > 14:
                stalled_deals.append(i)

    avg_deal_size = total_revenue / len(items) if items else 0

    return {
        "total_revenue": total_revenue,
        "total_deals": len(items),
        "open_deals": len(open_deals),
        "stalled_deals": len(stalled_deals),
        "avg_deal_size": avg_deal_size,
    }
