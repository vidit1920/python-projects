import pandas as pd
import os

RECYCLING_FILE = 'data/recycling.csv'

class RecyclingUnit:
    def __init__(self, unit_id, capacity, status='working'):
        self.unit_id = unit_id
        self.capacity = capacity
        self.status = status

    def to_dict(self):
        return {
            'unit_id': self.unit_id,
            'capacity': self.capacity,
            'status': self.status
        }

    def update_status(self, new_status):
        self.status = new_status
        print(f"> Status of Unit {self.unit_id} updated to '{self.status}'.")

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity
        print(f"> Capacity of Unit {self.unit_id} updated to {self.capacity} liters.")


class RecyclingUnitManager:
    def __init__(self):
        self.units = {}
        self.load_from_csv()

    def add_unit(self, unit_id, capacity, status='working'):
        if unit_id in self.units:
            print("! Unit already exists with this ID.")
        else:
            self.units[unit_id] = RecyclingUnit(unit_id, capacity, status)
            self.save_to_csv()
            print(f"> Unit {unit_id} added successfully.")

    def update_unit_status(self, unit_id, new_status):
        unit = self.units.get(unit_id)
        if unit:
            unit.update_status(new_status)
            self.save_to_csv()
        else:
            print("! Unit not found.")

    def update_unit_capacity(self, unit_id, new_capacity):
        unit = self.units.get(unit_id)
        if unit:
            unit.update_capacity(new_capacity)
            self.save_to_csv()
        else:
            print("! Unit not found.")

    def show_all_units(self):
        if not self.units:
            print("! No units to display.")
        else:
            print("\nAll Recycling Units:")
            for unit in self.units.values():
                print(f" - {unit.unit_id} | {unit.capacity}L | Status: {unit.status}")

    def show_units_by_status(self, status):
        filtered_units = [
            unit for unit in self.units.values()
            if unit.status.lower() == status.lower()
        ]
        if filtered_units:
            print(f"\nUnits with status '{status}':")
            for unit in filtered_units:
                print(f" - {unit.unit_id} ({unit.capacity}L)")
        else:
            print(f"! No units found with status '{status}'.")

    def save_to_csv(self):
        df = pd.DataFrame([unit.to_dict() for unit in self.units.values()])
        df.to_csv(RECYCLING_FILE, index=False)

    def load_from_csv(self):
        if not os.path.exists(RECYCLING_FILE):
            return
        try:
            df = pd.read_csv(RECYCLING_FILE)
            for _, row in df.iterrows():
                self.units[row['unit_id']] = RecyclingUnit(
                    row['unit_id'],
                    int(row['capacity']),
                    row['status']
                )
        except Exception as e:
            print(f"⚠️ Error loading recycling units: {e}")


def track_recycling_units():
    manager = RecyclingUnitManager()

    while True:
        print("\n========== Recycling Unit Tracker ==========")
        print("1. Add New Recycling Unit")
        print("2. Update Unit Status")
        print("3. Update Unit Capacity")
        print("4. Show All Units")
        print("5. Show Units by Status")
        print("6. Exit")
        print("============================================")

        choice = input("Enter your choice (1–6): ")

        if choice == "1":
            uid = input("Enter Unit ID (e.g., R001): ")
            try:
                cap = int(input("Enter Capacity (in liters): "))
                status = input("Enter Status (working/full/maintenance): ").lower()
                manager.add_unit(uid, cap, status)
            except ValueError:
                print("! Invalid number.")

        elif choice == "2":
            uid = input("Enter Unit ID: ")
            new_status = input("Enter New Status (working/full/maintenance): ")
            manager.update_unit_status(uid, new_status)

        elif choice == "3":
            uid = input("Enter Unit ID: ")
            try:
                new_cap = int(input("Enter New Capacity: "))
                manager.update_unit_capacity(uid, new_cap)
            except ValueError:
                print("! Invalid number.")

        elif choice == "4":
            manager.show_all_units()

        elif choice == "5":
            status = input("Enter status to filter (working/full/maintenance): ")
            manager.show_units_by_status(status)

        elif choice == "6":
            print("👋 Exiting Recycling Tracker.")
            break

        else:
            print("! Invalid choice. Please try again.")
