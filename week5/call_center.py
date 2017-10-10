
import datetime

class Call(object):
	def __init__(self, name, phone, reason, call_id=1):
		
		self.id = call_id
		self.name = name
		self.phone = phone
		self.time = datetime.datetime.now()
		self.reason = reason
		call_id += 1

	def display(self):
		print "Caller ID: {}; Name: {}; Phone# {}; Time: {}; Reason: {}".format(self.id, \
		self.name, self.phone, str(self.time.strftime('%Y-%m-%d %I:%-M %p')), self.reason)

	def __repr__(self):
		return "<Call Object {}: {}>".format(self.id, self.phone)

caller1 = Call("Kevin Dunn", "555-5555", "When is lunch?")
caller1.display()
caller2 = Call("Davy Jones", "none", "Where's me treasure!")
caller2.display()
caller3 = Call("Bobby", "455-5545", "Running out of propane.")
caller3.display()

class Call_Center(object):
	def __init__(self):
		self.calls = []

	@property
	def queue(self):
		return len(self.calls)

	def add(self, call):
		self.calls.append(call)
		return self

	def remove(self):
		self.calls.pop(0)
		return self

	def info(self):
		# print self.name
		# print self.phone 
		print self.queue 
		return self

center = Call_Center()
center.add(caller1).add(caller2).info().remove().info().add(caller3).info()


