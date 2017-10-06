
class Patient(object):
	count = 0
	def __init__(self, pa_name, allergies):
		Patient.count += 1
		self.id = Patient.count
		self.pa_name = pa_name 
		self.allergies = allergies
		self.bed_number = None
	
	def display(self):
		print "Patient ID: {}; Name: {}; Allergies: {}".format(self.id, self.pa_name, self.allergies)


class Hospital(object):
	num_of_patients = 0
	def __init__(self, hosp_name, capacity):
		self.hosp_name = hosp_name
		self.capacity = capacity
		self.patients = []
		self.beds = []
		for bed in range(0, capacity):
			self.beds.append({"Bed#": bed, "Available": True})

	def admit(self, patient_in):
		if len(self.patients) >= self.capacity:
			print "Sory, no more room for patients at {}".format(self.hosp_name)
		else:
			self.patients.append(patient_in)
			for bed in range(0, len(self.beds)):
				if self.beds[bed]["Available"]:
					patient_in.bed_number = self.beds[bed]["Bed#"]
					self.beds[bed]["Available"] = False
					break
			print "We are up to {} patients".format(len(self.patients))
			return self
	def discharge(self, patient_out):
		for patient in self.patients:
				if patient.id == patient_out.id:
					for bed in self.beds:
						if bed["Bed#"] == patient.bed_number:
							bed["Available"] = True
							break
				if patient.id == patient_out.id:
					self.patients.remove(patient)

				if len(self.patients) == 0:
					print "Wow! Good job everyone. We are all out of patients!"
				else: 
					print "We are down to {} patients".format(len(self.patients))
		return self

# -------------------------------------------------------------------------------------
patient_a = Patient("Kevin", "cats")
patient_b = Patient("Egon", ["spoors", "molds", "fungus"])
patient_b.display()

hospital_a = Hospital("Nashville Hospital", 5)
hospital_a.admit(patient_a)
hospital_a.admit(patient_b)

hospital_a.discharge(patient_a)
hospital_a.discharge(patient_b)