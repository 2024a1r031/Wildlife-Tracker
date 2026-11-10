# Milestone 3 - Model a Sighting with OOP and a Custom Exception

class InvalidSightingError(Exception):
    """Raised when a sighting has a count <= 0 or a zone outside Z1, Z2, Z3."""


class WildlifeSighting:
    project_name = "Wildlife Sighting and Patrol Monitoring Tracker"
    PRIORITY = {"Snow Leopard": "HIGH", "Musk Deer": "HIGH",
                "Himalayan Monal": "MEDIUM", "Langur": "LOW"}
    PRIORITY_WEIGHT = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
    VALID_ZONES = ("Z1", "Z2", "Z3")

    def __init__(self, species, zone, count, distance_m):
        if count <= 0:
            raise InvalidSightingError(f"Count must be greater than 0 (got {count})")
        if zone not in self.VALID_ZONES:
            raise InvalidSightingError(f"Zone must be Z1, Z2 or Z3 (got {zone})")
        self.species = species
        self.zone = zone
        self.count = count
        self.distance_m = distance_m
        self.priority = self.PRIORITY.get(species, "LOW")

    def monitoring_score(self):
        """Rule: score = count x priority weight (HIGH=3, MEDIUM=2, LOW=1)."""
        return self.count * self.PRIORITY_WEIGHT[self.priority]

    def display_record(self):
        print(f"{self.species:<16} | Zone {self.zone} | Count {self.count:>3} | "
              f"Priority {self.priority:<6} | Score {self.monitoring_score()}")

    def __str__(self):
        return (f"WildlifeSighting({self.species}, {self.zone}, "
                f"count={self.count}, distance={self.distance_m} m)")


if __name__ == "__main__":
    print("Project:", WildlifeSighting.project_name)
    print("\n--- Valid sightings ---")
    s1 = WildlifeSighting("Snow Leopard", "Z2", 2, 650)
    s2 = WildlifeSighting("Langur", "Z1", 5, 300)
    for obj in (s1, s2):
        print(obj)
        print("isinstance check:", isinstance(obj, WildlifeSighting))
        obj.display_record()

    print("\n--- Invalid sightings ---")
    try:
        WildlifeSighting("Musk Deer", "Z9", 3, 800)
    except InvalidSightingError as error:
        print("Rejected:", error)
    try:
        WildlifeSighting("Musk Deer", "Z1", 0, 800)
    except InvalidSightingError as error:
        print("Rejected:", error)