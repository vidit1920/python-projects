import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

def generate_reports():
    print("\n--- 📊 Reports Menu ---")
    print("1. Complaint Report (Bar Graph)")
    print("2. Area Population Report (Bar Graph)")
    print("3. Complaint Distribution (Pie Chart)")
    print("4. Back")

    try:
        complaints = pd.read_csv('data/complaints.csv')
    except:
        complaints = pd.DataFrame(columns=['status'])

    try:
        areas = pd.read_csv('data/areas.csv')
    except:
        areas = pd.DataFrame(columns=['Area Name', 'Pincode', 'Population'])

    while True:
        choice = input("Choose report to view (1–4): ")

        if choice == '1':
            if complaints.empty:
                print(" No complaints data found.")
                continue

            complaints['status'] = complaints['status'].str.capitalize()
            status_counts = complaints['status'].value_counts()

            print("\nComplaint Status Summary:")
            print(status_counts.to_string())

            status_counts.plot(kind='bar', title='Complaint Status Report', ylabel='Number of Complaints')
            plt.tight_layout()
            plt.show()

        elif choice == '2':
            if 'Area Name' in areas.columns and 'Population' in areas.columns:
                sorted_areas = areas.sort_values(by='Population', ascending=False)

                print("\nArea Population Summary:")
                print(sorted_areas[['Area Name', 'Population']].to_string(index=False))

                plt.bar(sorted_areas['Area Name'], sorted_areas['Population'])
                plt.title('Population by Area')
                plt.xlabel('Area Name')
                plt.ylabel('Population')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            else:
                print(" 'Area Name' or 'Population' column missing in areas.csv.")

        elif choice == '3':
            if complaints.empty:
                print(" No complaints data to display.")
                continue

            complaints['status'] = complaints['status'].str.capitalize()
            pie_data = complaints['status'].value_counts()

            if not pie_data.empty:
                pie_data.plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Complaint Distribution')
                plt.ylabel("")
                plt.tight_layout()
                plt.show()
            else:
                print(" No valid data for pie chart.")

        elif choice == '4':
            print("Returning to main menu.")
            break

        else:
            print(" Invalid option. Please choose between 1–4.")

