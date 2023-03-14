import pp

Trabajadores=pp.Server()
print("Numero de procesaores: ",Trabajadores.get_ncpus())

#Cerca de la linea 874 en el archivo pp.py se puede encontrar la linea de codigo:
# os.popen('TASKKILL /PID '+str(worker.pid)+' /F')
#Como administrador se modificara por la siguiente linea:
# os.popen('TASKKILL /PID '+str(worker.pid)+' /F >NUL')
