import pandas as pd

class Vehicle:
    def __init__(self, vehicle_id, model, capacity):
        self.vehicle_id = vehicle_id
        self.model = model
        self.capacity = capacity
        self.area_assigned = None
        self.available = True

    def assign_to_area(self, area):
        if self.available:
            self.area_assigned = area
            self.available = False
            print(f"Vehicle {self.vehicle_id} assigned to {area}")
        else:
            print(f"Vehicle {self.vehicle_id} is already assigned somewhere else")

    def mark_available(self):
        self.available = True
        self.area_assigned = None
        print(f"Vehicle {self.vehicle_id} marked as available again")


import pandas as pd

class VehicleManager:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle_id, model, capacity, file_path='data/vehicles.csv'):
        columns = ['vehicle_id', 'model', 'capacity', 'assigned_area', 'available']

        try:
            df = pd.read_csv(file_path)
            df = df.loc[:, ~df.columns.duplicated()]
        except (FileNotFoundError, pd.errors.EmptyDataError):
            df = pd.DataFrame(columns=columns)

        if vehicle_id in df['vehicle_id'].values:
            print("Vehicle already exists with this ID.")
        else:
            new_vehicle = pd.DataFrame([{
                'vehicle_id': vehicle_id,
                'model': model,
                'capacity': capacity,
                'assigned_area': '',
                'available': True
            }])
            df = pd.concat([df, new_vehicle], ignore_index=True)
            df.to_csv(file_path, index=False)
            print(f" Vehicle '{vehicle_id}' added successfully.")


    def delete_vehicle(self, vehicle_id):
        if vehicle_id in self.vehicles:
            del self.vehicles[vehicle_id]
            print("Vehicle deleted.")
        else:
            print("Vehicle not found.")

    def assign_vehicle(self, vehicle_id, area):
        v = self.vehicles.get(vehicle_id)
        if v:
            v.assign_to_area(area)
        else:
            print("Vehicle not found.")

    def mark_vehicle_available(self, vehicle_id):
        v = self.vehicles.get(vehicle_id)
        if v:
            v.mark_available()
        else:
            print("Vehicle not found.")

    def check_availability(self):
        available_list = [v for v in self.vehicles.values() if v.available]
        if available_list:
            print("Available Vehicles:")
            for v in available_list:
                print(f"{v.vehicle_id} - {v.model} (Capacity: {v.capacity})")
        else:
            print("No available vehicles.")
