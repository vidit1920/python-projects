from admin_part import User
from Area_Management import City
from vehiclemanagement import VehicleManager
from new_complaint import file_complaint
from resolve_complaint import resolve_complaint
from reports import generate_reports
from waste_pickup import schedule_pickups
from recyclingmanagement import track_recycling_units
from resolve_complaint import resolve_complaint, view_complaints
from new_complaint import manage_complaints



city = City("YOUR CITY") 
city.load_from_csv()
vehicle_manager = VehicleManager()

def manage_areas_menu():
    while True:
        print("\n--- Manage Areas ---")
        print("1. Add Area")
        print("2. Update Area Name")
        print("3. Delete Area")
        print("4. Display All Areas")
        print("5. Back to Admin Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            area_name = input("Enter Area Name: ")
            pincode = int(input("Enter Area Pincode: "))
            population = int(input("Enter Population: "))
            try:
                city.add_area(area_name, pincode, population)
                print(" Area added.")
            except ValueError as e:
                print(f" {e}")

        elif choice == '2':
            old_name = input("Enter Existing Area Name: ")
            new_name = input("Enter New Area Name: ")
            try:
                city.update_area_name(old_name, new_name)
                print(" Area name updated.")
            except ValueError as e:
                print(f" {e}")

        elif choice == '3':
            area_name = input("Enter Area Name to Delete: ")
            try:
                city.delete_area(area_name)
                print(" Area deleted.")
            except ValueError as e:
                print(f" {e}")

        elif choice == '4':
            print("\n Current City and Areas:")
            print(city)

        elif choice == '5':
            print(" Returning to Admin Menu.")
            break

        else:
            print(" Invalid choice.")
def resolve_complaint_menu(role='user'):
    while True:
        print("\n--- 🛠️ Complaint Resolution ---")
        print("1. Resolve Complaint")
        print("2. View Open Complaints")
        if role == 'admin':
            print("3. View Resolved Complaints")
            print("4. Back")
        else:
            print("3. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            complaint_id = input("Enter Complaint ID to resolve: ")
            resolve_complaint(complaint_id)

        elif choice == '2':
            view_complaints(show_only_open=True)

        elif choice == '3' and role == 'admin':
            view_complaints(show_only_resolved=True)

        elif (choice == '3' and role != 'admin') or (choice == '4' and role == 'admin'):
            print(" Returning to previous menu.")
            break

        else:
            print(" Invalid option.")

def admin_menu():
    while True:
        print("\n---  Admin Menu ---")
        print("1. Manage Areas")
        print("2. Add Vehicle")
        print("3. Complaints")
        print("4. Schedule Waste Pickup")
        print("5. Track Recycling Units")
        print("6. Generate Reports")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_areas_menu()

        elif choice == '2':
            vehicle_id = input("Enter Vehicle ID: ")
            model = input("Enter Vehicle Model: ")
            capacity = int(input("Enter Capacity: "))
            vehicle_manager.add_vehicle(vehicle_id, model, capacity)

        elif choice == '3':
            resolve_complaint_menu(role='admin')



        elif choice == '4':
            schedule_pickups()

        elif choice == '5':
            track_recycling_units()

        elif choice == '6':
            generate_reports()

        elif choice == '7':
            print("👋 Exiting Admin Menu.")
            break

        else:
            print("Invalid choice.")

def staff_menu():
    while True:
        print("\n---  Staff Menu ---")
        print("1. Add Vehicle")
        print("2. Complaints")
        print("3. Schedule Waste Pickup")
        print("4. Track Recycling Units")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_id = input("Enter Vehicle ID: ")
            model = input("Enter Vehicle Model: ")
            capacity = int(input("Enter Capacity: "))
            vehicle_manager.add_vehicle(vehicle_id, model, capacity)

        elif choice == '2':
            complaint_id = input("Enter Complaint ID to resolve: ")
            resolve_complaint(complaint_id)

        elif choice == '3':
            schedule_pickups()

        elif choice == '4':
            track_recycling_units()

        elif choice == '5':
            print("👋 Exiting Staff Menu.")
            break
        else:
            print("Invalid choice.")

def user_menu():
    while True:
        print("\n---  User Menu ---")
        print("1. File Complaint")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            citizen_name = input("Enter Your Name: ")
            complaint_text = input("Enter Your Complaint: ")
            area_code = input("Enter Area Code: ")
            file_complaint(citizen_name, complaint_text, area_code)

        elif choice == '2':
            print("👋 Exiting User Menu.")
            break
        else:
            print("Invalid choice.")

def main():
    print("\n🛠️ Welcome to Smart Waste Management System 🛠️")
    while True:
        role_input = input("Login as (admin / staff / user) or 'exit' to quit: ").lower()
        if role_input == 'exit':
            print(" Exiting the system.")
            break

        user = User(role_input)
        logged_in_role = user.authenticate()

        if logged_in_role == 'admin':
            print("\n Welcome Admin!")
            admin_menu()
        elif logged_in_role == 'staff':
            print("\n Welcome Staff!")
            staff_menu()
        elif logged_in_role == 'user':
            print("\n Welcome User!")
            user_menu()
        else:
            print(" Login failed. Try again.")


if __name__ == "__main__":
    main()
