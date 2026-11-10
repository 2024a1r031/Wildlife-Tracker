import math


def zone_summary(records):
    """Return {zone: {'sightings': n, 'animals': total}} for each zone in records."""
    summary = {}
    for record in records:
        zone = record["zone"]
        entry = summary.setdefault(zone, {"sightings": 0, "animals": 0})
        entry["sightings"] += 1
        entry["animals"] += record["count"]
    return summary


def species_total(records, species):
    """Return the total animals counted for one species."""
    return sum(r["count"] for r in records if r["species"] == species)


def estimate_patrol_hours(distance_km, speed_kmph=4.0):
    """Hours needed to walk distance_km, rounded UP to a whole hour using math.ceil."""
    return math.ceil(distance_km / speed_kmph)


def average_count(*counts):
    """Average of any number of counts (variable-length arguments)."""
    if not counts:
        return 0.0
    return sum(counts) / len(counts)