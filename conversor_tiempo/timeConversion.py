"""_summary_
    Funciones que reciben como parámetro un valor y realizan la conversión del mismo

    Args:
        time: valor a convertir
        
    Type_Conv:
    
    1. Hora a minuto
    2. Hora a segundo
    3. Minuto a hora
    4. Minuto a segundo
    5. Segundo a hora
    6. Segundo a Minuto

    Returns:
        return X (Nombre de la variable del valor a retornar): El resultado de convertir el parámetro recibido
    """

def hourToMinute_Convert(time):
    minute = 0
    minute = time * 60
    return minute

def hourToSecond_Convert(time):
    second = 0
    second = time * 3600
    return second

def minuteToHour_Convert(time):
    hour = 0
    hour = time / 60
    return hour

def minuteToSecond_Convert(time):
    second = 0
    second = time * 60
    return second

def secondToHour_Convert(time):
    hour = 0
    hour = time / 3600
    return hour

def secondToMinute_Convert(time):
    minute = 0
    minute = time / 60
    return minute