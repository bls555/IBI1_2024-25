class Patient:
    
    def __init__(self, name, age, date_of_latest_admission, medical_history):
        """
        Initialize a Patient object with the following attributes:
        - name: str, the name of the patient
        - age: int, the age of the patient
        - date_of_latest_admission: str, the date of the latest admission in 'YYYY-MM-DD' format
        - medical_history: str, the medical history of the patient
        """
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history

    def print_details(self):
        
        print(f"name: {self.name}, age {self.age}, the date of latest admission:{self.date_of_latest_admission}, medical history:{self.medical_history}")

# example
patient = Patient("John", 25, "2024-05-20", "fever, heart attack")
patient.print_details()