from conversor_tiempo.timeConversion import hourToMinute_Convert, hourToSecond_Convert, minuteToHour_Convert, minuteToSecond_Convert, secondToHour_Convert, secondToMinute_Convert
from datetime import datetime

print(f" Fecha y hora del sistema {datetime.now()}\n")

print("""
      Opciones de conversión
      
      1. Tiempo
      2. Velocidad
      """)

op = int(input("Inserte la opción deseada: "))

