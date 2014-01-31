import sqlite3 as sql

class dataHandler():
	""" 
		This class is used for file management.
	"""
	
	# System db name.
	DB_SYSN  	= "data.db"
	
	# DB Connection.
	dbc			= object()

	# Define if the project is new or not.
	new 		= False

	def __init__(self, path):
		# Formatting path to db.
		tp = path + self.DB_SYSN

		# DB Connection.
		self.dbc		= sql.connect("%s" % tp)
		self.q 			= self.dbc.cursor()
		
		try:
			pdata = self.q.execute("SELECT * FROM project").fetchall()
			self.new = False
			print("Bienvenido de nuevo, %s, iniciando su proyecto %s." %  (pdata[0][0], pdata[0][1]) )
		except:
			self.new = True
			self.createDataBase()

	def createDataBase(self):
		self.q.execute("CREATE TABLE project (UserName TEXT NOT NULL, ProjectName TEXT NOT NULL, cData TEXT NOT NULL, Syntax TEXT NOT NULL);")
		self.dbc.commit()

	def insertData(self, table, columns, data):
		# Format the strings.
		fc = self.formatString(columns,data)[0]
		fd = self.formatString(columns,data)[1]

		qs = "INSERT INTO %s (%s) Values (%s)" % (table, fc, fd)
		self.q.execute(qs)
		self.dbc.commit()

	def formatString(self, columns, data):
		cs = ""
		for s in columns:
			if(s == columns[len(columns)-1]):
				cs +="'"+s+"'"
			else:
				cs +="'"+s+"',"

		ds = ""
		for s in data:
			if(s == data[len(data)-1]):
				ds +="'"+s+"'"
			else:
				ds +="'"+s+"',"

		return cs, ds


			

		