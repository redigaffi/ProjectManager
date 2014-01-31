from Admin import Admin
from dataHandler import dataHandler
from cmd import cmd


print("La ruta hacía el proyecto, si aún no tiene proyecto indique la nueva ruta: ")
path = input()

data = dataHandler(path)
cmd = cmd()
Admin = Admin(path, cmd, data)

todo = ""
while (todo != "exit"):
	todo = input("Que desea hacer: ")
	Admin.callFunction(todo)