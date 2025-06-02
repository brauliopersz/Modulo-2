from datetime import datetime

from conversor_tiempo.timeConversion import hourToMinute_Convert, hourToSecond_Convert, minuteToHour_Convert, minuteToSecond_Convert, secondToHour_Convert, secondToMinute_Convert
from historiales_conversion.convertHistory import SpeedDiccionario, TimeDiccionario, SpeedViewHistory, TimeViewHistory
from conversor_velocidad.speedConversion import KmToMph, KmToMs, MphToKm, MphToMs, MsToKm, MsToMph

print()
#Fecha y hora del sistema actualizada
print(f" Fecha y hora del sistema {datetime.now()}\n")

#Bucle que se mantendrá realizando la tarea hasta que el usuario decida salir
while True:
      #Se imprime en pantalla las opciones para que el usuario pueda seleccionar
      print("""
            Opciones de conversión
            
            1. Tiempo
            2. Velocidad
            3. Historial de conversiones por pantalla
            4. Exportar historial en formato CSV
            5. Salir
            """)
      #Se declara variable op y se realiza conversión explicita del input a int
      op = int(input("Inserte la opción deseada: "))
      #Dependiendo la selección del usuario, se realizará un tipo X de conversión
      
      if op == 1:
            print("Conversión de Tiempo! \n")
            print("""
                  1. Hora a minuto
                  2. Hora a segundo
                  3. Minuto a hora
                  4. Minuto a segundo
                  5. Segundo a hora
                  6. Segundo a Minuto
                  """)
            
            op = int(input("Indique el tipo de conversión que desea realizar: "))
            #Se almacena el tipo de conversión en la variable tipo
            #Se solicita al usuario digitar el valor a convertir
            #Se imprime el resultado de la conversión utilizando la función correspondiente
            #Se guarda el resultado de la conversión en la variable resultado
            #Se almacenan los datos de las variables tipo, h/s/m, y resultado pasandolos como argumento a la función TimeDiccionario
            if op == 1:
                  tipo = "Hora a minuto"
                  print(f"{tipo}\n")
                  horas = int(input("Inserte el tiempo expresado en Hora/s: "))
                  print(f"{horas} horas expresado en minutos es igual a {hourToMinute_Convert(horas)} minutos")
                  resultado = hourToMinute_Convert(horas)
                  TimeDiccionario(horas, tipo, resultado)
                  
            
            elif op == 2:
                  tipo = "Hora a segundo"
                  print(f"{tipo}\n")
                  horas = int(input("Inserte el tiempo expresado en Hora/s: "))
                  print(f"{horas} horas expresado en segundos es igual a {hourToSecond_Convert(horas)} segundos")
                  resultado = hourToSecond_Convert(horas)
                  TimeDiccionario(horas, tipo, resultado)
            
            elif op == 3:
                  tipo = "Minuto a hora"
                  print(f"{tipo}\n")
                  minutos = int(input("Inserte el tiempo expresado en Minuto/s: "))
                  print(f"{minutos} Minuto/s expresado en hora/s es igual a {minuteToHour_Convert(minutos)} hora/s")
                  resultado = minuteToHour_Convert(minutos)
                  TimeDiccionario(minutos, tipo, resultado)
            
            elif op == 4:
                  tipo = "Minuto a segundo"
                  print(f"{tipo}\n")
                  minutos = int(input("Inserte el tiempo expresado en Minutos/s: "))
                  print(f"{minutos} minuto/s expresado en segundos es igual a {minuteToSecond_Convert(minutos)} segundos")
                  resultado = minuteToSecond_Convert(minutos)
                  TimeDiccionario(minutos, tipo, resultado)
            
            elif op == 5:
                  tipo = "Segundo a hora"
                  print(f"{tipo}\n")
                  segundos = int(input("Inserte el tiempo expresado en Segundos/s: "))
                  print(f"{segundos} Segundos expresado en horas es igual a {secondToHour_Convert(segundos)} hora/s")
                  resultado = secondToHour_Convert(segundos)
                  TimeDiccionario(segundos, tipo, resultado)
            
            elif op == 6:
                  tipo = "Segundo a Minuto"
                  print(f"{tipo}\n")
                  segundos = int(input("Inserte el tiempo expresado en Segundo/s: "))
                  print(f"{segundos} Segundo/s expresado en minutos es igual a {secondToMinute_Convert(segundos)} minuto/s")
                  resultado = secondToMinute_Convert(segundos)
                  TimeDiccionario(segundos, tipo, resultado)
            

      elif op == 2:
            print("Conversión de velocidad \n")
            print("""
                  1. Kilometro por hora a Metro por Segundo
                  2. Kilometro por hora a Milla por Hora
                  3. Metro por Segundo a Kilometro por Hora
                  4. Metro por Segundo a Milla por Hora
                  5. Milla por Hora a Kilometro por Hora
                  6. Milla por Hora a Metro por segundo
                  """)
            op = int(input("Inserte la opción deseada: "))
            #Se almacena el tipo de conversión en la variable tipo
            #Se solicita al usuario digitar el valor a convertir
            #Se imprime el resultado de la conversión utilizando la función correspondiente
            #Se guarda el resultado de la conversión en la variable resultado
            #Se almacenan los datos de las variables tipo, km/ms/mph, y resultado pasandolos como argumento a la función SpeedDiccionario
            if op == 1:
                  tipo = "Kilometro/s por hora a Metro/s por Segundo"
                  print(f"{tipo}\n")
                  km = int(input("Inserte el valor expresado en Kilometro/s: "))
                  print(f"El resultado de convertir {km} {tipo} es igual a: {KmToMs(km)}")
                  resultado = KmToMs(km)
                  SpeedDiccionario(km, tipo, resultado )
                  
            elif op == 2:
                  tipo = "Kilometro/s por hora a Milla/s por Hora"
                  print(f"{tipo}\n")
                  km = int(input("Inserte el valor expresado en Kilometro/s: "))
                  print(f"El resultado de convertir {km} {tipo} es igual a {KmToMph(km)}")
                  resultado = KmToMph(km)
                  SpeedDiccionario(km, tipo, resultado )
                  
            elif op == 3:
                  tipo = "Metro/s por Segundo a Kilometro/s por Hora"
                  print(f"{tipo}\n")
                  metro = int(input("Inserte el valor expresado en Metros: "))
                  print(f"El resultado de convertir {metro} {tipo} es igual a {MsToKm(metro)}")
                  resultado = MsToKm(metro)
                  SpeedDiccionario(metro, tipo, resultado )
                  
            elif op == 4:
                  tipo = "Metro/s por Segundo a Milla/s por Hora"
                  print(f"{tipo}\n")
                  metro = int(input("Inserte el valor expresado en Metros: "))
                  print(f"El resultado de convertir {metro} {tipo} es igual a {MsToMph(metro)}")
                  resultado = MsToMph(metro)
                  SpeedDiccionario(metro, tipo, resultado )
                  
            elif op == 5:
                  tipo = "Milla/s por Hora a Kilometro/s por Hora"
                  print(f"{tipo}\n")
                  milla = int(input("Inserte el valor expresado en Milla/s: "))
                  print(f"El resultado de convertir {milla} {tipo} es igual a {MphToKm(milla)}")
                  resultado = MphToKm(milla)
                  SpeedDiccionario(milla, tipo, resultado )
                  
            elif op == 6:
                  tipo = "Milla por Hora a Metro por segundo"
                  print(f"{tipo}\n")
                  milla = int(input("Inserte el valor expresado en Milla/s: "))
                  print(f"El resultado de convertir {milla} en {tipo} es igual a {MphToMs(milla)}")
                  resultado = MphToMs(milla)
                  SpeedDiccionario(milla, tipo, resultado )
                  
            else:
                  print("Inserte una opción válida!")

      elif op == 3:
            #El usuario podrá visualizar las conversiones realizadas utilizando las funciones TimeViewHistory y SpeedHistory
            TimeViewHistory()
            SpeedViewHistory()
            
      elif op == 4:
            print("Exportar historial en CSV")
            
      elif op == 5:
            #El usuario podrá salir del programa
            print("Hasta pronto!")
            exit()
            
      else:
            print("Inserte una opción válida!")

