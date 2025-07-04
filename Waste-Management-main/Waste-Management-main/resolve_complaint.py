import pandas as pd
from datetime import datetime

import pandas as pd
from datetime import datetime

def resolve_complaint(complaint_id, file_path='data/complaints.csv'):
    try:
        df = pd.read_csv(file_path)

        # Ensure the 'resolution_message' column exists
        if 'resolution_message' not in df.columns:
            df['resolution_message'] = ""

        if complaint_id not in df['complaint_id'].values:
            print("Complaint ID not found.")
            return

        idx = df[df['complaint_id'] == complaint_id].index[0]

        if df.loc[idx, 'status'].lower() == 'resolved':
            print("Complaint is already resolved.")
            return

        message = input("Enter a resolution message (optional, press Enter to skip): ")

        df.loc[idx, 'status'] = 'Resolved'
        df.loc[idx, 'timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df.loc[idx, 'resolution_message'] = message

        df.to_csv(file_path, index=False)
        print(f"Complaint {complaint_id} resolved successfully.")

    except FileNotFoundError:
        print("complaints.csv file not found.")


def view_complaints(show_only_open=False, show_only_resolved=False, file_path='data/complaints.csv'):
    try:
        df = pd.read_csv(file_path)

        if df.empty:
            print("No complaints found.")
            return

        if show_only_open:
            df = df[df['status'].str.lower() == 'open']
            if df.empty:
                print("No open complaints.")
                return

        if show_only_resolved:
            df = df[df['status'].str.lower() == 'resolved']
            if df.empty:
                print("No resolved complaints.")
                return

        print("\n Complaints List:")
        print(df.to_string(index=False))

    except FileNotFoundError:
        print("complaints.csv file not found.")

