class Patient(object):
    patient_count = 0
    def __init__(self, name, allergies):
        self.id = Patient.patient_count
        self.name = name
        self.allergies = allergies
        self.bed_num = None
        Patient.patient_count += 1    

class Hospital(object):
    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity 
        self.beds = self.get_a_bed()

    def get_a_bed(self):
        beds = []
        for i in range(0, self.capacity):
            beds.append({
                "bed_id": i,
                "available": True
            })
        return beds

    def admit(self, new_patient):
        if len(self.patients) < self.capacity:
            self.patients.append(new_patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["available"]:
                    new_patient.bed = self.beds[i]["bed_id"]
                    new_patient.bed_num = new_patient.bed
                    self.beds[i]["available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(new_patient.name, new_patient.bed)
            return self
        else:
            print "hospital is at full capacity"
            return self    
    
    def discharge(self, patient_id):
        for var in self.patients:
            if patient_id == var:
                self.patients.remove(var)
                for x in self.beds:
                    if x['bed_id'] == patient_id.bed_num:
                        x['available'] = True
                        return self
           
FirstHospital = Hospital("hospital", 5)
BillyBob = Patient("Billy Bob", "dairy")
franklink = Patient("Franklin Templeton", "nuts")
pat3 = Patient("jojo", "cleaning")
pat4 = Patient("Bob", "shellfish")
pat5 = Patient("Flippy", "meat")

FirstHospital.admit(BillyBob).admit(franklink).admit(pat3).admit(pat4).discharge(pat3).admit(pat5)
