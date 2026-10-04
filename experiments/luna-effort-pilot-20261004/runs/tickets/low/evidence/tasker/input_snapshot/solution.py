def urgent_open(tickets):
    return [ticket["id"] for ticket in tickets
            if ticket["status"] == "open" and ticket["priority"] >= 4
            or ticket["age_hours"] >= 48]
