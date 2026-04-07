def generate_id(items):
    if not items:
        return 1
    return max(item["id"] for item in items) + 1
