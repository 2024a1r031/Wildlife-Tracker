# Milestone 1 - Record and Analyse One Wildlife Sighting

observer = input("Observer name: ").strip()
species = input("Species: ").strip()
zone = input("Zone (Z1/Z2/Z3): ").strip().upper()
count = int(input("Count: "))
duration_min = float(input("Observation duration (minutes): "))
distance_m = float(input("Distance (metres): "))

print("\n--- Data types ---")
print("Type of count   :", type(count))
print("Type of distance:", type(distance_m))

sightings_per_min = count / duration_min
distance_km = distance_m / 1000

observer_name = observer.title()
species_name = species.title()
sighting_code = observer_name[:2].upper() + species_name.replace(" ", "")[:2].upper()

print("\n--- Sighting Report ---")
print("Sighting code     :", sighting_code)
print("Observer          :", observer_name)
print("Species           :", species_name)
print("Zone              :", zone)
print(f"Sightings per min : {sightings_per_min:.3f}")
print(f"Distance          : {distance_km:.2f} km")