
class Admin():
	"""
		@author Jordi Hoock Castro
	"""


	# The path to the project folder.
	pROOT = ""

	# Data Handlers object.
	data = object()

	# Commands.
	cmd = object()

	def __init__(self, path, cmd, data):
		self.data  = data
		self.cmd = cmd
		if(self.data.new):
			self.projectNew()

	def projectNew(self):
		# Data input.
		data = []
		data.append(input("Name:"))
		data.append(input("Project Name:"))
		data.append(input("Data:"))
		data.append(input("Syntax:"))
		
		# Columns.
		columns=["UserName","ProjectName","cData", "Syntax"]
		
		# Insert
		self.data.insertData("project", columns, data)

	def getFdata(self, cString):
		cmd = cString.split("-")[1].split("+")
		return cmd

	def createFString(self, command):
		c = self.getFdata(command)
		l = len(c)
		args = "("
		for x in range(1,l):
			args += c[x]
			if(x+1 != l):
				args += ", "
		args += ")"

		return c[0], args

	def eFunction(self, f):
		return f in dir(self.cmd)

	def callFunction(self, command):
		s = self.createFString(command)
		if(self.eFunction(s[0])):
			eval("self.cmd.%s%s" % (s[0], s[1]) )


