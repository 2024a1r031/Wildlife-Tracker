# Milestone 2 - Build a Multi-Sighting Patrol Register

PRIORITY = {"Snow Leopard": "HIGH", "Musk Deer": "HIGH",
            "Himalayan Monal": "MEDIUM", "Langur": "LOW"}
VALID_ZONES = ["Z1", "Z2", "Z3"]

records = []            # list of dictionaries (valid records only)
unique_species = set()  # set keeps unique species names
rejected_count = 0

print("Enter sightings. Type DONE as the species name to finish.")
while True:
    species = input("\nSpecies (or DONE): ").strip().title()
    if species.upper() == "DONE":
        break
    zone = input("Zone (Z1/Z2/Z3): ").strip().upper()
    count = int(input("Count: "))
    duration_min = float(input("Duration (minutes): "))

    if species not in PRIORITY:
        print("REJECTED: unknown species ->", species)
        rejected_count += 1
        continue
    if zone not in VALID_ZONES:
        print("REJECTED: invalid zone ->", zone)
        rejected_count += 1
        continue
    if count <= 0:
        print("REJECTED: count must be greater than 0")
        rejected_count += 1
        continue

    records.append({"species": species, "zone": zone, "count": count,
                    "duration": duration_min, "priority": PRIORITY[species]})
    unique_species.add(species)
    print("Record saved.")

print("\n========== PATROL SUMMARY ==========")
print("Total valid records   :", len(records))
print("Total animals         :", sum(r["count"] for r in records))
print("Unique species count  :", len(unique_species))
print("Rejected entries      :", rejected_count)
print("Zone-wise sightings:")
for z in VALID_ZONES:
    print(f"  {z}: {sum(r['count'] for r in records if r['zone'] == z)} animals")
print("HIGH-priority records:")
high = [r for r in records if r["priority"] == "HIGH"]
for r in high:
    print(f"  {r['species']} in {r['zone']} - count {r['count']}")
if not high:
    print("  None")