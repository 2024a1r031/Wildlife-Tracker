# Milestone 4 - main.py: imports functions from wildlife_utils.py
import time
from wildlife_utils import zone_summary, species_total, estimate_patrol_hours, average_count

records = [
    {"species": "Snow Leopard", "zone": "Z2", "count": 2},
    {"species": "Musk Deer", "zone": "Z1", "count": 3},
    {"species": "Langur", "zone": "Z1", "count": 5},
    {"species": "Himalayan Monal", "zone": "Z3", "count": 4},
    {"species": "Snow Leopard", "zone": "Z3", "count": 1},
]

start_time = time.time()

print("=== Zone-wise Summary ===")
for zone, data in sorted(zone_summary(records).items()):
    print(f"{zone}: {data['sightings']} sightings, {data['animals']} animals")

print("\nTotal Snow Leopard animals:", species_total(records, "Snow Leopard"))

print("\n=== Average Count ===")
print("Average of 2, 3, 5          :", average_count(2, 3, 5))
print("Average of 1, 4, 4, 7       :", average_count(1, 4, 4, 7))

print("\n=== Patrol Hours ===")
route_km = 10.5
print(f"Route of {route_km} km at 4.0 km/h needs {estimate_patrol_hours(route_km)} hour(s) (rounded up)")

elapsed = time.time() - start_time
print(f"\nReport generated in {elapsed:.4f} seconds")