from datetime import datetime

fechayhora = datetime.now()

print(fechayhora)

# acceder a varios item de la fecha

año = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day

# acceder a varios item de la hora

hora = fechayhora.hour
minutos = fechayhora.minute
segundos = fechayhora.second
microsegundos = fechayhora.microsecond

print("la hora actualemte es {}:{}:{}".format(hora,minutos,segundos))
