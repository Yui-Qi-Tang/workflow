def aggregate(rows):
    totals = {}
    for row in rows:
        sku = row["sku"].strip()
        if not sku:
            continue
        totals[sku] = totals.get(sku, 0) + row["delta"]
    return [{"sku": sku, "delta": delta} for sku, delta in totals.items()]
