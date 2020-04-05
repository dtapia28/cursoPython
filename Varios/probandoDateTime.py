import datetime

now = datetime.datetime.now()

print(now)

#Mostrando ciertos datos de now

print("El día es "+str(now.day))
print("El mes es "+str(now.month))
print("El año es "+str(now.year))
print("Los minutos son "+str(now.minute))


#Reemplazando en horario
print("Cambiando el día a 20")
print(now.replace(day=20))
print("Esto no cambia el valor de now")
print(now)
now=now.replace(day=18,year=2030,month=10)
print("Ahora si cambia el valor de now")
print(now)
fecha = now+datetime.timedelta(days=5)
print(fecha)
print(now.date())

now = datetime.datetime.now()
today = datetime.datetime.today()

print(now)
print(today)
print(datetime.time())

#Metodo combine
#Combinar today con time

print(datetime.datetime.combine(datetime.datetime.today(), datetime.time()))



##Formatenado fechas

ahora = datetime.datetime.now()
print(ahora)
print("Dando formato día/mes/año a fecha: "+ahora.strftime("%B %d, %Y"))


##Sacar fecha desde un string
fecha = "25/10/1989"
tomar_fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")
print(tomar_fecha)



#Zonas horarias
horario_chile = datetime.timezone(datetime.timedelta(hours=-3))


horaEstEste = datetime.timezone(datetime.timedelta(hours=-5))

hora_china = datetime.timezone(datetime.timedelta(hours=+8))


#Horario en Santiago, Shanghái y Washington


santiago = datetime.datetime.now(horario_chile)
washnigton = datetime.datetime.now(horaEstEste)
shanghai = datetime.datetime.now(hora_china)

print("En Santiago de Chile son las "+str(santiago.strftime("%H:%M")))
print("En Washington DC. son las "+str(washnigton.strftime("%H:%M")))
print("En Shanghái son las "+str(shanghai.strftime("%H:%M")))



# Horario del mundo en mi nacimiento

nacimiento = "25/10/1989 03:28:43"

tomar_fecha = datetime.datetime.strptime(nacimiento, "%d/%m/%Y %H:%M:%S")

en_china=tomar_fecha.astimezone(hora_china)
print(en_china)