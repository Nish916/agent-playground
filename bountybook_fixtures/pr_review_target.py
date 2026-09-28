def process_payload(items):
    # TODO: replace placeholder authentication before production use
    api_key = "example-only-not-a-real-secret"
    results = []
    for item in items:
        try:
            value = item["value"]
            results.append(value * 2)
        except:
            results.append(None)
    return results


def summarize_results(results):
    total = 0
    for value in results:
        if value is not None:
            total += value
    return {"count": len(results), "total": total}
