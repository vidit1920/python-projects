import pandas as pd
from datetime import datetime
from new_complaint import manage_complaints
import os

# File paths
USER_FILE = "data/users.csv"
AREA_FILE = "data/areas.csv"
VEHICLE_FILE = "data/vehicles.csv"
SCHEDULE_FILE = "data/schedules.csv"
COMPLAINT_FILE = "data/complaints.csv"
RECYCLING_FILE = "data/recycling.csv"

# Initialize CSV files
def init_files():
    if not os.path.exists(USER_FILE):
        pd.DataFrame([
            {'username': 'admin', 'password': 'admin123', 'role': 'admin'},
            {'username': 'staff1', 'password': 'staff123', 'role': 'staff'}
        ]).to_csv(USER_FILE, index=False)

    files_and_columns = [
        (AREA_FILE, ['area_code', 'area_name', 'population', 'priority']),
        (VEHICLE_FILE, ['vehicle_id', 'status', 'assigned_area']),
        (SCHEDULE_FILE, ['pickup_id', 'area_code', 'frequency', 'vehicle_id', 'time']),
        (COMPLAINT_FILE, ['complaint_id', 'area_code', 'description', 'status', 'timestamp']),
        (RECYCLING_FILE, ['unit_id', 'status', 'capacity'])
    ]

    for file, columns in files_and_columns:
        if not os.path.exists(file):
            pd.DataFrame(columns=columns).to_csv(file, index=False)

# Login function
def login():
    users = pd.read_csv(USER_FILE)
    username = input("Username: ")
    password = input("Password: ")
    user = users[(users['username'] == username) & (users['password'] == password)]
    if not user.empty:
        print(f" Logged in as {user.iloc[0]['role']}")
        return user.iloc[0]['role']
    else:
        print(" Invalid login.")
        return None

# Area Management
def manage_areas():
    areas = pd.read_csv(AREA_FILE)
    print("\n--- Area Management ---")
    print("1. Add area\n2. View areas")
    choice = input("Choose: ")
    if choice == '1':
        code = input("Enter area code: ")
        name = input("Enter area name: ")
        pop = int(input("Enter population: "))
        priority = input("Enter priority (Low/Medium/High): ")
        new_area = pd.DataFrame([{
            'area_code': code,
            'area_name': name,
            'population': pop,
            'priority': priority
        }])
        areas = pd.concat([areas, new_area], ignore_index=True)
        areas.to_csv(AREA_FILE, index=False)
        print(" Area added.")
    elif choice == '2':
        print(areas)

# Vehicle Management
def manage_vehicles():
    vehicles = pd.read_csv(VEHICLE_FILE)
    print("\n--- Vehicle Management ---")
    print("1. Add vehicle\n2. View vehicles")
    choice = input("Choose: ")
    if choice == '1':
        vid = input("Enter vehicle ID: ")
        status = input("Enter status (available/unavailable): ")
        area = input("Assigned area code (leave blank if none): ")
        new_vehicle = pd.DataFrame([{
            'vehicle_id': vid,
            'status': status,
            'assigned_area': area
        }])
        vehicles = pd.concat([vehicles, new_vehicle], ignore_index=True)
        vehicles.to_csv(VEHICLE_FILE, index=False)
        print(" Vehicle added.")
    elif choice == '2':
        print(vehicles)

# Waste Pickup Scheduler

SCHEDULE_FILE = 'data/schedules.csv'
AREA_FILE = 'data/areas.csv'
VEHICLE_FILE = 'data/vehicles.csv'

def schedule_pickups():
    if not os.path.exists(SCHEDULE_FILE):
        pd.DataFrame(columns=['pickup_id', 'area_code', 'frequency', 'vehicle_id', 'time']).to_csv(SCHEDULE_FILE, index=False)

    schedules = pd.read_csv(SCHEDULE_FILE)
    areas = pd.read_csv(AREA_FILE, dtype={'Pincode': str})
    vehicles = pd.read_csv(VEHICLE_FILE, dtype={'vehicle_id': str})

        # Display area list
    print("\nAvailable Areas:")
    print(areas[['Area Name', 'Pincode']].to_string(index=False))

    # Display available vehicles
    available_vehicles = vehicles[vehicles['available'].astype(str).str.lower() == 'true']

    if available_vehicles.empty:
        print("\n No available vehicles at the moment.")
    else:
        print("\nAvailable Vehicles:")
        print(available_vehicles[['vehicle_id', 'model', 'capacity']].to_string(index=False))

    while True:
        pickup_id = f"PICK{len(schedules) + 1:03}"

       
        while True:
            area_code = input("Enter area code: ").strip()
            if area_code in areas['Pincode'].astype(str).values:
                break
            print(" Invalid area code.")
            while True:
                retry = input("Do you want to retry? (yes/no): ").strip().lower()
                if retry in ['yes', 'no']:
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
            if retry == 'no':
                return

        # FREQUENCY input with validated retry
        while True:
            frequency = input("Enter pickup frequency (Daily/Weekly/etc.): ").strip().capitalize()
            if frequency:
                break
            print(" Frequency cannot be empty.")
            while True:
                retry = input("Do you want to retry? (yes/no): ").strip().lower()
                if retry in ['yes', 'no']:
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
            if retry == 'no':
                return

        # VEHICLE ID input with validated retry
        while True:
            vehicle_id = input("Enter assigned vehicle ID: ").strip()
            if vehicle_id not in vehicles['vehicle_id'].values:
                print(" Vehicle ID does not exist.")
            elif vehicle_id in schedules['vehicle_id'].values:
                print("⚠ Vehicle already assigned in schedule. Use another.")
            else:
                break
            while True:
                retry = input("Do you want to retry? (yes/no): ").strip().lower()
                if retry in ['yes', 'no']:
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
            if retry == 'no':
                return

        # TIME input with validated retry
        while True:
            time_input = input("Enter scheduled time (HH:MM 24hr): ").strip()
            try:
                datetime.strptime(time_input, "%H:%M")
                break
            except ValueError:
                print(" Invalid time format.")
                while True:
                    retry = input("Do you want to retry? (yes/no): ").strip().lower()
                    if retry in ['yes', 'no']:
                        break
                    else:
                        print("Please enter 'yes' or 'no'.")
                if retry == 'no':
                    return

        # Add to schedules
        new_schedule = pd.DataFrame([{
            'pickup_id': pickup_id,
            'area_code': area_code,
            'frequency': frequency,
            'vehicle_id': vehicle_id,
            'time': time_input
        }])
        schedules = pd.concat([schedules, new_schedule], ignore_index=True)
        schedules.to_csv(SCHEDULE_FILE, index=False)

        # Update vehicle assigned area
        vehicles.loc[vehicles['vehicle_id'] == vehicle_id, 'assigned_area'] = area_code
        vehicles.to_csv(VEHICLE_FILE, index=False)

        print(f" Schedule '{pickup_id}' added successfully.")
        print(f" Vehicle '{vehicle_id}' updated with assigned area '{area_code}' in vehicles.csv.")

        while True:
            again = input("Add another schedule? (yes/no): ").strip().lower()
            if again in ['yes', 'no']:
                break
            else:
                print("Please enter 'yes' or 'no'.")
        if again == 'no':
            break




# Recycling Unit Tracker
def track_recycling():
    recycling = pd.read_csv(RECYCLING_FILE)
    print("\n--- Recycling Unit Tracker ---")
    print("1. Add unit\n2. View units\n3. Update unit status")
    choice = input("Choose: ")
    if choice == '1':
        uid = input("Enter Unit ID: ")
        status = input("Enter Status (working/full/maintenance): ")
        cap = input("Enter Capacity: ")
        new_unit = pd.DataFrame([{
            'unit_id': uid,
            'status': status,
            'capacity': cap
        }])
        recycling = pd.concat([recycling, new_unit], ignore_index=True)
        recycling.to_csv(RECYCLING_FILE, index=False)
        print(" Unit added.")
    elif choice == '2':
        print(recycling)
    elif choice == '3':
        uid = input("Enter Unit ID: ")
        new_status = input("Enter New Status: ")
        recycling.loc[recycling['unit_id'] == uid, 'status'] = new_status
        recycling.to_csv(RECYCLING_FILE, index=False)
        print(" Status updated.")

# Report Generator
def generate_reports():
    print("\n---  Reports ---")
    areas = pd.read_csv(AREA_FILE)
    complaints = pd.read_csv(COMPLAINT_FILE)
    vehicles = pd.read_csv(VEHICLE_FILE)

    print("\nComplaints by Status:")
    print(complaints.groupby('status').size())

    print("\nVehicles Assigned per Area:")
    print(vehicles.groupby('assigned_area').size())

    print("\nAreas by Priority:")
    print(areas.groupby('priority').size())

# Main Menu
def main_menu(role):
    while True:
        print("\n--- Main Menu ---")
        print("1. Manage Areas")
        print("2. Manage Vehicles")
        print("3. Schedule Waste Pickup")
        print("4. Manage Complaints")
        print("5. Track Recycling Units")
        print("6. Generate Reports")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == '1':
            manage_areas()
        elif choice == '2':
            manage_vehicles()
        elif choice == '3':
            schedule_pickups()
        elif choice == '4':
            manage_complaints()
        elif choice == '5':
            track_recycling()
        elif choice == '6':
            generate_reports()
        elif choice == '0':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option.")

# Entry Point
if __name__ == "__main__":
    init_files()
    role = login()
    if role:
        main_menu(role)
