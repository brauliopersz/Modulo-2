
timeHistory = {}
SpeedDic = {}
indice = 0


#Función en donde se encuentra el Diccionario en donde se almacenan las conversiones realizadas en el módulo principal
def TimeDiccionario(time, tipo, resultado):
    global timeHistory
    global indice
    
    indice += 1
    
    timeHistory [indice]= {
        
        "time": time,
        "tipo": tipo,
        "resultado": resultado
    }
    
#Función en donde se encuentra el Diccionario en donde se almacenan las conversiones realizadas en el módulo principal
def SpeedDiccionario(speed, tipo, resultado):
    
    global SpeedDic
    global indice
    indice += 1
    SpeedDic [indice] = {
        "speed": speed,
        "tipo" :tipo,
        "resultado": resultado
    }
    
    
#Función para poder visualizar los datos almacenados de manera provisional en el diccionario
def TimeViewHistory():
    for clave, valor in timeHistory.items():
        print(f"{clave} - Valor convertido: {valor['time']}, Tipo de conversión: {valor['tipo']}, Resultado de la conversión: {valor['resultado']} ")
        
def SpeedViewHistory():
    for clave, valor in SpeedDic.items():
        print(f"{clave} - Valor convertido: {valor['speed']}, Tipo de conversión: {valor['tipo']}, Resultado de la conversión: {valor['resultado']}")



def GuardarInformacionDiccionario(speed, time, tipo, resultado, nombre_archivo = '/Modulo-2/historial.csv'):
    with open(nombre_archivo, mode='a', encoding='utf-8') as archivo:
        archivo.write(f"{speed}, {time}, {tipo}, {resultado}")
        print(f"Informacion del tipo de conversion {tipo} ha sido guardada exitosamente")
                

def cvsHistory():
    pass
        