# Milestone 5 - Preserve Field Logs and Recover from Bad Records
import os
import time
from wildlife_utils import zone_summary

LOG_FILE = os.path.join("field_logs", "sightings.txt")
DELIMITER = "|"            # log format: zone|species|count|distance_m
VALID_ZONES = ("Z1", "Z2", "Z3")


def add_record():
    """Validate one sighting and append it to the log. Bad input is never saved."""
    zone = input("Zone (Z1/Z2/Z3): ").strip().upper()
    species = input("Species: ").strip().title()
    count_text = input("Count: ")
    distance_text = input("Distance (metres): ")
    try:
        count = int(count_text)
        distance_m = float(distance_text)
    except ValueError:
        print("ERROR: count must be a whole number and distance a number. Record NOT saved.")
        return
    if count <= 0 or zone not in VALID_ZONES:
        print("ERROR: count must be > 0 and zone must be Z1, Z2 or Z3. Record NOT saved.")
        return
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as log:
        log.write(DELIMITER.join([zone, species, str(count), f"{distance_m:g}"]) + "\n")
    print("Saved to", LOG_FILE)


def read_log():
    """Read the log, skipping and reporting bad lines. Returns the valid records."""
    valid_records = []
    try:
        with open(LOG_FILE, "r") as log:
            lines = log.readlines()
    except FileNotFoundError:
        print(f"ERROR: log file '{LOG_FILE}' not found. Add a sighting first.")
        return valid_records

    print(f"Lines read from log: {len(lines)}")
    for line_no, line in enumerate(lines, start=1):
        text = line.strip()
        parts = text.split(DELIMITER)
        if len(parts) != 4:
            print(f"Line {line_no}: missing fields, skipped -> {text}")
            continue
        zone, species, count_text, distance_text = parts
        try:
            count = int(count_text)
            distance_m = float(distance_text)
        except ValueError:
            print(f"Line {line_no}: invalid number, skipped -> {text}")
            continue
        valid_records.append({"zone": zone, "species": species,
                              "count": count, "distance_m": distance_m})
    return valid_records


def show_metadata():
    if os.path.exists(LOG_FILE):
        size = os.path.getsize(LOG_FILE)
        modified = time.ctime(os.path.getmtime(LOG_FILE))
        print(f"Metadata -> size: {size} bytes, last modified: {modified}")


def main():
    while True:
        print("\n1. Add sighting\n2. View log\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_record()
        elif choice == "2":
            records = read_log()
            show_metadata()
            if records:
                print("\nValid records:")
                for r in records:
                    print(f"  {r['zone']} | {r['species']} | count {r['count']} | {r['distance_m']:g} m")
                print("Zone summary:", zone_summary(records))
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()