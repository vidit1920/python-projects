# admin_part.py

class User:
    admin_credentials = {
        "admin": "admin123"
    }

    staff_credentials = {
        "staff1": "staff1123",
        "staff2": "staff2123"
    }

    def __init__(self, role):
        self.role = role.lower()

    def authenticate(self):
        if self.role == 'admin':
            user_id = input("Enter Admin ID: ")
            password = input("Enter Admin Password: ")
            if user_id in self.admin_credentials and self.admin_credentials[user_id] == password:
                print(" Admin login successful.")
                return 'admin'
            else:
                print(" Wrong admin credentials.")
                return None

        elif self.role == 'staff':
            user_id = input("Enter Staff ID: ")
            password = input("Enter Staff Password: ")
            if user_id in self.staff_credentials and self.staff_credentials[user_id] == password:
                print("Staff login successful.")
                return 'staff'  
            else:
                print(" Wrong staff credentials.")
                return None

        elif self.role == 'user':
            print(" User login successful. No password needed.")
            return 'user'   

        else:
            print(" Invalid role entered.")
            return None
