def aggregate(rows):
    latest = {}
    for row in rows:
        latest[row["sku"]] = row["delta"]
    return [{"sku": sku, "delta": latest[sku]} for sku in sorted(latest)]
