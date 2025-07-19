def timeline_stress_test(events):
    issues = []
    for i in range(1, len(events)):
        if events[i]['time'] < events[i-1]['time']:
            issues.append(f"Inconsistency: {events[i]['event']} occurs before {events[i-1]['event']}")
    return issues if issues else ["No contradictions found."]
