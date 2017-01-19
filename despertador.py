import datetime
import time

def despierta():
	print 'ESTOLAHORA'

hora = 19
minuto = 10
segundo = 0

noeslahora = 1 

while noeslahora:
	tiempo = datetime.datetime.now()
	fecha = datetime.date.today()
	print 'hora: ',tiempo.hour
	print 'minuto: ',tiempo.minute
	print 'segundo: ',tiempo.second
	time.sleep(1)
	if hora == tiempo.hour:
		if minuto == tiempo.minute:
			noeslahora = 0

despierta()



sys.exit(0)