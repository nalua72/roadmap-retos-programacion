import datetime

hoy = datetime.datetime.now()
print("Hoy es:", hoy.strftime("%Y-%m-%d %H:%M:%S"))

fecha_nacimiento = datetime.datetime(1972, 7, 10, 8, 30, 0)
print("Fecha de nacimiento:", fecha_nacimiento.strftime("%Y-%m-%d %H:%M:%S"))

edad = hoy - fecha_nacimiento
print("Edad en días:", edad.days)
print("Edad en segundos:", edad.total_seconds())
print("Edad en años:", edad.days // 365)
print("Edad en meses:", edad.days // 30)
print("Edad en semanas:", edad.days // 7)

# EXTRA

print("Fecha de nacimiento:", fecha_nacimiento.strftime("%Y-%m-%d %H:%M:%S"))
print("Día de la semana:", fecha_nacimiento.strftime("%A"))
print("Día del año:", fecha_nacimiento.strftime("%j"))
print("Semana del año:", fecha_nacimiento.strftime("%U"))
print("Día del mes:", fecha_nacimiento.strftime("%d"))
print("Mes del año:", fecha_nacimiento.strftime("%B"))
print("Año:", fecha_nacimiento.strftime("%Y"))
print("Hora:", fecha_nacimiento.strftime("%H"))
print("Minuto:", fecha_nacimiento.strftime("%M"))
print("Segundo:", fecha_nacimiento.strftime("%S"))
print("AM/PM:", fecha_nacimiento.strftime("%p"))
print("Zona horaria:", fecha_nacimiento.strftime("%Z"))
print("Fecha de nacimiento (formato largo):", fecha_nacimiento.strftime("%A, %d de %B de %Y"))
print("Fecha de nacimiento (formato corto):", fecha_nacimiento.strftime("%d/%m/%Y"))
print("Fecha de nacimiento (ISO 8601):", fecha_nacimiento.isoformat())