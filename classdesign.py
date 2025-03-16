class MentalHealthSession:
    def __init__(self, counselor_name, patient_name, session_duration, session_date):
        self.counselor_name = counselor_name
        self.patient_name = patient_name
        self.session_duration = session_duration
        self.session_date = session_date
        self.is_active = False
    
    def start_session(self):
        self.is_active = True
        print(f"Session started between {self.counselor_name} and {self.patient_name} on {self.session_date}.")
    
    def end_session(self):
        self.is_active = False
        print(f"Session ended between {self.counselor_name} and {self.patient_name}.")
    
    def get_session_info(self):
        status = "Active" if self.is_active else "Inactive"
        return (f"Counselor: {self.counselor_name}\n"
                f"Patient: {self.patient_name}\n"
                f"Duration: {self.session_duration} minutes\n"
                f"Date: {self.session_date}\n"
                f"Status: {status}")

# Example usage
session = MentalHealthSession("Dr. Alfonce", "Otieno", 50, "2025-03-17")
session.start_session()
print(session.get_session_info())
session.end_session()
