import pandas as pd
from datetime import datetime

def file_complaint(citizen_name, complaint_text, area_code, file_path='data/complaints.csv'):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = "Open"

    try:
        df = pd.read_csv(file_path)

    
        if 'complaint_id' not in df.columns:
            df = pd.DataFrame()
            new_id = "CM001"
        else:
            last_id = df['complaint_id'].iloc[-1] if not df.empty else 'CM000'
            last_num = int(last_id.replace('CM', ''))
            new_id = f"CM{last_num + 1:03}"
    except FileNotFoundError:
        
        df = pd.DataFrame()
        new_id = "CM001"


    new_complaint = {
        'complaint_id': new_id,
        'citizen_name': citizen_name,
        'area_code': area_code,
        'description': complaint_text,
        'status': status,
        'timestamp': timestamp
    }

    # Append to file and save
    df = pd.concat([df, pd.DataFrame([new_complaint])], ignore_index=True)
    df.to_csv(file_path, index=False)
    print(f" Complaint filed successfully with ID {new_id}")

def manage_complaints():
    print("This is the complaints menu.")
    # Add logic here...

